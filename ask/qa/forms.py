from django import forms
from django.forms import ModelForm
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=255) 
	text = forms.CharField(widget=forms.Textarea)

	def clean_title(self):
		title = self.cleaned_data['title']
		if title=='':
			raise forms.ValidationError(
				u'none data!', code=12)
		return title

	def clean(self):
		if 1==0:
			raise forms.ValidationError(
				u'No validation',
				code = 1
			)

	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question


class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput())
#	question = forms.ModelChoiceField(queryset=Question.objects.all())

#	def __init__(self, question, *args, **kwargs):
#		self._question = question
#		super(AnswerForm, self).__init__(*args,**kwargs)

	def clean_question(self):
		return Question.objects.get(pk=int(self.cleaned_data['question']))
	
	def save(self):
#		self.cleaned_data['question_id'] = self._question
		answer = Answer(**self.cleaned_data)
#		answer.question = Question.objects.get(id=self._question)
		answer.save()
#		answer = Answer.objects.create(text=self.cleaned_data['text'], question=self.cleaned_data['question_id'])
		return answer


#class AnswerForm(ModelForm):
#	class Meta:
#		model = Answer
#		fields = ['text']
