from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        return redirect('details_page')

    return render(request, 'login.html')

def registration(request):
    if request.method == 'POST':
        return redirect('login')

    return render(request, 'registration.html')

def details_page(request):
    if request.method == 'POST':
       return redirect('submission_success')

    return render(request, 'details_page.html')

def submission_success(request):
   return render(request, 'submission_success.html')
