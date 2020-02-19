from django import forms
from .models import Question

# class QuestionCreateForm(forms.ModelForm):
#     def get(self, request, *args, **kwargs)
#     class meta:
#         model = Question
#         fields = ['question_text']
#     pass