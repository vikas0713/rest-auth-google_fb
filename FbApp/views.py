"""
This file was created at Smartbuzz Inc.
For more information visit http://www.smartbuzzinc.com
"""
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
	return render(
		request,
		"index.html"
	)

class MYAPI(APIView):

	def get(self,request):
		return Response({"msg": "success"})


class GetJWT(APIView):

	def post(self,request):

