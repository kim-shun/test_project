from django.views import generic
#from .models import Test
from test_app.serveces import testService
#from .forms import InquiryForm

class IndexView(generic.ListView):
  #test_lists = testService.testsService
  #model = Test
  template_name = "index.html"
  #form_class = InquiryForm

  def get_queryset(self):
    tests = testService.testsService
    return tests
  # def get_queryset(self):
  #   tests = Test.objects.all().order_by('-created_at')
  #   return tests