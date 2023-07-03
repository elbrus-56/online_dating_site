from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from register_user.serializers import CreateUserSerializer
from register_user.services.create_watermark import Watermark
from config.settings import MEDIA_ROOT


class RegisterUser(CreateAPIView):
    """
    Эндпоинт для регистрации нового пользователя
    """
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            if "default" not in str(user.photo):
                try:
                    Watermark.create_watermark(user.photo, MEDIA_ROOT / str(user.photo))
                except Exception as e:
                    print(f"RegisterUser: Не удалось нанести водяной знак на фото {user.photo} - {e}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
