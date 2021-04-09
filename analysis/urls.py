from django.urls import path

from . import views

urlpatterns = [
    path('',views.display, name='display'),
    path('post',views.post, name='post'),
    path('report',views.report, name='report')
]