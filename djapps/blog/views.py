from django.shortcuts import render
from rest_framework.views import APIView
import os
import json
from rest_framework.response import Response
from rest_framework import status



class BlogView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        djapps_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_file = os.path.join(djapps_path, "blog.json")
        with open(json_file, "r") as fp:
            articles = json.loads(fp.read())
            return Response(articles, status=status.HTTP_200_OK)
