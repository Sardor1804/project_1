from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Test, Option
from accounts.models import TestResult


def bilimlar_janggi_english(request):
    return render(request, "bilimlar_janggi_english.html")


# ================= HOME =================
def home_english(request):
    tests = Test.objects.all()
    return render(request, 'home_english.html', {'tests': tests})


# ================= SCIENCE =================
def science_view(request):
    tests = Test.objects.all()
    return render(request, "science.html", {"tests": tests})

def science_english(request):
    tests = Test.objects.all()
    return render(request, "science_english.html", {"tests": tests})


# ================= MATH =================
def math_level(request):
    return render(request, "math_level.html")

def math_easy(request):
    tests = Test.objects.all()
    return render(request, 'math_easy.html', {'tests': tests})

def math_normal(request):
    tests = Test.objects.all()
    return render(request, 'math_normal.html', {'tests': tests})

def math_hard(request):
    tests = Test.objects.all()
    return render(request, 'math_hard.html', {'tests': tests})


# ================= MATH ENGLISH =================
def math_level_english(request):
    return render(request, 'math_level_english.html')

def math_easy_english(request):
    tests = Test.objects.all()
    return render(request, 'math_easy_english.html', {'tests': tests})

def math_normal_english(request):
    tests = Test.objects.all()
    return render(request, 'math_normal_english.html', {'tests': tests})

def math_hard_english(request):
    tests = Test.objects.all()
    return render(request, 'math_hard_english.html', {'tests': tests})


# ================= PHYSICS =================
def physics_level(request):
    return render(request, "physics_level.html")

def physics_easy(request):
    tests = Test.objects.all()
    return render(request, 'physics_easy.html', {'tests': tests})

def physics_normal(request):
    tests = Test.objects.all()
    return render(request, 'physics_normal.html', {'tests': tests})

def physics_hard(request):
    tests = Test.objects.all()
    return render(request, 'physics_hard.html', {'tests': tests})


# ================= PHYSICS ENGLISH =================
def physics_level_english(request):
    return render(request, 'physics_level_english.html')

def physics_easy_english(request):
    tests = Test.objects.all()
    return render(request, 'physics_easy_english.html', {'tests': tests})

def physics_normal_english(request):
    tests = Test.objects.all()
    return render(request, 'physics_normal_english.html', {'tests': tests})

def physics_hard_english(request):
    tests = Test.objects.all()
    return render(request, 'physics_hard_english.html', {'tests': tests})


# ================= INFORMATICS =================
def informatics_level(request):
    return render(request, "informatics_level.html")

def informatics_easy(request):
    tests = Test.objects.all()
    return render(request, 'informatics_easy.html', {'tests': tests})

def informatics_normal(request):
    tests = Test.objects.all()
    return render(request, 'informatics_normal.html', {'tests': tests})

def informatics_hard(request):
    tests = Test.objects.all()
    return render(request, 'informatics_hard.html', {'tests': tests})


# ================= INFORMATICS ENGLISH =================
def informatics_level_english(request):
    return render(request, 'informatics_level_english.html')

def informatics_easy_english(request):
    tests = Test.objects.all()
    return render(request, 'informatics_easy_english.html', {'tests': tests})

def informatics_normal_english(request):
    tests = Test.objects.all()
    return render(request, 'informatics_normal_english.html', {'tests': tests})

def informatics_hard_english(request):
    tests = Test.objects.all()
    return render(request, 'informatics_hard_english.html', {'tests': tests})


# ================= RESULT =================
def result(request):
    score = request.session.get('score', 0)
    total = request.session.get('total', 0)
    return render(request, 'accounts/result.html', {'score': score, 'total': total})

def result_english(request):
    score = request.session.get('score', 0)
    total = request.session.get('total', 0)
    return render(request, 'accounts/result_english.html', {'score': score, 'total': total})


# ================= KNOWLEDGE BATTLE =================
def knowledge_battle_english(request):
    return render(request, 'bilimlar_janggi_english.html')

def bilimlar_janggi(request):
    return render(request, 'accounts/bilimlar_janggi.html')


# ================= TEST DETAIL =================
def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()

    if request.method == "POST":
        score = 0
        total = questions.count()

        for question in questions:
            selected_id = request.POST.get(f"question_{question.id}")
            if selected_id:
                option = Option.objects.filter(id=selected_id).first()
                if option and option.is_correct:
                    score += 1

        request.session['score'] = score
        request.session['total'] = total
        return redirect('subjects:result_test')

    return render(request, 'test_detail.html', {
        'test': test,
        'questions': questions
    })


# ================= RESULT TEST =================
def result_test(request):
    score = request.session.get('score', 0)
    total = request.session.get('total', 0)
    return render(request, 'accounts/result_test.html', {'score': score, 'total': total})


# ================= QUIZ SUBMIT =================
@login_required
def quiz_submit(request, test_id):
    test      = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()

    if request.method == 'POST':
        correct = 0
        total   = questions.count()

        for question in questions:
            selected_id = request.POST.get(f'question_{question.id}')
            if selected_id:
                try:
                    option = question.options.get(id=selected_id)
                    if option.is_correct:
                        correct += 1
                except Exception:
                    pass

        score     = round((correct / total) * 5, 1) if total > 0 else 0
        stars_map = {5: '⭐⭐⭐⭐⭐', 4: '⭐⭐⭐⭐', 3: '⭐⭐⭐', 2: '⭐⭐', 1: '⭐', 0: '—'}
        stars     = stars_map.get(round(score), '⭐')

        TestResult.objects.create(
            user          = request.user,
            subject       = test.title,
            level         = test.level,
            score         = score,
            stars         = stars,
            finish_reason = request.POST.get('finish_reason', 'manual'),
            time_spent    = int(request.POST.get('time_spent', 0) or 0),
        )

        return redirect('profile')

    return render(request, 'quiz.html', {
        'test':      test,
        'questions': questions,
    })



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def ai_teacher(request):
    return render(request, "ai_teacher.html")