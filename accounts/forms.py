from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import User, Company, UserProfile
from django.db import transaction


class SignUpUserForm(UserCreationForm):
    CAREER_LIVEL_CHOICES = (
        ('ENTRY', 'Freshman'),
        ('EXPERIENCE_NM', 'Experienced (Non-Manager)'),
        ('MANAGER', 'Manager'),
    )
    JOB_TYPE_CHOICES = (
        ('FULL', 'Full Time'),
        ('PART', 'Part Time'),
        ('REMOTE', 'Remotely'),
    )
    LANGUAGES_CHOICES = (
        ('ARABIC', 'Arabic'),
        ('ENGLISH', 'English'),
        ('FRENCH', 'French'),
    )

    career_levele = forms.ChoiceField(
        choices=CAREER_LIVEL_CHOICES,
        label="Whate is your current career level ?"
    )
    job_type = forms.ChoiceField(
        choices=JOB_TYPE_CHOICES,
        label="Whate is the job type you searching for ?"

    )
    languages = forms.ChoiceField(
        choices=LANGUAGES_CHOICES,
        label="Whate languages do you have ?"

    )

    education = forms.CharField(label="What is your education ?")
    skills = forms.CharField(
        widget=forms.Textarea,label="Write down all your skills you have " )
    salary = forms.IntegerField(label="What salary you expect you will have ?")
    experience = forms.IntegerField(label="How many experience do you have ?")
    image = forms.ImageField(
        required=False, label="Enter a recent image of You")

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels={
            'username':"Enter your user name (the viable name)",
            'password':"Repeate the password ",
            'password1': "Enter a powerful password",
        }
       
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_job_seeker = True
        user.save()
        profile = UserProfile.objects.create(
            user=user, career_levele=self.cleaned_data.get('career_levele'),
            job_type=self.cleaned_data.get('job_type'),
            languages=self.cleaned_data.get('languages'),
            education=self.cleaned_data.get('education'),
            skills=self.cleaned_data.get('skills'),
            salary=self.cleaned_data.get('salary'),
            experience=self.cleaned_data.get('experience'),
            image=self.cleaned_data.get('image'))

        return user


class SignUpCompanyForm(UserCreationForm):
    description = forms.CharField(widget=forms.Textarea, max_length=255,
                                  required=False)
    address = forms.CharField(max_length=140, required=True)
    industry = forms.CharField(max_length=140, required=True)
    image = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        labels = {
            'username': 'Company name'
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        company = Company.objects.create(
            user=user, company_name=user.username,
            description=self.cleaned_data.get('description'),
            industry=self.cleaned_data.get('industry'),
            address=self.cleaned_data.get('address'),
            image=self.cleaned_data.get('image'))

        return user


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        