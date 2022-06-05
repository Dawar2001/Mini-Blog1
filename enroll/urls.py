from django.urls import path
from enroll import views

urlpatterns=[
    path('post/',views.sforms,name='loop'),
]