import re
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import * 
from datetime import datetime
from .filter import *
from django.db.models import Sum  # قم باستيراد Sum هنا

# Students Def.


def studentes (request):
 
 students =Students.objects.all()

 myFilter = StudentsFilter(request.GET , queryset=students)
 students = myFilter.qs

 content={
  'students':students,
  'myFilter':myFilter,
 }

 return render(request,'studentes.html',content)

 
def add_students(request):
    form = StudentForm()  

    if request.method == "POST":
        form = StudentForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('studentes')
        else:
            print(form.errors)  

    content = {'form': form}
    return render(request, 'add_students.html', content)

def update_students(request,pk):

    student = Students.objects.get(id=pk)
    form =StudentForm(instance=student)
    if request.method == "POST":
        form =StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentes')
    content={
        'form':form,
    }

    return render(request, 'update_students.html',content)


def delete_students(request,pk):

    student=Students.objects.get(id=pk)


    if request.method == "POST":
        student.delete()
        return redirect('studentes')

  


    return render(request, 'delete_students.html')




# Techer Def .



def techeres (request):

       techeres=Techers.objects.all()
       myFilter = TechersFilter(request.GET , queryset=techeres)
       techeres = myFilter.qs
       content={
         'techeres':techeres,
         'myFilter':myFilter,
          }
       return render(request, 'techeres.html',content)


def add_techeres(request):
   

    form = TechersForm()  

    if request.method == "POST":
          form = TechersForm(request.POST)  
          if form.is_valid():
              form.save()
              return redirect('techeres')
    content={
       'form':form
    }
    return render(request,'add_techeres.html',content )



def delete(request ,pk):
    techeres = Techers.objects.get(id=pk)
    if request.method == "POST" :
       techeres.delete()
       return redirect('techeres')
    return render (request , 'delete.html'  )


def update_techers(request,pk):
   
    techeres = Techers.objects.get(id=pk)
    form = TechersForm(instance=techeres)

    if request.method == "POST":
        form = TechersForm(request.POST, instance=techeres) 
        if form.is_valid():
            form.save()
            return redirect('techeres')

    content = {
        'form': form
    }

    return render(request, 'update_techers.html',content)



# Statistics

def statistics(request):
    studentes=Students.objects.all()  
    total_studentes =studentes.count()
    total_amount = Students.objects.aggregate(Sum('amount'))['amount__sum'] or 0



    techeres=Techers.objects.all()
    total_techeres =techeres.count()
    total_salary = Techers.objects.aggregate(Sum('salary'))['salary__sum'] or 0


    total_net_profit=total_amount-total_salary


    #paid_studenntes=S

    content={
        'total_studentes':total_studentes,
        'total_techeres':total_techeres,
        'total_amount':total_amount,
        'total_salary':total_salary,
        'total_net_profit':total_net_profit
        


    }
    



    return render(request,  'statistics.html',content)

    



# log and reg
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('studentes')  # Change 'studentes' to your desired redirect URL or view name
        else:
            messages.error(request, 'Username or Password is incorrect.')

    return render(request, 'login.html')


def register (request):
    form = UserCreationForm()
    content={
        'form':form
       }
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
           form.save()

    return render(request,  'register.html',content)

def logout_page(request):
    logout(request)
    return redirect('login')



def aboute(request):


    return render(request,  'aboute.html')
