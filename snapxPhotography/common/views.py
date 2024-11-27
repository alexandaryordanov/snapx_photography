from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView, LoginView):
    template_name = 'common/index.html'
