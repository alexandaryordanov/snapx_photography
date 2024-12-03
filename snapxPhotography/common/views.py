from django.utils import timezone
from django.views.generic import ListView

from snapxPhotography.contests.models import Contest


# Create your views here.
class IndexView(ListView):
    model = Contest
    template_name = 'common/index.html'

    def get_queryset(self):
        return Contest.objects.filter(deadline__lt=timezone.now().date())[:10]
