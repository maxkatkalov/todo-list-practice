from django.db import models


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True, null=True, related_name="tasks")


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ["done", "deadline"]
