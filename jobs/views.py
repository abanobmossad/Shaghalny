from django.shortcuts import render, get_object_or_404
from jobs.models import Job
from accounts.models import UserProfile
from django.views.generic import ListView, DetailView
# Create your views here.


class RelatedJobList(ListView):
    model = Job
    context_object_name = 'related_jobs'
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user.userprofile
        user_job_type = user.job_type
        user_experience = user.experience
        user_career_level = user.career_levele
        user_skills = user.skills
        jobs = Job.objects.filter(career_levele=user_career_level, job_type=user_job_type,
                                  experience_needed__lte=user_experience)

        return jobs


class JobDetail(DetailView):
    model = Job
    template_name = 'jobs/job_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_job = get_object_or_404(Job, slug=self.kwargs.get("slug"))
        context['related'] = Job.objects.filter(title__contains=this_job.title)
        return context
