from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=255) 
	text = forms.CharField(widget=forms.Textarea)

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

	def save(self):
		question = Question(**self.cleaned_data)
		question.save()
		return question

