from django.shortcuts import redirect, render
from .models import Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'notes/home.html')

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'notes/note_list.html', {
        'notes': notes
    })


@login_required
def create_note(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Note.objects.create(
            user=request.user,
            title=title,
            content=content
        )

        return redirect('note_list')

    return render(request, 'notes/create_note.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {
        'form': form
    })

class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'