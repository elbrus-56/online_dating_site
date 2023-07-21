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

        current_user = request.user
        target_user = get_object_or_404(User, pk=pk)

        check_like_from_target_user = Matches.objects.filter(
            like_to_user=current_user.pk,
            user=pk
        ).exists()

        check_like_from_current_user = Matches.objects.filter(
            like_to_user=pk,
            user=current_user
        ).exists()

        if not check_like_from_target_user:

            if not check_like_from_current_user:
                try:
                    Matches.objects.create(like_to_user=pk, user=current_user)
                except Exception:
                    return Response({'like': 'Не удалось поставить like другому участнику'},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'like': 'Ваша симпатия доставлена другому участнику'},
                                    status=status.HTTP_200_OK)

            else:
                return Response({'like': 'Вы уже ставили лайк этому участнику'},
                                status=status.HTTP_200_OK)

        else:

            if not check_like_from_current_user:

                try:
                    Matches.objects.create(like_to_user=pk, user=current_user)
                except Exception:
                    return Response({'like': 'Не удалось поставить like другому участнику'},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    messages = [{'subject': 'Уведомление с сайта Dating Site',
                                 'message': f'Вы понравились {current_user.first_name} '
                                 f'{current_user.last_name}! Почта участника: {current_user.email}',
                                 'emails': target_user.email
                                 },
                                {'subject': 'Уведомление с сайта Dating Site',
                                 'message': f'Вы понравились {target_user.first_name} '
                                 f'{target_user.last_name}! Почта участника: {target_user.email}',
                                 'emails': current_user.email
                                 }]

                    for message in messages:
                        Notify.send_email(subject=message['subject'],
                                          message=message['message'],
                                          emails=[message['emails']]
                                          )

                    return Response({'like': f'Вы понравились {target_user.first_name} ! '
                                     f'Почта участника: {target_user.email}'},
                                    status=status.HTTP_200_OK)

            else:
                return Response({'like': 'Вы уже ставили лайк этому участнику'},
                                status=status.HTTP_200_OK)
