from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'POST' and request.FILES.get('document'):
        # Handling the file upload
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()

        # Save the uploaded file
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        # Return a JSON response to inform the frontend about the successful upload
        return JsonResponse({'message': 'File uploaded successfully!', 'file_url': file_url})

    return render(request, 'myapp/home.html')
