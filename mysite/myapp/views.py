# myapp/views.py
from django.shortcuts import render
from .forms import TextForm

def home(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            return render(request, 'myapp/home.html', {'form': form, 'text': text})
    else:
        form = TextForm()

    return render(request, 'myapp/home.html', {'form': form})
