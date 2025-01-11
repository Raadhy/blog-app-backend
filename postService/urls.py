from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="post")
urlpatterns = router.urls