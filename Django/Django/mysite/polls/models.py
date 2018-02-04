from django.db import models
import datetime
from django.utils import timezone
# Create your models here

 ##creat data base

class Question(models.Model):
   
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
##used to return string when view object
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

##foreign key one to many
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
