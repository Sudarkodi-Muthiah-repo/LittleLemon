#define URL route for index() view
from django.urls import path,include
from . import views
from .views import BookingViewSet,MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.routers import DefaultRouter
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'tables',views.BookingViewSet) 

urlpatterns = [
    path('', views.index, name='index'),
    #path('booking/',include(router.urls)),
    path('menu-items/', views.MenuItemsView.as_view()), #Menu API
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),# Single menu API
    path('api-token-auth/',obtain_auth_token),
    path('message/', views.securedview),
]
