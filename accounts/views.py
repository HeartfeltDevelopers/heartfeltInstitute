from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.db import connection
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from accounts.models import CustomUser, UserAttributes
from .forms import LoginForm, RegistrationForm, UserAttributesForm
from django.contrib.auth.views import FormView, LoginView
from .models import Student, Lecturer, Aluminum, Partner
from lib.models import t_url


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def admin_dashboard(request):
    labels = []
    data = []

    url = t_url.objects.all()

    queryset = Student.objects.all()  # order_by('-population')[:5]
    for stud in queryset:
        labels.append(stud.user.username)
        data.append(queryset.all().count())

    students = CustomUser.objects.filter(Q(user_type="student")).count()
    female_count = UserAttributes.objects.filter(Q(gender="Female")).count()
    male_count = UserAttributes.objects.filter(Q(gender="Male")).count()
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
    students = connection.cursor()
    students.cursor.execute(
        """SELECT a.root, s.student_id, a.photo, u.first_name, u.last_name, s.current_year, s.major, a.gender, a.address, a.date_of_birth, a.phone, u.email
            FROM accounts_CustomUser u
            INNER JOIN accounts_UserAttributes a ON CAST(a.root AS INT) = u.id
            INNER JOIN accounts_Student s ON s.root = u.id
            WHERE u.user_type = 'student';
        """
    )

    students = dictfetchall(students)

    c = connection.cursor()
    c.cursor.execute(
        """Select a.gender, count(a.id) as total
                            FROM accounts_UserAttributes a
                            INNER JOIN accounts_Student s ON s.root = a.root
                            GROUP BY a.gender
                            """
    )

    c = dictfetchall(c)

    totalFemale = c[0]["total"] if c else 0
    totalMen = c[1]["total"] if c else 0
    total_students = totalFemale + totalMen

    context = {
        "students": students,
        "total_students": total_students,
        "totalFemale": totalFemale,
        "totalMen": totalMen,
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
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("registration-step-2")
    else:
        form = RegistrationForm()
    return render(request, "accounts/registration.html", {"form": form})


def registration2(request):
    if request.method == "POST":
        form = UserAttributesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("user-details", kwargs={"id": request.user.id})
            )
    else:
        form = UserAttributesForm()
    return render(request, "accounts/registration2.html", {"form": form})


def Logout(request):
    logout(request)
    return redirect("/")
