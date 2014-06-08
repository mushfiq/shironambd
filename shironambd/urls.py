from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shironambd.views.home', name='home'),
    # url(r'^shironambd/', include('shironambd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	
    url(r'^about-us', 'shironambd.home.views.aboutus'),
    url(r'^contact-us', 'shironambd.home.views.contactus'),
    url(r'legal', 'shironambd.home.views.legal'),
    url(r'', 'shironambd.home.views.index')
    
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()