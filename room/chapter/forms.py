from django.contrib.auth.forms import UserCreationForm
from django.forms  import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *

#class UserCreationForm(UserCreationForm):
 #   class Meta :
  #      model= User
   #     fields = ['username','email','password1','password2']
class StudentForm(ModelForm):
    class Meta:
        model= Students
        fields = '__all__'

class TechersForm(ModelForm):
    class Meta:
        model= Techers
        fields = '__all__'


