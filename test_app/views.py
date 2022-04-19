from django.views import generic
from .models import Test

class IndexView(generic.ListView):
  model = Test
  template_name = "index.html"

  def get_queryset(self):
    tests = Test.objects.all().order_by('-created_at')
    return tests