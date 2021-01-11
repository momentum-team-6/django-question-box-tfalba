from django import forms
from .models import Question, Label, Answer

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = [
      'title',
      'body',
      'labels',
    ]

    title = forms.CharField()
    body = forms.Textarea()

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = [
      'text'
    ]


class SearchForm(forms.Form):
  search_term = forms.CharField(label='Search Term', max_length=50, required=False)


