# Create your views here.
from django.http import HttpResponse
import requests
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from resumeuploader.settings import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
import json


def login(request):
	login_url = "http://join.agiliq.com/oauth/authorize/?client_id="+CLIENT_ID+"&redirect_uri="+REDIRECT_URI
	data = { "login_url": login_url }
	return render_to_response("index.html",
				  data,
				  context_instance=RequestContext(request))



def get_code(request):
	code = request.GET['code']
	url = "http://join.agiliq.com/oauth/access_token/"
	pay_load = {"client_id":CLIENT_ID, "client_secret": CLIENT_SECRET, "redirect_uri": REDIRECT_URI, "code": code  }
	response = requests.post(url,data=pay_load)
	result = json.loads(response.text)
	request.session['access_token'] = result['access_token']

	data = {"access_token":request.session['access_token']}

	if result['access_token']:
		return render_to_response("form.html",data,context_instance=RequestContext(request))
	else:
		return HttpResponse ("Invalid Access Token...")





