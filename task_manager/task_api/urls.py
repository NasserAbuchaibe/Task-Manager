from rest_framework import routers

from .viewsets import TaskViewSet

router = routers.SimpleRouter()
router.register('task', TaskViewSet, basename='TaskModel')

urlpatterns = router.urls
