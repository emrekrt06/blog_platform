# flake8: noqa
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

# Create your views here.


def signup_view(request):
    """Handles user registration.
    Processes the SignUpForm to create a new user account.
    If the form is valid, it saves the user with a securely
    hashed password and redirects to the login page.

    Parameters:
        request (HttpRequest): The HTTP request object
        containing form data.
    Returns:
        HttpResponse: Renders the signup page with a form on
        GET requests, or redirects to the login page on
        successful registration.
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    """Handles user authentication and login.
    Authenticates the user based on the provided username
    and password.
    If the credentials are valid, logs the user in and
    redirects to the post list page.
    If authentication fails, returns the login page with an
    error message.

    Parameters:
        request (HttpRequest): The HTTP request object
        containing username and password.
    Returns:
        HttpResponse: Renders the login page or redirects to
        the post list on success.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("post_list")
        return render(
            request, "users/login.html", {"error": "Invalid username or password."}
        )
    return render(request, "users/login.html")


def logout_view(request):
    """Logs out the current user.
    Ends the user's session and redirects them to the
    post list page.

    Parameters:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponseRedirect: Redirects to the post list
        page after logout.
    """
    logout(request)
    return render(request, "users/logout.html")
