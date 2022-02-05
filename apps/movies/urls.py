from django.urls import include, path
from .views import MovieView

urlpatterns = [
    path('unicorn/', include('django_unicorn.urls')),
    path('', MovieView.as_view())
]
