# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view,detail_route
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

# Create your views here.
"""
class SnippetList(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
    queryset= Snippet.objects.all()
    serializer_class=SnippetSerializer

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
"""

"""
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
"""

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        snippet=self.get_object()
        return Response(snippet.highlighted)

"""
@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'users': reverse('user-list',request=request,format=format),
        'snippets':reverse('snippet-list',request=request,format=format)
        })
"""

"""
class SnippetHighlight(generics.GenericAPIView):
    queryset=Snippet.objects.all()
    renderer_class=(renderers.StaticHTMLRenderer,)

    def get(self,request,*args,**kwargs):
        snippet=self.get_object()
        return Response(snippet.highlighted)
"""
