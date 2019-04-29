from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    brief_content = models.TextField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title