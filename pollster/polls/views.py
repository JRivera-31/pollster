from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# Get questions and display them
def index(request):
    # create latest question list, order by ascending date and limit to 5
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # create object to pass to render method to access question data on front end
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)

# Show specific questions and choices
def detail(request, question_id):
    # try to get the question by id
    try:
        question = Question.objects.get(pk=question_id)
    
    # send back error if question is not found
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    # return the question if try is successful
    return render(request, 'polls/detail.html', {'question': question})

# Get question and display results
def results(request, question_id):
    # get the question
    question = get_object_or_404(Question, pk=question_id)

    # return the question data
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice
def vote(request, question_id):
    # get question
    question = get_object_or_404(Question, pk=question_id)

    # try to post selected choice
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # if a choice is not selected
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })

    # if everything goes okay, increment vote by 1 and save to db    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if the user
        # hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))