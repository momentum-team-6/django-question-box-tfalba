"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.index, name='home'),
    path('questions/answers', views.answer_detail, name='answer_detail'),
    path('questions/<int:pk>/', views.question_detail, name='question_detail'),
    path('questions/add', views.add_question, name='add_question'),
    path('questions/<int:pk>/answer', views.add_answer, name='add_answer'),
    path('questions/my_questions', views.user_home, name='my_questions'),
    path('questions/my_q_a', views.user_q_a, name='my_q_a'),
    path('questions/<int:pk>/delete/', views.delete_question, name='delete_question'),
    path('questions/<int:pk>/answer/delete', views.delete_answer, name='delete_answer'),
    path('questions/<int:pk>/answer/mark_correct', views.mark_correct, name='mark_correct'),
    path('questions/<int:pk>/mark_closed', views.mark_closed, name='mark_closed'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
