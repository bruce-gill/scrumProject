from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Sprint(models.Model):
    """Development iteration period."""
    name = models.CharField(max_length=100, blank=True, default="")
    description = models.TextField(blank=True, default="")
    start = models.DateField(unique=True)
    end = models.DateField(unique=True)
    project = models.ForeignKey(project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name or "Sprint ending %s" % self.end


class TaskStatus(models.Model):
    """The status of a task."""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    """Unit of work to be done for the sprint."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    order = models.SmallIntegerField(default=0)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name