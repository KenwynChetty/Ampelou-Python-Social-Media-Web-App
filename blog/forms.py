from django import forms
from .models import Comment, Post

class NewPostForm(forms.ModelForm):
	pic = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
	

	class Meta:
		model = Post
		fields = ['pic', 'caption']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
