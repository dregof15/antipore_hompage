from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='indenx'),
    path('<int:customer_id>/', views.detail, name='detail'),
    path('location_page/', views.location_page, name='location_page'),
    path('loading_page/', views.loading_page, name='loading_page'),
]
