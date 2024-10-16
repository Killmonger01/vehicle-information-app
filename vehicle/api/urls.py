from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'

urlpatterns = [
    path('cars/', views.CarListCreateView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('cars/<int:car_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
