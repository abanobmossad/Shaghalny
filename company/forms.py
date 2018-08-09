from jobs.models import Job
from django import forms
from django.utils.text import slugify


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('company', 'date', 'slug')

        widgets = {
            'description': forms.Textarea(),
            'requirements': forms.Textarea(),
        }

    def save(self):
        job = super().save(commit=False)
        slug = slugify("{} --{} {} ---{}".format(job.title,
                                                 job.company, job.company.address, job.date))
        job.slug = slug
        job.save()
        return job
