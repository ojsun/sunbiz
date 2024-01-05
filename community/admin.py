from django.contrib import admin
from .models import Question,Answer,Comment

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields=['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, QuestionAdmin)
admin.site.register(Comment, QuestionAdmin)