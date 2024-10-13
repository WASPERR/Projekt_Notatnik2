from django.shortcuts import render, get_object_or_404
from .models import Note
from django.http import Http404
# Create your views here.
def notes_list(request):
 notes = Note.published.all()
 return render(request,
 'notatki/note/list.html',
 {'notes': notes})
def notes_detail(request, id):
    note = get_object_or_404(Note,
                             id=id,
                             status=Note.Status.PUBLISHED)
    return render(request,
 'notatki/note/list.html',
 {'note': note})