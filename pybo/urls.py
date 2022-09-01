from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='indenx'),
    path('<int:customer_id>/', views.detail, name='detail'),
]
