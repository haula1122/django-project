from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('team/', views.team_view, name='team'),
    # path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    # path('service/', views.service_view, name='service'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('portfolio/<int:id>/', views.portfolio_view, name='portfolio-detail'),
]
