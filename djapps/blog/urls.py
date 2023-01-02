from django.urls import path
from djapps.blog.views import BlogView


urlpatterns = [
    path("api/blogs/", BlogView.as_view())
]
