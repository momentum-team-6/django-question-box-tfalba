from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.http import JsonResponse
from .models import Question, Label, Answer, Favorite
from .forms import QuestionForm, AnswerForm, SearchForm
import requests


  # Iterate over user_favorite and find where user_favorite[].question is equal to question in outer loop
  
@login_required
def index(request):
  labels = Label.objects.all()
  favorites = Favorite.objects.all()
  form = SearchForm()
  user_favorites = Favorite.objects.filter(user=request.user)
  num_favorite = Count('favorites')
  question_base = Question.objects.all()

  
  if request.method == 'POST':
    form = SearchForm(data=request.POST)
    if form.is_valid():
      my_search_term = form.cleaned_data['search_term']
      questions = question_base.filter(body__icontains=my_search_term)
  elif request.GET.get('labels'):
    select_label = request.GET.get('labels')
    if select_label == 'All':
      questions = question_base
    elif select_label == 'Open':
      questions = question_base.filter(is_closed='False')
    elif select_label == 'Closed':
      questions = question_base.filter(is_closed='True')
    else:
      questions = question_base.filter(labels__name=select_label)
  else:
    form = SearchForm()
    questions = question_base
  
  faves = questions.annotate(num_favorite=num_favorite)
  return render(request, 'questions/index.html', {"questions": questions, "labels": labels, "favorites": favorites, "faves": faves, "form": form, "user_favorites": user_favorites})

@login_required
def user_home(request):
  labels = Label.objects.all()
  favorites = Favorite.objects.all()
  form = SearchForm()
  user_favorites = Favorite.objects.filter(user=request.user)
  num_favorite = Count('favorites')
  question_base = Question.objects.filter(user=request.user)
    
  if request.method == 'POST':
    form = SearchForm(data=request.POST)
    if form.is_valid():
      my_search_term = form.cleaned_data['search_term']
      questions = question_base.filter(body__icontains=my_search_term)
  elif request.GET.get('labels'):
    select_label = request.GET.get('labels')
    if select_label == 'All':
      questions = question_base
    elif select_label == 'Open':
      questions = question_base.filter(is_closed='False')
    elif select_label == 'Closed':
      questions = question_base.filter(is_closed='True')
    else:
      questions = question_base.filter(labels__name=select_label)
  else:
    form = SearchForm()
    questions = question_base

  #faves = questions.annotate(num_favorite=num_favorite)
  faves = questions.annotate(num_favorite=num_favorite)

  return render(request, 'questions/my_questions.html', {"questions": questions, "labels": labels, "favorites": favorites, "faves": faves, "form": form, "user_favorites": user_favorites})

@login_required
def user_q_a(request):
  labels = Label.objects.all()
  favorites = Favorite.objects.all()
  form = SearchForm()
  user_favorites = Favorite.objects.filter(user=request.user)
  num_favorite = Count('favorites')
  question_base = Question.objects.filter(user=request.user)
  
  if request.method == 'POST':
    form = SearchForm(data=request.POST)
    if form.is_valid():
      my_search_term = form.cleaned_data['search_term']
      questions = question_base.filter(body__icontains=my_search_term)
  elif request.GET.get('labels'):
    select_label = request.GET.get('labels')
    if select_label == 'All':
      questions = question_base
    elif select_label == 'Open':
      questions = question_base.filter(is_closed='False')
    elif select_label == 'Closed':
      questions = question_base.filter(is_closed='True')
    else:
      questions = question_base.filter(labels__name=select_label)
  else:
    form = SearchForm()
    questions = question_base
  
  faves = questions.annotate(num_favorite=num_favorite)

  return render(request, 'questions/my_q_a.html', {"questions": questions, "labels": labels, "favorites": favorites, "faves": faves, "form": form, "user_favorites": user_favorites})



def answer_detail(request):
  labels = Label.objects.all()
  favorites = Favorite.objects.all()
  form = SearchForm()
  user_favorites = Favorite.objects.filter(user=request.user)
  question_base = Question.objects.all()
  
  if request.method == 'POST':
    form = SearchForm(data=request.POST)
    if form.is_valid():
      my_search_term = form.cleaned_data['search_term']
      questions = question_base.filter(body__icontains=my_search_term)
  elif request.GET.get('labels'):
    select_label = request.GET.get('labels')
    if select_label == 'All':
      questions = question_base
    elif select_label == 'Open':
      questions = question_base.filter(is_closed='False')
    elif select_label == 'Closed':
      questions = question_base.filter(is_closed='True')
    else:
      questions = question_base.filter(labels__name=select_label)
  else:
    form = SearchForm()
    questions = question_base
  
  num_favorite = Count('favorites')
  faves = questions.annotate(num_favorite=num_favorite)

  return render(request, 'questions/answer_detail_view.html', {"questions": questions, "labels": labels, "favorites": favorites, "faves": faves, "form": form, "user_favorites": user_favorites})


def question_detail(request, pk):
  questions = get_object_or_404(Question, pk=pk)
  labels = Label.objects.filter(questions=questions)
  answers = Answer.objects.filter(question=questions)

  return render(request, "questions/question_detail.html", {"question": questions, "labels": labels, "answers": answers})

def add_question(request):
  if request.method == 'GET':
    form = QuestionForm()
  else:
    form = QuestionForm(data=request.POST)
    if form.is_valid():
      new_question = form.save(commit=False)
      new_question.user = request.user
      new_question.save()

      return redirect(to='home')
  return render(request, "questions/add_question.html", {"form": form })


def delete_question(request, pk):
  question = get_object_or_404(Question, pk=pk)
  if request.method == 'POST':
    question.delete()
    return redirect(to='home')
  return render(request, "questions/delete_question.html", {
    "question": question})

def delete_answer(request, pk):
  answer = get_object_or_404(Answer, pk=pk)
  if request.method == 'POST':
    answer.delete()
    # return redirect(to='home')
    return redirect(to='question_detail', pk=answer.question.pk)
  return render(request, "questions/delete_answer.html", {
    "answer": answer})

def mark_favorite(request, pk):
  question = get_object_or_404(Question, pk=pk)
  # if request.method == 'GET':
  #   new_favorite = Favorite(data=user, pk)
    # pass user from request.user and pk from question into a new instance of favorite
    # favorite will have a ForeignKey on question and a ForeignKey on User
  pass

def add_answer(request, pk):
  question = get_object_or_404(Question, pk=pk)
  labels = Label.objects.filter(questions=question)
  answers = Answer.objects.filter(question=question)
  if request.method == 'GET':
    form = AnswerForm()
  else:
    form = AnswerForm(data=request.POST)
    if form.is_valid():
      new_answer = form.save(commit=False)
      new_answer.question = question
      new_answer.user = request.user
      new_answer.save()
      return redirect(to='question_detail', pk=pk)
  return render(request, "questions/add_answer.html", {"question": question, "form": form, "answers": answers, "labels": labels})

def mark_closed(request, pk):
  question = get_object_or_404(Question, pk=pk)
  if not question.is_closed:
    question.is_closed = True
    question.save()
    data = {'change': 'closed'}
  else:
    question.is_closed = False
    question.save()
    data = {'change': 'open'}
  return JsonResponse(data)


def mark_correct(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if not answer.is_correct:
        answer.is_correct = True
        answer.save()
        data = {'change': 'correct'}
    else:
        answer.is_correct = False
        answer.save()
        data = {'change': 'not-correct'}
    return JsonResponse(data)