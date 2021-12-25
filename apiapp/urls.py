from django.urls import path

from apiapp import views

app_name = 'apiapp'

urlpatterns = [
    path('phone/', views.PhoneApiView.as_view(), name='phone_search'),
]
