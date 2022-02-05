from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', include('apps.base.urls')),
    path('', include('apps.authentication.urls')),
    # path('', include('apps.movies.urls')),
]
