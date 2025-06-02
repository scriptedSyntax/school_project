from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from core.models import School

User = get_user_model()


# ------------------------------
# User Registration View
# ------------------------------
def register_user(request):
    allowed_roles = ['superadmin', 'schooladmin', 'teacher', 'student']

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        school_id = request.POST.get('school_id')

        # Check role
        if not role or role not in allowed_roles:
            return render(request, 'registration/register.html', {
                'error': 'Invalid or missing role.',
                'schools': School.objects.all(),
                'allowed_roles': allowed_roles
            })

        # Check duplicate username
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/register.html', {
                'error': 'Username already exists.',
                'schools': School.objects.all(),
                'allowed_roles': allowed_roles
            })

        try:
            # School is optional for superadmin
            school = None
            if role != 'superadmin':
                school = School.objects.get(id=school_id)

            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role=role,
                school=school
            )

            return render(request, 'registration/register.html', {
                'success': 'User created successfully.',
                'schools': School.objects.all(),
                'allowed_roles': allowed_roles
            })

        except School.DoesNotExist:
            return render(request, 'registration/register.html', {
                'error': 'Invalid school selected.',
                'schools': School.objects.all(),
                'allowed_roles': allowed_roles
            })

    # GET request
    return render(request, 'registration/register.html', {
        'schools': School.objects.all(),
        'allowed_roles': allowed_roles
    })


# ------------------------------
# Login View (Role-Based Redirect)
# ------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if not hasattr(user, 'role') or user.role not in ['superadmin', 'schooladmin', 'teacher', 'student']:
                print("Invalid role on login:", user.role)
                return render(request, 'dashboards/unauthorized.html', {
                    'error': f'Invalid role: {user.role}'
                })

            login(request, user)
            print("Login success:", user.username, "Role:", user.role)

            if user.role == 'superadmin':
                return redirect('superadmin_dashboard')
            elif user.role == 'schooladmin':
                return redirect('schooladmin_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'student':
                return redirect('student_dashboard')
        else:
            return render(request, 'registration/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'registration/login.html')


# ------------------------------
# Dashboard Role Redirect View
# ------------------------------
@login_required
def dashboard_redirect(request):
    role = getattr(request.user, 'role', None)

    if role == 'superadmin':
        return redirect('superadmin_dashboard')
    elif role == 'schooladmin':
        return redirect('schooladmin_dashboard')
    elif role == 'teacher':
        return redirect('teacher_dashboard')
    elif role == 'student':
        return redirect('student_dashboard')
    else:
        print("Invalid dashboard redirect role:", role)
        return render(request, 'dashboards/unauthorized.html', {
            'error': f'Invalid user role: {role}'
        })


# ------------------------------
# Dashboard Views for Each Role
# ------------------------------
@login_required
def superadmin_dashboard(request):
    return render(request, 'dashboards/superadmin.html')


@login_required
def schooladmin_dashboard(request):
    return render(request, 'dashboards/schooladmin.html')


@login_required
def teacher_dashboard(request):
    return render(request, 'dashboards/teacher.html')


@login_required
def student_dashboard(request):
    return render(request, 'dashboards/student.html')


# ------------------------------
# Public Welcome Page
# ------------------------------
def welcome_view(request):
    return render(request, 'core/welcome.html')


# ------------------------------
# Logout View (POST only)
# ------------------------------
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

@require_POST
def logout_view(request):
    logout(request)
    return redirect('welcome')
