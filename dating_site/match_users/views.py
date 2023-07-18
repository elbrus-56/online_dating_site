from django.contrib.auth import get_user_model
from match_users.models import Matches
from match_users.serializers import MatchesSerializer, ParticipantSerializer
from match_users.services.notify import Notify
from rest_framework import status
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()


class MatchUsers(RetrieveAPIView):
    """
    Эндпоинт для поиска симпатий
    """
    queryset = User.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ParticipantSerializer
        return MatchesSerializer

    def post(self, request, pk: int = 1) -> Response:

        user = request.user
        participant = get_object_or_404(User, pk=pk)

        check_like_from_participant = Matches.objects.filter(
            like_to_user=user.pk, user=pk).exists()
        check_like_from_user = Matches.objects.filter(
            like_to_user=pk, user=user).exists()

        if not check_like_from_participant:

            if not check_like_from_user:
                Matches.objects.create(like_to_user=pk, user=user)
                return Response({'like': 'Ваша симпатия доставлена другому участнику'},
                                status=status.HTTP_200_OK)

            else:
                return Response({'like': 'Вы уже ставили лайк этому участнику'},
                                status=status.HTTP_200_OK)

        else:

            if not check_like_from_user:

                Matches.objects.create(like_to_user=pk, user=user)

                messages = [{'subject': 'Уведомление с сайта Dating Site',
                             'message': f'Вы понравились {user.first_name} '
                             f'{user.last_name}! Почта участника: {user.email}',
                             'emails': participant.email
                             },
                            {'subject': 'Уведомление с сайта Dating Site',
                             'message': f'Вы понравились {participant.first_name} '
                             f'{participant.last_name}! Почта участника: {participant.email}',
                             'emails': user.email
                             }]

                for message in messages:
                    Notify.send_email(subject=message['subject'],
                                      message=message['message'],
                                      emails=[message['emails']]
                                      )

                return Response({'like': f'Вы понравились {participant.first_name} ! '
                                 f'Почта участника: {participant.email}'},
                                status=status.HTTP_200_OK)

            else:
                return Response({'like': 'Вы уже ставили лайк этому участнику'},
                                status=status.HTTP_200_OK)
