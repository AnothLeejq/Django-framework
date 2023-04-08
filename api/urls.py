from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('job/',views.addItem),
    path('job/<int:job_id>',views.searchSingleJob),
    ]
