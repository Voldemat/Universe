from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AccountPageView(TemplateView):
    template_name = 'pages/account.html'