# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

from django.http import HttpResponse
from django.template import loader, Context
from django.views.generic import TemplateView, View


PRESENCE_API = 'https://api.pushy.me/devices/presence?api_key=some_api_key'  

class IndexView(TemplateView):
    template_name = 'contrib/index.html'


class ServiceWorker(View):

    def get(self, request, *args, **kwargs):
        javascript = loader.get_template('contrib/service-worker.js')
        response = HttpResponse(javascript.render({}))
        response['Content-Type'] = 'application/javascript'
        return response


class PresenceTestView(TemplateView):
	template_name = 'contrib/presence.html'

	def post(self, request, *args, **kwargs):
		device = request.POST.get('device', 0)
		tokens = list(map(str, [device]))
		payload = {'registration_ids': tokens}
		req = requests.post(
			PRESENCE_API,
			headers={'Content-Type': 'application/json'},
			data=json.dumps(payload))
		context = self.get_context_data(*args, **kwargs)
		context['response'] = req.text
		return self.render_to_response(context)