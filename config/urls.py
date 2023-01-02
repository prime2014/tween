from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import HealthCheck

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("djapps.blog.urls")),
    path("api/accounts/status/", HealthCheck.as_view())
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls))
    ]


#127.0.0.1:8000/blog/
