from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import loader

from polls.models import Question

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-date')

    context = {
        'questions': questions
    }

    return render (request, 'index.html', context)


def detail(request, question_id):
    return HttpResponse("This is a question number: " + str(question_id))