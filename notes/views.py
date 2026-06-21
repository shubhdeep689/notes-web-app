from django.shortcuts import redirect, render
from .models import Note

# Create your views here.
def home(request):
    return render(request, 'notes/home.html')


def note_list(request):
    notes = Note.objects.all().order_by('-created_at')

    return render(request, 'notes/note_list.html', {
        'notes': notes
    })


def create_note(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.create(
            title=title,
            content=content
        )

        return redirect('note_list')

    return render(request, 'notes/create_note.html')