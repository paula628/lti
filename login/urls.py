from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    #url(r'^$', xframe_options_exempt(TemplateView.as_view(template_name='home.html')), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^lti/', include('lti_provider.urls')),
    url(r'^$', views.IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^assignment/1/', views.LTIAssignment1View.as_view()),
    url(r'^assignment/2/', views.LTIAssignment2View.as_view()),
    url(r'^assignment/success', TemplateView.as_view(
        template_name='main/assignment_success.html'),
        name='assignment-success')
]
