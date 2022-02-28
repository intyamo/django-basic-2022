from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return '\n'.join((self.title, f'{self.author.username} | {self.date}', '\n', self.text[:140]))

    def get_absolute_url(self):
        if self.slug:
            return reverse('single_post_slug', kwargs={'slug': self.slug})
        else:
            return reverse('single_post', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(*args, **kwargs)
