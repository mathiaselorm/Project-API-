from django.urls import path
from . import views
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.apioverview, name='api_overview'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_create/', views.product_create, name='product_create'),
    path('product_detail/<str:pk>/', views.product_detail, name='product_detail'),
    path('product_update/<str:pk>/', views.product_update, name='product_update'),
    path('product_delete/<str:pk>/', views.product_delete, name='product_delete'),
    path('signup/',  views.user_signup, name='signup'),
    
]