from django.urls import path
from crud_app.views import CategoryListCreateView, CategoryUpdateDeleteView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='categories'),
    path('<int:pk>/', CategoryUpdateDeleteView.as_view(), name='categories_delete'),
]
