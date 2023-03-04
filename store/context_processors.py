from .models import variation_list
from carts.views import Variation



def variants(request):
    variant = Variation.objects.all()
    return dict(variant = variant)