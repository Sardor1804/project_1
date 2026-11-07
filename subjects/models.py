from django.db import models
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tests/', null=True, blank=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    LEVEL_CHOICES = (
        ('easy', 'Easy'),
        ('normal', 'Normal'),
        ('hard', 'Hard'),
    )

    title  = models.CharField(max_length=255)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='easy'
    )
    image      = models.ImageField(upload_to='tests/', null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    text = models.TextField()

    def __str__(self):
        return self.text


class Option(models.Model):
    question   = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='options'
    )
    text       = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    """Foydalanuvchilar tomonidan qoldirilgan otzivlar (fan + daraja bo'yicha)."""

    DARAJA_CHOICES = [
        ("oson", "Oson"),
        ("ortacha", "O'rtacha"),
        ("qiyin", "Qiyin"),
    ]

    TAVSIYA_CHOICES = [
        ("ha", "Ha"),
        ("balki", "Balki"),
        ("yoq", "Yo'q"),
    ]

    fan = models.CharField("Fan nomi", max_length=100)
    daraja = models.CharField("Daraja", max_length=20, choices=DARAJA_CHOICES)

    ism = models.CharField("Ism", max_length=150)
    lavozim = models.CharField("Lavozim / kompaniya", max_length=150, blank=True)

    baho = models.PositiveSmallIntegerField(
        "Baho", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    kuchli_tomonlar = models.TextField("Kuchli tomonlar", blank=True)
    kamchiliklar = models.TextField("Kamchiliklar", blank=True)
    izoh = models.TextField("Qo'shimcha fikr", blank=True)

    tavsiya = models.CharField(
        "Tavsiya qiladimi", max_length=10, choices=TAVSIYA_CHOICES, blank=True
    )

    foydalanuvchi = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="otzivlar",
        verbose_name="Foydalanuvchi",
    )

    yaratilgan_vaqt = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)

    class Meta:
        verbose_name = "Otziv"
        verbose_name_plural = "Otzivlar"
        ordering = ["-yaratilgan_vaqt"]

    def __str__(self):
        return f"{self.ism} — {self.fan} ({self.get_daraja_display()}) {self.baho}/5"

    @property
    def yulduzlar(self) -> str:
        return "⭐" * self.baho