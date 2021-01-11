from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Question, Label, Answer, Favorite
#import Favorite

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Label)
admin.site.register(Favorite)


