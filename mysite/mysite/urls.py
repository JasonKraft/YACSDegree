from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^register/$', 'member.views.MemberRegistration'),
    (r'^login/$', 'member.views.LoginRequest'),
    (r^'logout/$', 'member.views.LogoutRequest'),
)
