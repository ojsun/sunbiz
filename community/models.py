from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=200)
    content=models.TextField()
    image_file=models.ImageField(max_length=100,blank=True, null=True)
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True,blank=True)
    class Meta:
        managed = False
        db_table = 'community_question'

class Answer(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True,blank=True)
    class Meta:
        managed = False
        db_table = 'community_answer'


class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True,blank=True)
    question=models.ForeignKey(Question, null=True,blank=True, on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer, null=True,blank=True, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'community_comment'


