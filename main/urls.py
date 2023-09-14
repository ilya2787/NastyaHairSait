from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('cosmetic', views.cosmetic, name="cosmetic"),
    path('cat_<int:cat_id>/', views.cosmetic_cat, name="cosmetic-cat"),
    path('<int:content_id>/', views.cosmetic_id, name="cosmetic-cat-id"),
    path('services', views.services, name="services"),
]
