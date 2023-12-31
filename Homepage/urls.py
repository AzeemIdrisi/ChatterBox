from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("chat", views.index, name="index"),
    path("send_message/", views.send_message, name="send_message"),
    path("send_reply/", views.send_reply, name="send_reply"),
    path("like/<int:message_id>/<str:type>/", views.like, name="like"),
]
