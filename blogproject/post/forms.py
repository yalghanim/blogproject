from django import forms

from .models import Post

class PostForm(forms.ModelForm):
	#ask hamza about . (ModelForm referring to forms?)
	class Meta:
		model = Post
		fields = ['title', 'content']
		