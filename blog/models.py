from django.db import models

# Create your models here.


class AuditedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True


class Post(AuditedModel):
	title = models.CharField(max_length=50, unique=True)
	img = models.ImageField(upload_to='media/')
	content = models.CharField(max_length=2500)
	slug = models.SlugField(max_length=100, blank=True)

	def save(self, *args, **kwargs):
		self.slug = self.title.lower().replace(' ','-')
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
			
		