from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe
import json

class IndexView(TemplateView):
	template_name = 'index.html'


class RoomView(TemplateView):
	template_name = 'room.html'

	def get_context_data(self, **kwargs):
		context = super(RoomView, self).get_context_data(**kwargs)
		context['room_name_json'] = mark_safe(
			json.dumps(self.kwargs['room_name'])
			)
		return context
