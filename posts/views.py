from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
