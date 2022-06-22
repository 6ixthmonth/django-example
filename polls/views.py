from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # hardcoding
    # output = "<br>".join([q.question_text for q in latest_question_list])
    # print(output)
    # return HttpResponse(output)
    
    # set template file
    context = {
        "latest_question_list": latest_question_list
    }
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    # render by shortcuts
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
