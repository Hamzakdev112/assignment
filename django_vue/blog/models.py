from django.db import models

class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	published = models.DateTimeField(null=True, blank=True)
	title = models.CharField(max_length=256)
	body = models.TextField()

	def __str__(self):
		return self.title
