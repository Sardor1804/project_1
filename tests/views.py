from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def math_easy(request):
    return render(request, 'tests/math_easy.html')

@login_required
def math_normal(request):
    return render(request, 'tests/math_normal.html')

@login_required
def math_hard(request):
    return render(request, 'tests/math_hard.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def physics_easy(request):
    return render(request, 'tests/physics_easy.html')

@login_required
def physics_normal(request):
    return render(request, 'tests/physics_normal.html')

@login_required
def physics_hard(request):
    return render(request, 'tests/physics_hard.html')


@login_required
def informatics_easy(request):
    return render(request, 'tests/informatics_easy.html')

@login_required
def informatics_normal(request):
    return render(request, 'tests/informatics_normal.html')

@login_required
def informatics_hard(request):
    return render(request, 'tests/informatics_hard.html')