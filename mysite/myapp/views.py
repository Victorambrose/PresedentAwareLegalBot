# myapp/views.py
from django.shortcuts import render
from .forms import TextForm
from textblob import TextBlob

def rephrase_text(text):
    blob = TextBlob(text)
    return blob.correct()  

def home(request):
    text = ""
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            rephrased_text = str(rephrase_text(text))
            return render(request, 'myapp/home.html', {'form': form, 'text': rephrased_text})
    else:
        form = TextForm()

    return render(request, 'myapp/home.html', {'form': form, 'text': text})
