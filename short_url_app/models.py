from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    shortened = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def total_accesses(self):
        click = self.click_set.get()
        return click.access_count

    def last_accessed(self):
        click = self.click_set.get()
        return click.last_accessed


class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    last_accessed = models.DateTimeField(null=True)
    access_count = models.IntegerField(default=0)
