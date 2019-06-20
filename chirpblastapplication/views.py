from django.http import HttpResponse
from django.views.generic import TemplateView
from .services.web.restservice import WebRequest
from .forms.chirpblastapplication.login import LoginForm
from django.views.generic.edit import FormView

class IndexView(TemplateView):
    template_name = 'chirpblastapplication/index.html'

    def __init__(self):
        self.__testJson= self.Test()
        self.__testData = WebRequest.parse_JSON(self.__testJson)
        print(self.__testData)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        geoData = self.__testData
        context.update({'geoData': geoData})
        return context

    def Test(sefl):
        try:
            webrequest = WebRequest('https://freegeoip.app/json/')
            return webrequest.get()
        except:
            return 0

class LoginView(FormView):
    template_name = 'chirpblastapplication/login.html'
    form_class = LoginForm
    user_authenticated = False

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({'user': self.user_authenticated})
        return context

            

    