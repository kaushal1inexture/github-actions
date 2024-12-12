import json
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from crud_app.models import Category
from crud_app.serializers import CategorySerializer
from crud_app.constants import (RETRIEVED_SUCCESSFULLY, CREATED_SUCCESSFULLY,
                              DELETED_SUCCESSFULLY, NOT_FOUND,
                              UPDATED_SUCCESSFULLY)


class CategoryListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        try:
            status_code = status.HTTP_200_OK
            message = RETRIEVED_SUCCESSFULLY.format('Categories')
            category_data = self.get_queryset()
            serializer = self.get_serializer(category_data, many=True)
            resp_data = {'data': serializer.data, 'status': status_code, 'message': message}
        except Exception as e:
            message = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            resp_data = {"data": [], "status": status_code, "message": message}
        return Response(resp_data, status=status_code)

    def create(self, request, *args, **kwargs):
        data = []
        try:
            message = CREATED_SUCCESSFULLY.format('Category')
            status_code = status.HTTP_201_CREATED
            serializer = self.get_serializer(data=request.data.copy())
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data
        except Exception as e:
            message = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        resp_data = {'data': data, 'message': message, 'status': status_code}
        return Response(resp_data, status=status_code)

class CategoryUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.filter(is_deleted=False)
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        data = []
        try:
            message = RETRIEVED_SUCCESSFULLY.format('Category')
            status_code = status.HTTP_200_OK
            serializer = self.get_serializer(self.get_object())
            data =serializer.data
        except Exception as e:
            message = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        resp_data = {'data': data, 'message': message, 'status': status_code}
        return Response(resp_data, status=status_code)

    def delete(self, request, *args, **kwargs):
        try:
            message = DELETED_SUCCESSFULLY.format('Category')
            status_code = status.HTTP_200_OK
            if category_data := self. queryset.filter(**kwargs):
                category_data.update(is_deleted=True, is_active= False)
            else:
                message = NOT_FOUND.format('Category')
                status_code = status.HTTP_404_NOT_FOUND
        except Exception as e:
            message = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        resp_data = {'data': [], 'message': message, 'status': status_code}
        return Response(resp_data, status=status_code)

    def put(self, request, *args, **kwargs):
        data = []
        try:
            status_code = status.HTTP_200_OK
            message = UPDATED_SUCCESSFULLY.format('Category')
            product_serializer = self.get_serializer(data=request.data,
                                                     instance=self.get_object())
            product_serializer.is_valid(raise_exception=True)
            product_serializer.save()
            data = product_serializer.data
        except Exception as e:
            message = str(e)
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        resp_data = {'data': data, 'message': message, 'status': status_code}
        return Response(resp_data, status=status_code)
