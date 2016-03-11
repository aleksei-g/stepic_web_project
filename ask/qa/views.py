from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from qa.models import Question, Answer

def test(request, *args, **kwargs):
	return HttpResponse('OK')

#proverka parametrov paginatora
def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 2))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10	

	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
		#page = 1

	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	
	#paginator.baseurl = '?page='
	paginator.baseurl = request.path + '?page='
	return page


#URL = /?page=2
@require_GET
def question_new(request, act_page=None):
	questions = Question.objects.all()
	questions = questions.order_by('-id')
	page = paginate(request, questions)
	return render(request, 'qa/question_new.html',{
		'questions': page.object_list,
		'paginator': page.paginator, 
		'page': page,
		})


#URL = /popular/?page=2
@require_GET
def question_popular(request, act_page=None):
	questions = Question.objects.all()
	questions = questions.order_by('-rating')
	page = paginate(request, questions)
	return render(request, 'qa/question_new.html',{
		'questions': page.object_list,
		'paginator': page.paginator, 
		'page': page,
		})


#URL = /question/5/
@require_GET
def question_details(request, pk=None):
	#question = Question.objects.get(pk=pk)
	question = get_object_or_404(Question, pk=pk)	
	try:
		answers = Answer.objects.all()
		answers = Answer.objects.filter(question_id = pk)
		answers = answers.order_by('added_at')
		#answers = answers.order_by('id')
	except Answer.DoesNotExist:
		answers = None
	#response = HttpResponse(
	#	content = '<html><h1>'+pk+'</h1></html>',
	#	content_type = 'text/html',
	#	status = 200,	
	#)
	#return HttpResponse(question.title+';\n'+question.text)
	return render(request, 'qa/question_details.html', {
	'question': question,	
	'answers': answers,
	})
