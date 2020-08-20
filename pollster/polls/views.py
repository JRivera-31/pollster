from django.shortcuts import render

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
    return render(request, 'polls/results.html', {'question': question})

# Get question and display results
def results(request, question_id):
    # get the question
    question = get_object_or_404(Question, pk=question_id)
    # return the data
    return render(request, 'polls/results.html', {'question': question})