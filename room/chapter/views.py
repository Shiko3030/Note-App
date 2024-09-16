from django.shortcuts import render,redirect
from .forms import * 
from .filter import NoteFilter

# Create your views here.


def add_note (request):
    form = NoteForm()
  
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/')

    context ={
        'form':form
    }
    return render( request , 'add_note.html' ,context)




def home(request ):
    notes =Note.objects.all()

    searsh = NoteFilter(request.GET , queryset=notes )
    notes=searsh.qs

    

    context={
        'searsh':searsh,
        'notes':notes

    }
    return render(request , 'home.html',context)



def edit (request , pk):
    note = Note.objects.get(id=pk)
    form =NoteForm(instance=note)#يعني البيانات تبقي ظاهرة في ال فورم
    if request.method == "POST":
        form =NoteForm(request.POST ,instance=note)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={
        'form':form
    }

    return render(request , 'edit.html' ,context)


def delete (request ,pk):
   note=Note.objects.get(id=pk)

   if request.method == "POST":
       note.delete()
       return redirect('/')


   return render(request ,'delete.html' )
      


    

    


    




