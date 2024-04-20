from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"bookmarks", views.BookmarkViewSet)


app_name = "barkyapi"

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]

# add the router's URLs to the urlpatterns
urlpatterns += router.urls