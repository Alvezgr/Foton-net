"""User views"""
#Django
from django.urls import reverse
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView

#Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile
#Forms
from users.forms import SignupForm
#Local modules


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all() 
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        """Add users post to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LoginView(auth_views.LoginView):
    """Login VIew"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Log out from the platform"""
    template_name = 'users/login.html'

def signup_view(request):
    """sign up users"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()
    return render(
        request = request,
        template_name = 'users/signup.html',
        context = {'form': form}
        )

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update a profile"""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website','biography','phone_number','picture']

    def get_object(self):
        """Return User Profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return success url"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username':username})