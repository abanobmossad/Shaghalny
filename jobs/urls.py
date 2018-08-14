from django.urls import path
from jobs.views import JobDetail, MyApplicationsView, MySavedJobsView, save_job,un_save_job,apply_job

app_name = 'jobs'
urlpatterns = [
    path("appications", MyApplicationsView.as_view(), name="applications"),
    path("save/<slug>", save_job, name="save_job"),
    path("unsave/<slug>", un_save_job, name="un_save_job"),
    path("apply/<slug>", apply_job, name="apply_job"),
    path("saved", MySavedJobsView.as_view(), name="display_saved_jobs"),
    path("<slug>/", JobDetail.as_view(), name="job_details"),
]
