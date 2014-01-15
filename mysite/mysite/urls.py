from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

from mysite.views import current_datetime, hours_ahead

urlpatterns = patterns('',
		(r'^time/$', current_datetime),
		(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# from django.conf.urls import patterns, url, include
# from mysite.views import current_datetime

# urlpatterns = patterns('', 
# 		(r'^time/$', current_datetime),
# 	)
