# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader, Context
from django.views.generic import TemplateView, View


class IndexView(TemplateView):
    template_name = 'contrib/index.html'


class ServiceWorker(View):

    def get(self, request, *args, **kwargs):
        javascript = loader.get_template('contrib/service-worker.js')
        response = HttpResponse(javascript.render({}))
        response['Content-Type'] = 'application/javascript'
        return response
