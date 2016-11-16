from django import forms
from models import Question, Answer


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "text"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text", "question"]

'''
class AskForm(forms.ModelForm):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean_title(self):
		title = cleaned_data['title']
		if title.strip() == '':
			raise forms.ValidationError(u'Incorrect Title')
		return title

	def clean_text(self):
		text = cleaned_data['text']
		if text.strip() == '':
			raise forms.ValidationError(u'Incorrect Text')
		return text

	def save(self):
		question=Question(**self.cleaned_data)
		question.save()
		return question


class AnswerForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)

	def clean_text(self):
		title = cleaned_data['text']
		if title.strip() == '':
			raise forms.ValidationError(u'Incorrect Text')
		return title

	def save(self):
		answer=Answer(**self.cleaned_data)
		answer.save()
		return answer
'''