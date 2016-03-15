from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout

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
@login_required
def question_add(request):
	#user = request.user
	if request.method == "POST":
		form = AskForm(request.POST)
		form.user=request.user
		#text = request.POST['text']
		#title = request.POST['title']
		#form = AskForm(user, text=text, title=title)
		if form.is_valid():
			question = form.save()
			return HttpResponseRedirect("/question/%s/" %question.id)
			#return HttpResponseRedirect("/question/"+str(question.id)+"/") 
			#return redirect('question_details', question.id)
	else:
		form = AskForm()
	return render(request, 'qa/question_add.html', {
		'form': form
	})


#URL = /answer/
@login_required
def answer_add(request, question_id):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		form.user=request.user
		if form.is_valid():
			answer = form.save()
			return redirect('question_details', answer.question.id)
	else:
		form = AnswerForm()
	return render(request, 'qa/question_details.html', {	
		'form': form,
	})


#URL = /signup/
def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			user = authenticate(username=request.POST.get('username'), password = request.POST.get('password'))
			#user = form.save()
			if user is not None and user.is_active:
				login(request,user)
				return HttpResponseRedirect("/")
	else:
		form = SignupForm()
	return render(request, 'qa/signup.html', {
		'form': form
	})

#URL = /login/
def login_user(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=request.POST.get('username'), password = request.POST.get('password'))
			if user is not None and user.is_active:
				login(request,user)
				return HttpResponseRedirect("/")
	else:
		form = LoginForm()
	return render(request, 'qa/login.html', {
		'form': form
	})


#URL = /logout/
def logout_user(request):
	logout(request)
	return HttpResponseRedirect("/")
