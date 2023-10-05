from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False, blank=False)
    tags = models.ManyToManyField("Tag", blank=True, related_name="tasks")

    class Meta:
        ordering = ["-done", "deadline"]


class Tag(models.Model):
    name = models.CharField(max_length=50)


