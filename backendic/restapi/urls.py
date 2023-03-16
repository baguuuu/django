from rest_framework import routers
from views import ConfigurationViewSet, UsrsViewSet, GrpViewSet

router = routers.DefaultRouter()
router.register('Configuration', ConfigurationViewSet)
router.register('Usrs', UsrsViewSet)
router.register('Grp', GrpViewSet)