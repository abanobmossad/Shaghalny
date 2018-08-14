from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import Job
from accounts.models import UserProfile
from django.http import HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

REDIRECT_FIELD_NAME = 'index.html'
LOGIN_URL = reverse_lazy('login')


class RelatedJobList(ListView, LoginRequiredMixin):
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    model = Job
    context_object_name = 'jobs'
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user.userprofile
        user_job_type = user.job_type
        user_experience = user.experience
        user_career_level = user.career_levele
        user_skills = user.skills
        jobs = Job.objects.filter(
            career_levele=user_career_level, job_type=user_job_type)
        return jobs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        saved_jobs = self.request.user.userprofile.user_saved_jobs.all()
        context["saved_jobs"] = saved_jobs
        return context


class JobDetail(DetailView):
    model = Job
    template_name = 'jobs/job_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_job = get_object_or_404(Job, slug=self.kwargs.get("slug"))
        context['related'] = Job.objects.filter(
            description__search="Developer")

        if self.request.user.is_authenticated:
            applications = self.request.user.userprofile.application_users.all()
            context['applied_jobs'] = applications

        return context


class MyApplicationsView(View, LoginRequiredMixin):

    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    def get(self, request, *args, **kwargs):

        applications = request.user.userprofile.application_users.all()

        return render(request, 'jobs/my_jobs.html', {"myjobs": applications})


class MySavedJobsView(View, LoginRequiredMixin):

    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    def get(self, request, *args, **kwargs):

        saved = request.user.userprofile.user_saved_jobs.all()

        return render(request, 'jobs/my_jobs.html', {"myjobs": saved, 'saved': True})


@login_required(redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL)
def save_job(request, slug):
    
    if request.method == "POST":
        job = get_object_or_404(Job, slug=slug)
        job.saved_jobs.add(request.user.userprofile)
        data = {
            "is_saved": True
        }
        return JsonResponse(data)

    return redirect(reverse('index'))


@login_required(redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL)
def un_save_job(request, slug):
    if request.method == "POST":
        job = get_object_or_404(Job, slug=slug)
        job.saved_jobs.remove(request.user.userprofile)
        data = {
            "is_unsaved": True
        }
        return JsonResponse(data)

    return redirect(reverse('index'))


@login_required(redirect_field_name=REDIRECT_FIELD_NAME, login_url=LOGIN_URL)
def apply_job(request, slug):
    if request.method == "POST":
        job = get_object_or_404(Job, slug=slug)
        job.applications.add(request.user.userprofile)
        data = {
            "is_apply": True
        }
        return JsonResponse(data)

    return redirect(reverse('index'))
