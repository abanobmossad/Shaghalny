from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import Job
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy, reverse
from company.forms import JobForm
# Create your views here.


class CreateJob(CreateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('company:jobs')
    template_name = 'company/new_job.html'

    def form_valid(self, form):
        form.instance.company = self.request.user.company
        return super().form_valid(form)


class UpdateJob(UpdateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy('company:jobs')
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


class Dashboard(ListView):
    model = Job
    template_name = 'company/dashboard.html'


class CompanyJobs(ListView):
    model = Job
    context_object_name = 'company_jobs'
    template_name = 'company/company_jobs.html'

    def get_queryset(self):
        print(self.request.user.company)
        job = Job.objects.filter(company=self.request.user.company)
        return job
