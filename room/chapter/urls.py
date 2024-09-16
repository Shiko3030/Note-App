from django.urls import path
from . import views


urlpatterns = [
    
path('',views.home,name=''),
path('add_note/',views.add_note,name='add_note'),
path('edit/<str:pk>/',views.edit,name='edit'),
path('delete/<str:pk>/',views.delete,name='delete'),

]
