from django.db import models

# Create your models here.
class JobPosting(models.Model):
    # id - starts at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    # Modify name of object
    def __str__(self):
        return f"{self.title} | {self.company} | Active: {self.is_active}"

    # CRUD Operations
    # create
    # read
    # update
    # delete

    # model manager -> objects
    # JobPosting.objects.all()
    # JobPosting.objects.get(id=1)
    # JobPosting.objects.filter(company="abc tech")

    # Django shell
    # python manage.py shell
    # from job_board.models import JobPosting
    # JobPosting.objects.all()
    # JobPosting.objects.create(title="A Job Title", description="First Job", company="ABC Tech", salary=75000)
    # job = JobPosting.objects.get(id=1)
    # job
    # job.description
    # job.description = "A Good First Job"
    # job.save()
    # job.description

    # job.delete()
    # JobPosting.objects.all()