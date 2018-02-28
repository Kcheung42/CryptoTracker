# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Crypto
from django_apps.cryptoApp.Crawler import Crawler
from django.core.urlresolvers import reverse

# Create your views here.

def crypto_list(request):
	if request.method == 'POST':
		Crawler()
	query_list = Crypto.objects.all().order_by('-price')
	context = {
		"title":"Crypto",
		"object_list":query_list,
	}
	print(query_list.count())
	return render(request,'index.html', context)

def crypto_detail(request):
	pass

