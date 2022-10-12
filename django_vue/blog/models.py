from django.db import models
from django.urls import reverse

class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	published = models.DateTimeField(null=True, blank=True)
	title = models.CharField(max_length=256)
	body = models.TextField()

	def __str__(self):
		return self.title

	@property
	def detail_url(self):
		return reverse('post_detail', args=[self.pk])
