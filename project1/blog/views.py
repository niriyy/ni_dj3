from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def blog(request):
  template = loader.get_template('b.html')
  return HttpResponse(template.render())