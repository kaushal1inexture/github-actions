from django.urls import path

from app1.views import HealthChecker, NumberValidator, EnvironmentExtractor

urlpatterns = [
    path('health_checker/',HealthChecker.as_view(), name="health_checker"),
    path('number_validator/<int:id_no>',NumberValidator.as_view(), name="number_validator"),
    path('env_extractor/',EnvironmentExtractor.as_view(), name="env_extractor"),
]
