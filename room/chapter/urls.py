from django.urls import path  ,re_path
from . import views


urlpatterns = [

# Studentes 
path('',views.studentes ,name="studentes"),
path('update_students/<str:pk>/',views.update_students,name="update_students"),
path('delete_students/<str:pk>/',views.delete_students,name="delete_students"),
path('add_students/',views.add_students ,name="add_students"),


#Techers
path('techeres/',views.techeres,name="techeres"),
path('delete/<str:pk>/',views.delete,name="delete"),
path('add_techeres/',views.add_techeres,name="add_techeres"),
path('update_techers/<str:pk>/',views.update_techers,name="update_techers"),

#Statistics
path('statistics/', views.statistics ,name="statistics"),


#login and register 


path('login/' ,views.login_page   ,name="login"),
path('register/' ,views.register ,name="register"),

path('logout/' ,views.logout_page ,name="logout"),



#aboute

path('aboute/' , views.aboute , name="aboute")

]