from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializerIn, UserSerializerOut


@api_view(["GET", "POST"])
def handle_users(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializerOut(users, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer_in = UserSerializerIn(data=request.data)
        if serializer_in.is_valid():
            user = serializer_in.save()
            serializer_out = UserSerializerOut(user)
            return Response(serializer_out.data, status.HTTP_201_CREATED)
        return Response(serializer_in.errors, status.HTTP_400_BAD_REQUEST)
