from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import IsBookOwner, BlacklistPermission
from .serializers import BookSerializer
from .models import Book


class ProtectedAPIView(APIView):
    def get(self, request, format=None):
        content = {"message": "Hey! you have authenticated!"}
        return Response(content)


class BooksViewSet(ModelViewSet):
    permission_classes = [BlacklistPermission, IsAuthenticated, IsBookOwner]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
