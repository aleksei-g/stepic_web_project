from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField()#min_length = 1) 
	text = forms.CharField(widget=forms.Textarea)#,min_length = 1)

#	def __init__(self, user=None, **kwargs):
#		self.user = user
#		super(AskForm, self).__init__(kwargs)

#	def clean_title(self):
#		title = self.cleaned_data['title']
#		if title=='':
#			raise forms.ValidationError(
#				u'none data!', code=12)
#		return title
#
#	def clean(self):
#		if 1==0:
#			raise forms.ValidationError(
#				u'No validation',
#				code = 1
#			)
#
	def save(self):
		self.cleaned_data['author'] = self.user
		question = Question(**self.cleaned_data)
		question.save()
		#question = Question.objects.create(text=self.cleaned_data['text'], title=self.cleaned_data['title'], author=self.user)
		return question


class AnswerForm(forms.Form):
	text = forms.CharField(min_length=1, widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput())
#	question = forms.ModelChoiceField(queryset=Question.objects.all())

#	def __init__(self, user=None, question=None, **kwargs):
#		self.user = user
#		self.question = question
#		super(AnswerForm, self).__init__(kwargs)

	def clean_question(self):
		return Question.objects.get(pk=int(self.cleaned_data['question']))
	
	def save(self):
		self.cleaned_data['author'] = self.user
		answer = Answer(**self.cleaned_data)
#		answer.question = Question.objects.get(id=self._question)
		answer.save()
#		answer = Answer.objects.create(text=self.cleaned_data['text'], question=self.cleaned_data['question_id'])
		return answer


#class AnswerForm(ModelForm):
#	class Meta:
#		model = Answer
#		fields = ['text']


class SignupForm(forms.Form):
	username = forms.CharField(min_length=1)
	email = forms.EmailField()
	password = forms.CharField(min_length=1, widget=forms.PasswordInput)

	def save(self):
		user = User.objects.create_user(**self.cleaned_data)
		user.save()
		return user

class LoginForm(forms.Form):
	username = forms.CharField(min_length=1)
	password = forms.CharField(min_length=1, widget=forms.PasswordInput)
