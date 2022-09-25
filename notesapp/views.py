from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def get_notes(request):
    notes = Note.objects.all()
    
    context = {"notes":notes}
    return render(request, 'notes.html', context)
    # return HttpResponse('Welcome')

def create_note(request):
    
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {"form":form}
    return render(request, 'note.html', context)


def update_note(request, pk):
    note = Note.objects.get(pk=pk)
    
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(instance=note, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {"form":form}
    return render(request, 'note.html', context)
    # return HttpResponse('Welcome')


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    
    if request.method == "POST":
        # form.save()
        note.delete()
        return redirect('/')


    context = {"note":note}
    return render(request, 'delete.html', context)
    # return HttpResponse('Welcome')