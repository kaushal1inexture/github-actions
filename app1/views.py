import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class HealthChecker(APIView):
    def get(self, request, *args, **kwargs):
        status_code = status.HTTP_200_OK
        resp_data = {"data": [], "message": "System is Up!", "status_code": status_code}
        return Response(resp_data, status = status_code)


class NumberValidator(APIView):
    def get(self, request, *args, **kwargs):
        id_no = None
        try:
            status_code = status.HTTP_200_OK
            message = "Successfully shared validate number."
            id_no = kwargs.get("id_no")
        except Exception as e:
            message = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        resp_data = {"data": [id_no], "message": message, "status_code": status_code}
        return Response(resp_data, status = status_code)


class EnvironmentExtractor(APIView):
    def get(self, request, *args, **kwargs):
        env_name = None
        try:
            status_code = status.HTTP_200_OK
            message = "Successfully shared env data."
            env_name = os.environ.get("name")
        except Exception as e:
            message = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        resp_data = {"data": [env_name], "message": message, "status_code": status_code}
        return Response(resp_data, status = status_code)
