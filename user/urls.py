from user import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('me/', views.UserInfoView.as_view(), name='info'),
]
