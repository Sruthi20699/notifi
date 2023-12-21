from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path 
from myapp.consumers import Consumer

websocket_urlpatterns = [
    path('ws/notifications/', Consumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(
        websocket_urlpatterns
    ),
}

)