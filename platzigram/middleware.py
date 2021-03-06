"""Platzigram middelware catalog"""

#Django
from django.shortcuts import redirect
from django.urls import reverse

class  ProfileCompletionMiddelware:
	"""Profile Completion Middelware
	Ensure that every user that interacting with the platzigram has biograpfy
	"""
	def __init__(self, get_response):
		"""Middelware initialization"""
		self.get_response = get_response

	def __call__(self, request):
		"""Code to be executed for each request before the view is called"""

		if not request.user.is_anonymous:
			if not request.user.is_staff:
				profile = request.user.profile
				if not profile.picture or not profile.biography:
					if request.path not in [reverse('update_profile'),reverse('logout')]:
				 		return redirect('update_profile')

		response = self.get_response(request)
		return response