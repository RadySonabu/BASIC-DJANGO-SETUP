from django.urls import include, path
# from .views import index

urlpatterns = [
    path('unicorn/', include('django_unicorn.urls')),
    # path('', index)
]
