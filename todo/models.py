from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='tasks')

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('task_list')

