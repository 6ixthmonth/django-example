"""
polls 앱의 뷰를 작성하는 파일.
"""


# from django.http import HttpResponse
# from django.template import loader
# from django.http import Http404
# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.utils import timezone

from .models import Choice, Question


# def index(request):
#     """
#     'polls/' 요청 URL을 처리하는 함수.
#     데이터베이스에서 최신 질문 데이터들을 가져와서 웹 페이지로 전달한다.
#     처리 후 설문 목록 페이지로 이동시킨다.
#     """

#     # 임시로 작성한 응답 객체.
#     # return HttpResponse("Hello, world. You're at the polls index.")

#     # 날짜 역순으로 정렬하여 최신 질문 데이터 5개를 가져온다.
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]

#     # 데이터를 이용해서 화면에 표시할 내용을 직접 하드코딩 하는 경우.
#     # output = "<br>".join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)

#     # 템플릿을 사용하는 경우. 전달할 데이터 또한 함께 넘겨준다.
#     # template = loader.get_template('polls/index.html')
#     # context = {'latest_question_list': latest_question_list}
#     # return HttpResponse(template.render(context, request))

#     # 템플릿 단축 함수를 사용하는 경우. 더 이상 loader 모듈과 HttpResponse 객체를 사용하지 않아도 된다.
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     """
#     'polls/<int:question_id>/' 요청 URL을 처리하는 함수.
#     전달받은 question_id에 해당하는 데이터를 가져와서 웹 페이지로 전달한다.
#     처리 후 설문 상세 페이지로 이동시킨다.
#     """

#     # 임시로 작성한 응답 객체.
#     # return HttpResponse("You're looking at question %s." % question_id)

#     # 템플릿 단축 함수를 사용하는 경우. 찾고자 하는 데이터가 없으면 404 오류가 발생하도록 설정한다.
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, "polls/detail.html", {"question": question})

#     # 오류 단축 함수를 사용하는 경우.
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     """
#     'polls/<int:question_id>/results/' 요청 URL을 처리하는 함수.
#     전달받은 question_id에 해당하는 데이터를 가져와서 웹 페이지로 전달한다.
#     처리 후 설문 결과 페이지로 이동시킨다.
#     """

#     # 임시로 작성한 응답 객체.
#     # return HttpResponse("You're looking at the results of question %s." % question_id)

#     # 오류 단축 함수를 사용하는 경우.
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """
    'polls/<int:question_id>/vote/' 요청 URL을 처리하는 함수.
    전달받은 question_id에 해당하는 설문에 대해 투표 처리를 한다.
    처리 후 설문 상세 페이지로 리다이렉트 한다.
    """

    # 임시로 작성한 응답 객체.
    # return HttpResponse("You're voting on question %s." % question_id)

    # 템플릿 단축 함수 및 오류 단축 함수를 사용하는 경우.
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # request.POST['choice']에서 KeyError 발생 가능
    except (KeyError, Choice.DoesNotExist):
        # 오류 발생 시 질문 투표 양식을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "선택을 하지 않으셨습니다.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 성공적으로 처리한 후 항상 HttpResponseRedirect 객체를 반환한다.
        # 만약 사용자가 뒤로 가기 버튼을 클릭하면 데이터가 두 번 처리되는 것을 방지한다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    """설문 목록으로 이동하는 클래스."""
    template_name = "polls/index.html"  # 이 뷰에서 연결할 템플릿 이름. 기본 값은 <앱 이름>/<모델 이름>_list.html
    context_object_name = "latest_question_list"  # 클라이언트로 전달할 콘텍스트 객체의 이름. 기본 값은 object_list 또는 <모델 이름>_list

    def get_queryset(self):
        """최근 등록된 설문 다섯 개를 반환한다."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """설문 상세 페이지로 이동하는 클래스."""
    model = Question  # 각각의 제네릭 뷰에게 어떤 모델에 대해 동작할지 알려주는 변수.
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """설문 결과 페이지로 이동하는 클래스."""
    model = Question
    template_name = 'polls/results.html'
