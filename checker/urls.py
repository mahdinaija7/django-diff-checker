from django.urls import path
from .views import checker, apiJson

urlpatterns = [
    path("", checker, name="diffChecker"),
    path("api/compare/", apiJson, name="compareApi"),
]

