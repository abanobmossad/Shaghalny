from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import Job
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy, reverse
from company.forms import JobForm
from django.contrib.auth.mixins import LoginRequiredMixin

REDIRECT_FIELD_NAME = 'index.html'
LOGIN_URL = reverse_lazy('login')


class CreateJob(CreateView, LoginRequiredMixin):
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    model = Job
    form_class = JobForm
    success_url = reverse_lazy('company:myjobs')
    template_name = 'company/new_job.html'

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class UpdateJob(UpdateView, LoginRequiredMixin):
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    model = Job
    form_class = JobForm
    success_url = reverse_lazy('company:myjobs')
    template_name = 'company/new_job.html'

    def get(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs.get("pk"))
        if not job.company == self.request.user.company:
            redirect('index')
        return super().get(request, *args, **kwargs)


def delete_job(request, pk):
    """ delete a job form company profile and redirect """
    job = get_object_or_404(Job, pk=pk)

    if request.method == 'POST':
        if not job.company == request.user.company:
            return redirect("index")
        job.delete()
        return redirect('company:dashboard')

    else:
        return redirect("index")


class Dashboard(ListView, LoginRequiredMixin):
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    model = Job
    template_name = 'company/dashboard.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        jobs = Job.objects.filter(
            applications__isnull=False, company=self.request.user.company)
        return jobs


class CompanyJobs(ListView, LoginRequiredMixin):
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    model = Job
    context_object_name = 'company_jobs'
    template_name = 'company/company_jobs.html'

    def get_queryset(self):
        print(self.request.user.company)
        job = Job.objects.filter(company=self.request.user.company)
        return job
