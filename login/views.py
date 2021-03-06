from django.views.generic.base import TemplateView
from lti_provider.mixins import LTIAuthMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


class IndexView(TemplateView):
    template_name = 'index.html'


class LTIAssignment1View(LTIAuthMixin, LoginRequiredMixin, TemplateView):

    template_name = 'assignment.html'

    def get_context_data(self, **kwargs):
        print self, kwargs
        return {
            'is_student': self.lti.lis_result_sourcedid(self.request),
            'course_title': self.lti.course_title(self.request),
            'number': 1
        }


class LTIAssignment2View(LTIAuthMixin, LoginRequiredMixin, TemplateView):

    template_name = 'assignment.html'

    def get_context_data(self, **kwargs):
        return {
            'is_student': self.lti.lis_result_sourcedid(self.request),
            'course_title': self.lti.course_title(self.request),
            'number': 2
        }