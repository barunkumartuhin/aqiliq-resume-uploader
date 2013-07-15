from django.conf.urls import patterns, include, url

urlpatterns = patterns('resume.views',
	

	url(r'^$', 'login', name='login'),
    
    url(r'^get-code$', 'get_code', name='get_code'),

    url(r'^upload-resume/$', 'upload', name='upload'),


)
