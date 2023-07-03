from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from register_user.serializers import CreateUserSerializer


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
            # you can access the file like this from serializer
            # photo = serializer.validated_data["photo"]
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
