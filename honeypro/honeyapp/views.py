from django.shortcuts import render

def landing_page(request):
    return render(request, 'index.html')

def oil_page(request):
    return render(request, 'oil.html')

def spices_page(request):
    return render(request, 'spices.html')
