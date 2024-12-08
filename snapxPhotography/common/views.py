from django.db.models import Count
from django.utils import timezone
from django.views.generic import ListView
from snapxPhotography.contests.models import Contest


# Create your views here.
class IndexView(ListView):
    model = Contest
    template_name = 'common/index.html'

    def get_queryset(self):
        queryset = Contest.objects.annotate(count_photos=Count('photo')).filter(deadline__lt=timezone.now().date()).order_by('-count_photos')[:10]
        return queryset
