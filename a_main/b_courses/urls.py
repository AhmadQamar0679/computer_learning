from django.urls import path
from b_courses import views


urlpatterns = [
    path('',views.course_detail,name='course_detail'),
    path('layout/',views.layout,name='layout')
]