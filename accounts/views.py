from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.views import FormView, LoginView
from .models import Student, Lecturer, Aluminum, Partner


def admin_dashboard(request):
    labels = []
    data = []

    queryset = Student.objects.all()  # order_by('-population')[:5]
    for stud in queryset:
        labels.append(stud.user.username)
        data.append(queryset.all().count())

    students = Student.objects.all().count()
    all_students = Student.objects.all()
    partners_count = Partner.objects.all().count()

    context = {
        "students": students,
        "all_students": all_students,
        "partners_count": partners_count,
        'labels': labels,
        'data': data,
    }
    return render(request, 'accounts/admin/dashboard.html', context)


def student_dashboard(request):
    students = Student.objects.all().count()

    context = {
        "students": students,
    }
    return render(request, 'accounts/students/dashboard.html', context)


def lecturer_dashboard(request):
    students = Student.objects.all().count()

    context = {
        "students": students,
    }
    return render(request, 'accounts/lecturers/dashboard.html', context)


class CustomRegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'  # Assuming this is your registration template
    success_url = 'accounts/login/'  # Customize this URL

    def form_valid(self, form):
        # Create the user account
        user = form.save()

        # Determine user type and create corresponding profile
        user_type = form.cleaned_data['user_type']
        if user_type == 'student':
            Student.objects.create(user=user)
        elif user_type == 'lecturer':
            Lecturer.objects.create(user=user)
        elif user_type == 'alumni':
            Aluminum.objects.create(user=user)
        elif user_type == 'donor':
            Partner.objects.create(user=user)

        return super().form_valid(form)


#
# class CustomLoginView(LoginView):
#     def get_success_url(self):
#         user = self.request.user
#
#         if user.is_authenticated:
#             if user.user_type == 'admin':
#                 return '/admin/dashboard/'  # Customize the URL for the admin dashboard
#             elif user.user_type == 'lecturer':
#                 return '/lecturer/dashboard/'  # Customize the URL for the lecturer dashboard
#             elif user.user_type == 'student':
#                 return '/student/dashboard/'  # Customize the URL for the student dashboard
#             elif user.user_type == 'alumni':
#                 return '/alumni/dashboard/'  # Customize the URL for the alumni dashboard
#
#         return '/'


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/student-dashboard')  # Redirect to your home page
    else:
        form = LoginForm(request)
    return render(request, 'accounts/login.html', {'form': form})

#
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')  # Redirect to your home page
#     else:
#         form = RegistrationForm()
#     return render(request, 'accounts/register.html', {'form': form})
