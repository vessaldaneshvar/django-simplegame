from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("game/rock/<str:groupname>/",consumers.RockConsumer),
    path("game/dotsandbox/<str:groupname>/",consumers.DotsConsumerInit),
    path("game/dotsandbox/action/<str:secretgroupname>/",consumers.DotsConsumerGame),
]