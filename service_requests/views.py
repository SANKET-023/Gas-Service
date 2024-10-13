from django.shortcuts import render

# Create your views here.
# service_requests/views.py
from django.shortcuts import render, redirect
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
from .forms import CustomerCreationForm
from django.contrib.auth import login

@login_required
def submit_request(request):
    if request.method == 'POST':
        request_type = request.POST['request_type']
        description = request.POST['description']
        attachment = request.FILES.get('attachment')
        
        service_request = ServiceRequest.objects.create(
            customer=request.user.customer,
            request_type=request_type,
            description=description,
            attachment=attachment,
        )
        return redirect('track_request', request_id=service_request.id)
    
    return render(request, 'submit_request.html')

@login_required
def track_request(request, request_id):
    service_request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'track_request.html', {'service_request': service_request})

@login_required
def manage_requests(request):
    if request.user.is_staff:
        service_requests = ServiceRequest.objects.all()
        return render(request, 'manage_requests.html', {'service_requests': service_requests})
    else:
        return redirect('home')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('submit_request')  # Redirect to submit request after successful registration
    else:
        form = CustomerCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def submit_request(request):
    # You can use the submit_request logic already created here.
    pass