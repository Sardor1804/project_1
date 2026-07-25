import nested_admin
from django.contrib import admin
from .models import Course, Test, Question, Option


class OptionInline(nested_admin.NestedTabularInline):
    model = Option
    extra = 2


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    inlines = [OptionInline]


import nested_admin
from django.contrib import admin
from django.utils.html import format_html
from .models import Test, Course


# ================= TEST ADMIN =================
@admin.register(Test)
class TestAdmin(nested_admin.NestedModelAdmin):

    list_display = (
        'title',
        'created_by',
        'image_preview',   # 👈 qo‘shildi
    )

    search_fields = (
        'title',
    )

    inlines = [QuestionInline]

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" style="border-radius:8px;" />',
                obj.image.url
            )
        return "Rasm yo‘q"

    image_preview.short_description = "Preview"


# ================= COURSE =================
admin.site.register(Course)
