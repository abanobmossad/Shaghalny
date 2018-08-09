from django.urls import path
from company.views import CreateJob, Dashboard, CompanyJobs, UpdateJob, delete_job
app_name = 'company'
urlpatterns = [
    # auth section
    path("new-job/", CreateJob.as_view(), name="new_job"),
    path("<pk>/update-job/", UpdateJob.as_view(), name="update_job"),
    path("<pk>/delete/", delete_job, name="delete_job"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("myjobs/", CompanyJobs.as_view(), name="jobs"),

    # event
]
