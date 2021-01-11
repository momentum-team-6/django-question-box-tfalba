from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Count
from django.urls import reverse


class User(AbstractUser):
    pass

    

class Label(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'

class Question(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField('Label', related_name='questions', help_text='Select any tags for this question.')
    is_favorite = models.BooleanField(default=False)
    #has_correct_answer = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    is_closed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['title', '-created_at']
    
    def __str__(self):
        return f'{self.title}'


class Favorite(models.Model):
    question_is_favorite = models.BooleanField(default=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='favorite')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return f'{self.user} {self.question} {self.question_is_favorite}'


class Answer(models.Model):
    text = models.TextField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    is_correct = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f'{self.text}'

