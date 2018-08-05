from django.urls import path
from accounts.views import UserSignUp,CompanySignUp
app_name = 'accounts'
urlpatterns = [
    # auth section
    path("signup/company/", CompanySignUp.as_view(), name="signup_company"),
    path("signup/job-seeker/", UserSignUp.as_view(), name="signup_job_seeker"),

    # event
]
