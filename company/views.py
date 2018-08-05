from django.shortcuts import render
from jobs.models import Job
from django.views.generic import CreateView,DeleteView,DetailView,ListView
from django.urls import reverse_lazy
# Create your views here.


class CreateJob(CreateView):
    model = Job
    success_url = reverse_lazy('company:dashboard')
    template_name = 'company/new_job.html'

class Dashboard(ListView):
    model = Job
    context_object_name = 'appliers'
    template_name='company/dashboard.html'    

class CompanyJobs(ListView):
    model = Job
    context_object_name = 'company_Jobs'
    template_name='company/company_jobs.html'

    def get_queryset(self):
        print(self.request)
        job = Job.objects.filter(complany=self.request.user.company)
        return job

