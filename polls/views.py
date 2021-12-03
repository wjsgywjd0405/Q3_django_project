from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# Create your views here.
### Generic VIew (class-based views)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# 투표 목록(index)
# def index(request):
    # return HttpResponse("Hello world. You're at the polls index.")
    # Question 테이블에 등록된 것들중에 가장 최근에 등록된 날짜로 5개를 가져옴
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # list를 순회하며 하나씩 가져옴, 그 텍스트를 ,로 연결하여 작성해줌 -> output에 들어감
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # template = loader.get_template('polls/index.html') #temlate 변수에 들어감
    # context = { #context라는 사전형 변수에 넣어줌
        # 'latest_question_list' : latest_question_list
    # }
    # return render(request, 'polls/index.html', context) #render() 단축 함수


# 투표 상세(detail)
# def detail(request, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request,'polls/detail.html', {'question':question})

# 투표 결과(results)
# def results(request, question_id):
    # response = HttpResponse("You're looking at results of question %s." % question_id)
    # return response
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/results.html', {'question': question})

# 투표 기능(vote)
def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice"})
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))