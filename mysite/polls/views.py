"""
View 함수 또는 클래스를 작성하는 스크립트 파일.
"""


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# def index(request):
#     """`polls/` 요청 URL을 처리하는 함수. 데이터베이스에서 최신 질문 데이터들을 가져와서 웹 페이지로 전달한다."""

#     # return HttpResponse("Hello, world. You're at the polls index.")

#     # 날짜 역순으로 정렬하여 최신 질문 데이터 5개를 가져온다.
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]

#     # hardcoding
#     # output = "<br>".join([q.question_text for q in latest_question_list])
#     # print(output)
#     # return HttpResponse(output)

#     # use template
#     # template = loader.get_template('polls/index.html')
#     # context = {'latest_question_list': latest_question_list}
#     # return HttpResponse(template.render(context, request))

#     # use shortcut
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     """`polls/<int:question_id>/` 요청 URL을 처리하는 함수. 함수 설명"""

#     # return HttpResponse("You're looking at question %s." % question_id)

#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, "polls/detail.html", {"question": question})

#     # user shortcut
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     """`polls/<int:question_id>/results/` 요청 URL을 처리하는 함수. 함수 설명"""

#     # return HttpResponse("You're looking at the results of question %s." % question_id)

#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """`polls/<int:question_id>/vote/` 요청 URL을 처리하는 함수. 함수 설명"""
    
    # return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = "polls/index.html" # <app name>/<model name>_list.html
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html' # <app name>/<model name>_detail.html


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
