from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
	return HttpResponse('OK')

#proverka parametrov paginatora
def paginate(request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
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
	return render(request, 'qa/question_popular.html',{
		'questions': page.object_list,
		'paginator': page.paginator, 
		'page': page,
		})


#URL = /question/5/
#@require_GET
def question_details(request, pk=None):
	question = get_object_or_404(Question, pk=pk)	
	try:
		answers = Answer.objects.all()
		answers = Answer.objects.filter(question_id = pk)
		answers = answers.order_by('added_at')
		#answers = answers.order_by('id')
	except Answer.DoesNotExist:
		answer = None
	#form = AnswerForm(request, question.id)
	form = AnswerForm(initial={'question': question.id})
	return render(request, 'qa/question_details.html', {
	'question': question,	
	'answers': answers,
	'form': form
	})



#URL = /ask/
def question_add(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			#return HttpResponseRedirect(question.get_url())
			return HttpResponseRedirect("/question/%s/" %question.id)
			#return HttpResponseRedirect("/question/"+str(question.id)+"/") 
	else:
		form = AskForm()
	return render(request, 'qa/question_add.html', {
		'form': form
	})

def show(request, pk):
	question = get_object_or404(Question, pk=pk)
	form = AnswerForm(initial={'question': question.id})
	return render(request, 'qa/question_details.html', {'q': question, 'form': form})


#URL = /answer/
def answer_add(request, question_id):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		#form._question=question_id
		if form.is_valid():
			#answer = form.save(commit=False)
			#answer.question = Question.objects.get(id=question_id)
			#answer.question = question_id
			#answer.save()
			#return HttpResponseRedirect(question.get_url())
			answer = form.save()
			#return HttpResponseRedirect("/question/"+str(question_id)+"/")
			return redirect('question_details', answer.question.id)
	else:
		form = AnswerForm()
	return render(request, 'qa/question_details.html', {
		'form': form
	})
