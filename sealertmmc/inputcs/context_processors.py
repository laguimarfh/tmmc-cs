from django.db.models import Count
from . import models


def base_context(request):
    defects = models.Sheet.objects.all().order_by('-id')[:10]
    # coord = models.AjaxImage.objects.all()
    side = models.Sheet.objects.all()[:1]

    return {
        'defects': defects,
        # 'coord' : coord,
        'side' : side,
    }
