from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments")
router.register("groups", GroupViewSet, basename="group")
router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(router.urls)),
]
