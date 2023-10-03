from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from accounts.models import CustomUser, UserAttributes
from .forms import LoginForm, RegistrationForm, UserAttributesForm
from django.contrib.auth.views import FormView, LoginView
from .models import Student, Lecturer, Aluminum, Partner
from lib.models import t_url


def admin_dashboard(request):
    labels = []
    data = []

    url = t_url.objects.all()

    queryset = Student.objects.all()  # order_by('-population')[:5]
    for stud in queryset:
        labels.append(stud.user.username)
        data.append(queryset.all().count())

    students = CustomUser.objects.filter(Q(user_type="student")).count()
    female_count = CustomUser.objects.filter(
        Q(gender="Female") & Q(user_type="student")
    ).count()
    male_count = CustomUser.objects.filter(
        Q(gender="Male") & Q(user_type="student")
    ).count()
    all_students = Student.objects.all()
    lecturer_count = CustomUser.objects.filter(Q(user_type="lecturer")).count()

    context = {
        "students": students,
        "female_count": female_count,
        "male_count": male_count,
        "all_students": all_students,
        "lecturer_count": lecturer_count,
        "labels": labels,
        "data": data,
        "url": url,
    }
    return render(request, "accounts/admin/dashboard.html", context)


def user_details(request, id):
    user = get_object_or_404(UserAttributes, rootID=id)

    if request.method == "POST":
        form = UserAttributesForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to the user's dashboard after successful form submission
            return HttpResponseRedirect(
                reverse("user-details", kwargs={"id": user.rootID})
            )

    else:
        form = UserAttributesForm(instance=user)

    context = {
        "photo": user.photo,
        "church_name": user.church_name,
        "phone": user.phone,
        "address": user.address,
        "city": user.city,
        "country": user.country,
        "form": form,
    }
    template = "accounts/users/dashboard.html"
    return render(request, template, context)


def student_dashboard(request, id):
    user = get_object_or_404(CustomUser, id=id)
    # student = get_object_or_404(Student, user_id=request.user.id)
    students = Student.objects.all().count()

    context = {
        "username": user.username,
        "students": students,
    }
    template = "accounts/students/dashboard.html"
    return render(request, template, context)


def lecturer_dashboard(request):
    students = Student.objects.all().count()

    context = {
        "students": students,
    }
    return render(request, "accounts/lecturers/dashboard.html", context)


# class CustomRegistrationView(FormView):
#     form_class = RegistrationForm
#     template_name = (
#         "accounts/register.html"  # Assuming this is your registration template
#     )
#     success_url = "/accounts/login/"  # Customize this URL

#     def form_valid(self, form):
#         # Create the user account
#         user = form.save()

#         # Determine user type and create corresponding profile
#         user_type = form.cleaned_data["user_type"]
#         if user_type == "student":
#             Student.objects.create(user=user)
#         elif user_type == "lecturer":
#             Lecturer.objects.create(user=user)
#         elif user_type == "alumni":
#             Aluminum.objects.create(user=user)
#         elif user_type == "donor":
#             Partner.objects.create(user=user)

#         return super().form_valid(form)


class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_authenticated:
            if user.user_type == "admin":
                return "/admin/dashboard/"  # Customize the URL for the admin dashboard
            elif user.user_type == "lecturer":
                return "/lecturer/dashboard/"  # Customize the URL for the lecturer dashboard
            elif user.user_type == "student":
                student_dashboard_url = reverse("user-details", kwargs={"id": user.id})
                return student_dashboard_url
            elif user.user_type == "alumni":
                return (
                    "/alumni/dashboard/"  # Customize the URL for the alumni dashboard
                )

        return "/"


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_authenticated:
                if user.user_type == "student":
                    student_dashboard_url = reverse(
                        "user-details", kwargs={"id": user.id}
                    )
                    return redirect(student_dashboard_url)
                elif user.user_type == "lecturer":
                    return redirect("/lecturer-dashboard")
                elif user.user_type == "admin":
                    return redirect("/admin-dashboard")
                elif user.user_type == "alumni":
                    return redirect("/alumni-dashboard")
    else:
        form = LoginForm(request)
    return render(request, "accounts/login.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")  # Redirect to your home page
    else:
        form = RegistrationForm()
    return render(request, "accounts/registration.html", {"form": form})


def Logout(request):
    logout(request)
    return redirect("/")
