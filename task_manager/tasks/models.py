from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associa a tarefa ao usuário

    def __str__(self):
        return self.title

    def clean(self):
        # Verificar se o due_date é maior ou igual ao created_at
        if self.due_date and self.due_date < timezone.now():
            raise ValidationError('A data de vencimento não pode ser anterior ao momento atual.')
