
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "subjects"

urlpatterns = [

    # ================= SUBJECTS =================
    path("science/", views.science_view, name="science"),
    path("science-english/", views.science_english, name="science_english"),
    path("english/", views.home_english, name="home_english"),

    # ================= AI TEACHER =================
    path("ai-teacher/", views.ai_teacher, name="ai_teacher"),
    path("ai-teacher-english/", views.ai_teacher_english, name="ai_teacher_english"),

    # ================= MATH =================
    path("math/", views.math_level, name="math_level"),
    path("math/easy/", views.math_easy, name="math_easy"),
    path("math/normal/", views.math_normal, name="math_normal"),
    path("math/hard/", views.math_hard, name="math_hard"),

    # ================= MATH ENGLISH =================
    path("math/english/", views.math_level_english, name="math_level_english"),
    path("math/english/easy/", views.math_easy_english, name="math_easy_english"),
    path("math/english/normal/", views.math_normal_english, name="math_normal_english"),
    path("math/english/hard/", views.math_hard_english, name="math_hard_english"),

    # ================= PHYSICS =================
    path("physics/", views.physics_level, name="physics_level"),
    path("physics/easy/", views.physics_easy, name="physics_easy"),
    path("physics/normal/", views.physics_normal, name="physics_normal"),
    path("physics/hard/", views.physics_hard, name="physics_hard"),

    # ================= PHYSICS ENGLISH =================
    path("physics/english/", views.physics_level_english, name="physics_level_english"),
    path("physics/english/easy/", views.physics_easy_english, name="physics_easy_english"),
    path("physics/english/normal/", views.physics_normal_english, name="physics_normal_english"),
    path("physics/english/hard/", views.physics_hard_english, name="physics_hard_english"),

    # ================= INFORMATICS =================
    path("informatics/", views.informatics_level, name="informatics_level"),
    path("informatics/easy/", views.informatics_easy, name="informatics_easy"),
    path("informatics/normal/", views.informatics_normal, name="informatics_normal"),
    path("informatics/hard/", views.informatics_hard, name="informatics_hard"),

    # ================= INFORMATICS ENGLISH =================
    path("informatics/english/", views.informatics_level_english, name="informatics_level_english"),
    path("informatics/english/easy/", views.informatics_easy_english, name="informatics_easy_english"),
    path("informatics/english/normal/", views.informatics_normal_english, name="informatics_normal_english"),
    path("informatics/english/hard/", views.informatics_hard_english, name="informatics_hard_english"),

    # ================= KNOWLEDGE BATTLE =================
    path("knowledge-battle/", views.knowledge_battle_english, name="knowledge_battle_english"),
    path("bilimlar_janggi/", views.bilimlar_janggi, name="bilimlar_janggi"),
    path("bilimlar-janggi/", views.bilimlar_janggi_english, name="bilimlar_janggi_english"),

    # ================= RESULTS =================
    path("result/", views.result, name="result"),
    path("result-english/", views.result_english, name="result_english"),
    path("result-test/", views.result_test, name="result_test"),

    # ================= TEST =================
    path("test/<int:test_id>/submit/", views.quiz_submit, name="quiz_submit"),
    path("test/<int:pk>/", views.test_detail, name="test_detail"),

    # ================= AUTHENTICATION =================
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
]
