from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

""" longform render HttpResponse with template
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
"""

# Shortcut render
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

# Longform 404
"""
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    context = {
        "question": question
    }
    return render(request, "polls/detail.html", context)
    # old stub
    #return HttpResponse("You're looking at question %s." % question_id)
"""

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# Stub
def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

# Stub
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
