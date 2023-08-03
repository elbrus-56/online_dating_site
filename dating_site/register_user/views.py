from django.contrib.auth import authenticate, login
from register_user.serializers import CreateUserSerializer, LoginSerializer
from register_user.services.watermark import Watermark
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterUser(CreateAPIView):
    '''
    Эндпоинт для регистрации нового пользователя
    '''

    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            if 'default' not in str(user.photo.name):

                try:
                    Watermark.create_watermark(
                        user.photo.path, user.photo.path)

                except FileNotFoundError:
                    print(
                        f'RegisterUser: Не удалось нанести водяной знак на \
                        фото {user.photo.name}')

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    '''
    Эндпоинт для аутентикации пользователя
    '''

    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def post(self, request):

        try:
            user = authenticate(request,
                                email=request.data['email'],
                                password=request.data['password']
                                )
            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')

        except Exception:
            return Response({'login': 'Ошибка аутентификации'},
                            status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'login': 'Аутентификация прошла успешно'},
                            status=status.HTTP_200_OK)
