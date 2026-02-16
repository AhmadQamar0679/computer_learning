from django.urls import path
from b_courses import views


urlpatterns = [
    path('',views.css,name='css_page'),
    path('home',views.home,name='home_page')
]
