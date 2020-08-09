from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from game import routing as game_routing

application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        SessionMiddlewareStack(
                URLRouter(
                    game_routing.websocket_urlpatterns
                )
            )
        )
})