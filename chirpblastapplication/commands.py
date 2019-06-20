from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from .forms.chirpblastapplication.login import LoginForm

class Login(FormView):
    form_class = LoginForm
    user_authenticated = False
    success_url = '/index'
    
    def form_valid(self, form):
        return super().form_valid(form)