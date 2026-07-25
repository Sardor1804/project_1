from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Result, TestResult
from .forms import CustomUserCreationForm
from subjects.models import Course


def home(request):
    return render(request, 'home.html')


def home_english(request):
    return render(request, 'home_english.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        role = request.POST.get('role')
        if form.is_valid():
            user = form.save(commit=False)
            user.role = role if role else 'student'
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Login yoki parol xato'})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    results     = TestResult.objects.filter(user=request.user).order_by('-created_at')
    total_tests = results.count()
    total_score = sum(r.score for r in results)
    avg         = total_score / total_tests if total_tests > 0 else 0

    stars_map = {5: '⭐⭐⭐⭐⭐', 4: '⭐⭐⭐⭐', 3: '⭐⭐⭐', 2: '⭐⭐', 1: '⭐', 0: '—'}

    return render(request, 'accounts/profile.html', {
        'results':     results,
        'total_score': round(total_score, 1),
        'total_tests': total_tests,
        'avg_stars':   stars_map.get(round(avg), '—'),
    })


@login_required
def profile_english_view(request):
    results     = TestResult.objects.filter(user=request.user).order_by('-created_at')
    total_tests = results.count()
    total_score = sum(r.score for r in results)
    avg         = total_score / total_tests if total_tests else 0

    stars_map = {5: '⭐⭐⭐⭐⭐', 4: '⭐⭐⭐⭐', 3: '⭐⭐⭐', 2: '⭐⭐', 1: '⭐', 0: '—'}

    return render(request, 'accounts/profile_english.html', {
        'results':     results,
        'total_score': round(total_score, 1),
        'total_tests': total_tests,
        'avg_stars':   stars_map.get(round(avg), '—'),
    })


def add_course(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.role != 'teacher':
        return redirect('home')
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        description = request.POST.get("description")
        if not course_name:
            return JsonResponse({"success": False, "error": "Kurs nomi bo'sh bo'lmasligi kerak!"})
        Course.objects.create(
            name=course_name,
            description=description,
            teacher=request.user
        )
        return JsonResponse({"success": True})
    return render(request, 'accounts/add_course.html')


def science_view(request):
    course = get_object_or_404(Course, title="science")
    questions = course.questions.all()
    return render(request, "subjects/science.html", {
        "course": course,
        "questions": questions,
    })


@login_required
def finish_test(request):
    if request.method == 'POST':
        score    = int(request.POST.get('score', 0))
        subject  = request.POST.get('subject', 'Noma\'lum')
        level    = request.POST.get('level', 'Asosiy')
        time_spent = int(request.POST.get('time_spent', 0) or 0)
        finish_reason = request.POST.get('finish_reason', 'manual')

        stars_map = {5:'⭐⭐⭐⭐⭐', 4:'⭐⭐⭐⭐', 3:'⭐⭐⭐', 2:'⭐⭐', 1:'⭐', 0:'—'}

        TestResult.objects.create(
            user          = request.user,
            subject       = subject,
            level         = level,
            score         = float(score),
            stars         = stars_map.get(score, '⭐'),
            finish_reason = finish_reason,
            time_spent    = time_spent,
        )

        Result.objects.create(
            user    = request.user,
            subject = subject,
            level   = level,
            score   = score,
        )

        return redirect('profile')
    return redirect('home')