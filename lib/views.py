from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from accounts.models import Student


@login_required(login_url="coresms/login/")
def home(request):
    student = get_object_or_404(Student, root=request.user.id)
    context = {
        "student_id": student.student_id,
    }
    template = "lib/home.html"

    return render(request, template, context)
