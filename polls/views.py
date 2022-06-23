from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    from mysite.settings import BASE_DIR
    print(BASE_DIR)
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
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
