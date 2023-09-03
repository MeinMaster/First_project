from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описиние")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Торг ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField("изображение", upload_to="advertisements/")

    def get_absolute_url(self):
        return reverse('adv-detail', kwargs={'pk': self.pk})

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold; ">Сегодня в {}</span', created_time
            )
        return self.created_at.strftime("%d.%m.%Y")

    @admin.display(description='дата  обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: yellow; font-weight: bold; ">Сегодня в {}</span', updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y")

    @admin.display(description='фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;">', url=self.image.url
            )

    def __str__(self):
        return f"Advertisement(id={self.id}), title={self.title}, price={self.price}"

    class Meta:
        db_table = 'advertisements'
