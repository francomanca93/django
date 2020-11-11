""" Users views"""

# Django
# Vamos hacer uso de render y redirect

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Exceptions
# Importamos posible error al tratar de crear
# una instancia con valor único que ya existe
from django.db.utils import IntegrityError

# Models
# Importamos los modelos de las instancias que crearemos
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm

# Create your views here.


@login_required
def update_profile(request):
    """ Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    """ Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request,
                          'users/login.html',
                          {'error': 'Invalid username and pasword'})
    return render(request, 'users/login.html')


def signup(request):
    """ Sign up view."""
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        # PASSWORD VALIDATION
        if passwd != passwd_confirmation:
            error = 'The passwords do not match.'
            return render(request, 'users/signup.html', {'error': error})

        # EMAIL VALIDATION
        email_validation = User.objects.filter(email=email)
        if email_validation:
            error = f'There is another account using {email}'
            return render(request, 'users/signup.html', {'error': error})

        # USERNAME VALIDATION
        try:
            user = User.objects.create_user(username=username, password=passwd)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = email
            user.save()
        except IntegrityError:
            return render(request, 'users/signup.html',
                          {'error': 'Username is already exist'})

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """ Logout a user."""
    logout(request)
    return redirect('login')
