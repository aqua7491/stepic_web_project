from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from qa.models import Question, paginate, Answer
 
def test(request, *args, **kwargs):
	return HttpResponse('OK')


def question_list(request):
    #Using Paginate
	page, paginator = paginate(request, Question.objects.new())
#    paginator.baseurl = reverse('question_list') + '?page='

	return render(request, 'list.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})


def popular(request):

    #Pagination
	page, paginator = paginate(request, Question.objects.populr())
    #Update baseurl
#    paginator.baseurl = reverse('popular') + '?page='
    #Return answer
	return render(request, 'list_rating.html', {
		'questions': page.object_list,
		'page': page,
		'paginator': paginator,
	})


def question_detail(request, pk):
	question = get_object_or_404(Question, id=pk)
#    answers = question.answer_set.all()
	answers = Answer.objects.filter(question_id__exact=int(id))
	return render(request, 'detail.html', {
		'question': question,
		'answers': answers,})









