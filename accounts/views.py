from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from enquiries.models import Enquiry
from listings.models import Listing

def register(request):
    if request.method == 'POST':
        
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirm = request.POST['password-confirm']

        # Check if Passwords Match
        if password == passwordConfirm:
            # Check if Email Exists
            print(0)
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email address is already in use')
                print(1)
                return redirect('register')
            else:
                # Register User
                user = User.objects.create_user(
                    username = email,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    password = password
                )
                user.save()
                messages.success(request, 'Congratulations! You are now registered')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, 'Email and/or password did not match our records')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('index')
    
def dashboard(request):
    user = request.user

    if request.method == 'POST':
        
        # Retrieve Post Request Values
        listing_id = request.POST['listing-id']
        message = request.POST['new-message']

        # Add Enquiry to Database
        new_enquiry = Enquiry(
            listing_id = Listing.objects.get(pk=listing_id),
            user_id = user.id,
            user_group = 'customer',
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            message = message
        )
        new_enquiry.save()
        return redirect('/user/dashboard')

    enquiries = Enquiry.objects.filter(Q(user_id=user.id) | Q(response_to_user_id=user.id)).order_by('-listing_id', '-message_date')
    context = {
        'enquiries': enquiries
    }

    
    return render(request, 'accounts/dashboard.html', context)