from django.urls import path
from b_courses import views


urlpatterns = [
    path('',views.home,name='home_page'),
]
