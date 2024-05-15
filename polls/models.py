from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.question_text
    
    def is_popular(self):
        if self.likes >= 3:
            return True
        else:
            return False

class Awnser(models.Model):
    awnser_text = models.CharField(max_length=200)
    date = models.DateField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.awnser_text
    
    def is_popular(self):
        if self.likes >= 3:
            return True
        else:
            return False