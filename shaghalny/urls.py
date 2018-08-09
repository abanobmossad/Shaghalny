"""shaghalny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from jobs import views as jobs_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.HomePage.as_view(), name='index'),
    # auth section
    path("accounts/", include('accounts.urls'), name="accounts"),
    path("employer/", include('company.urls'), name="employer"),
    path("explore/", jobs_views.RelatedJobList.as_view(), name="explore"),
    path("jobs/", include('jobs.urls'), name="jobs"),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout,
         name='logout', kwargs={'next_page': '/'}),

    # event
]
