from rest_framework.routers import DefaultRouter
from integration import views

app_name = 'integration'

router = DefaultRouter()
router.register('subscriptions', views.ResthookScriptionViewSet, basename='subscriptions')
router.register('tickets', views.TicketViewSet, basename='tickets')

urlpatterns = [
    *router.urls,
]
