from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.products, name="products"),
    path('search/', views.search, name='search'),
]

urlpatterns += staticfiles_urlpatterns()