from django.urls import path

from mobilephones import views

app_name = 'mobilephones'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('brands/', views.brandsView, name='brands'),
    path('phones/', views.phonesView, name='phones'),
    path('add-brand/', views.addBrandView, name='add-brand'),
    path('edit-brand/<id>/', views.editBrandView, name='edit-brand'),
    path('delete-brand/<id>/', views.deleteBrandView, name='delete-brand'),
    path('add-phone/', views.addPhoneView, name='add-phone'),
    path('edit-phone/<id>/', views.editPhoneView, name='edit-phone'),
    path('delete-phone/<id>/', views.deletePhoneView, name='delete-phone'),
]
