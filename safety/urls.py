from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('dashboard/',
         views.dashboard,
         name='dashboard'),

    path('navigation/',
         views.navigation,
         name='navigation'),

    path('safety-zones/',
         views.safety_zones,
         name='safety_zones'),

    path('guardian/',
         views.guardian,
         name='guardian'),

    path('reports/',
         views.reports,
         name='reports'),
    path('api/zones/', views.api_zones, name='api_zones'),
    path('api/report/', views.api_report, name='api_report'),
]