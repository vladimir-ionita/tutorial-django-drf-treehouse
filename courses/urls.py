from django.urls import path

from . import views

urlpatterns = [
    path('', views.CourseListCreate.as_view(), name='course_list')
]
