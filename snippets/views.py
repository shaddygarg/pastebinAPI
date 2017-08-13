# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset= Snippet.objects.all()
    serializer_class=SnippetSerializer
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
