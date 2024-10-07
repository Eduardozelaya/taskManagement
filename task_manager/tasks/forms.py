from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'is_completed']

    # Customizando o widget para o campo due_date
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=False,  # Você pode mudar para True se for obrigatório
        input_formats=['%Y-%m-%dT%H:%M'],  # Formato esperado para datetime-local
    )

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if not due_date:
            raise forms.ValidationError("A data e hora de conclusão são obrigatórias.")
        return due_date
