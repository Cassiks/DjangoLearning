from django.shortcuts import render

def Contact(request):
    return render(request, 'pages/contact.html')