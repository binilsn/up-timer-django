from django.urls import path

from monitors import views

app_name = "monitors"

urlpatterns = [path("", views.index, name="index")]
