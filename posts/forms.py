"""Post forms"""


#Django
from django import forms

#Local
from posts.models import Post

class PostForm(forms.ModelForm):
	"""The post form"""

	class Meta:
		"""Form settings"""

		model = Post
		fields = ('user','profile','title', 'photo')