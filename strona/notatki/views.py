from django.shortcuts import render, get_object_or_404
from .models import Note
from django.http import Http404
# Create your views here.
def note_list(request):
 notes = Note.published.all()
 return render(request,
 'notatki/note/list.html',
 {'notes': notes})
def note_detail(request, slug):
    note = get_object_or_404(Note,
                             slug=slug,
                             status=Note.Status.PUBLISHED)
    return render(request,
 'notatki/note/detail.html',
 {'note': note})