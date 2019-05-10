from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        help_text='The title of the article.',
    )
    body = models.TextField(
        blank=True,  # Article can have blank body.
        help_text="The body text of the article.",
    )
    author = models.CharField(
        max_length=30,
        help_text="The name of the author who published the article.",
    )
    create_date = models.DateField(
        help_text="The date of the article.",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
