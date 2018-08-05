from django.urls import path
from company.views import CreateJob, Dashboard, CompanyJobs
app_name = 'company'
urlpatterns = [
    # auth section
    path("new-job/", CreateJob.as_view(), name="new_job"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("myjobs/", CompanyJobs.as_view(), name="jobs"),

    # event
]
