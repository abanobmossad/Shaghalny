from django.urls import path
from jobs.views import JobDetail

app_name = 'jobs'
urlpatterns = [
  path('<slug>/',JobDetail.as_view(),name="job_details")
]
