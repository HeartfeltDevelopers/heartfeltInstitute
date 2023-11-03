from django.shortcuts import render, redirect
from .forms import AssignmentForm

def assignment_form(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = AssignmentForm()
    return render(request, 'assignment-files/assignment_form.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')



