from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, TemplateView, View
from django.urls import reverse_lazy, reverse
from accounts.forms import SignUpUserForm, SignUpCompanyForm
from accounts.models import User
from django.contrib.auth import login
#  Create your views here.


class HomePage(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_company:
                return redirect("company:dashboard")
            elif self.request.user.is_job_seeker:
                return redirect("explore")
        else:
            return render(request, 'index.html')


class UserSignUp(CreateView):
    model = User
    form_class = SignUpUserForm
    template_name = 'registration/signup_user.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class CompanySignUp(CreateView):
    model = User
    form_class = SignUpCompanyForm
    template_name = 'registration/signup_company.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
