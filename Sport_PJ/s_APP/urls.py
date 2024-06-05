from django.urls import path
from s_APP import views

urlpatterns = [
    path('', views.store_list, name='store_list'),
    path('store/<int:pk>/', views.store_detail, name='store_detail'),
    path('category/', views.category_list, name='category_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('store/add/', views.add_store, name='add_store'),
    path('store/<int:pk>/edit/', views.edit_store, name='edit_store'),
    path('store/<int:pk>/delete/', views.delete_store, name='delete_store'),
]
