from django.urls import path
from . import views

urlpatterns = [
    path('', views.mehndiMsgSubmit, name='mehndiMsgSubmit'),
    path('showmsgs5059/', views.mehndiShowMsgs, name='mehndiShowMsgs'),
]