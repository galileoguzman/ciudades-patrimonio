from django.views.generic import TemplateView
from . import models


class IndexView(TemplateView):
	model = models.Post
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(*kwargs)
		context['posts'] = self.model.objects.all()
		return context


class PostView(TemplateView):
	model = models.Post
	template_name = 'post.html'

	def  get_context_data(self, **kwargs):
		context = super(PostView, self).get_context_data(*kwargs)
		context['post'] = self.model.objects.filter(slug=context['slug'])
		return context
		


