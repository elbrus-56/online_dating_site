from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from match_users.serializers import ParticipantSerializer, MatchesSerializer
from django.contrib.auth import get_user_model
from match_users.models import Matches
from match_users.services.notify import Notify

User = get_user_model()


class MatchUsers(APIView):
    """
    Эндпоинт для поиска симпатий
    """

    serializer_class = MatchesSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def get(self, request, pk: int = 1) -> Response:
        obj = get_object_or_404(User, pk=pk)
        serializer = ParticipantSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk: int, *args, **kwargs) -> Response:
        user = User.objects.get(email=request.user)
        participant = User.objects.get(pk=pk)

        check_like_from_participant = Matches.objects.filter(like_to_user=user.pk, user=pk)

        if not check_like_from_participant:
            Matches.objects.create(like_to_user=pk, user=user)  # пользователь ставит лайк
            return Response({'like': 'Ваша симпатия доставлена другому участнику'},
                            status=status.HTTP_200_OK)

        else:

            Matches.objects.create(like_to_user=pk, user=user)

            Notify.send_email(subject='Уведомление с сайта Dating Site',
                              message=f'Вы понравились {user.first_name} {user.last_name}!'
                                      f' Почта участника: {user.email}',
                              emails=[participant.email]
                              )

            Notify.send_email(subject='Уведомление с сайта Dating Site',
                              message=f'Вы понравились {participant.first_name} {participant.last_name}!'
                                      f' Почта участника: {participant.email}',
                              emails=[user.email]
                              )
            return Response({'like': f'Вы понравились {participant.first_name} ! Почта участника: {participant.email}'},
                            status=status.HTTP_200_OK)

