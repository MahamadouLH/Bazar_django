from .models import  Cart, CartItem
from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist as DoesNotExist


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id = _cart_id(request))
            authenticate = request.user.is_authenticated
            if authenticate:
                cart_items = CartItem.objects.all().filter(user = request.user)
            else:
                cart_items = CartItem.objects.all().filter(cart = cart[:1])
            
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except DoesNotExist:
            cart_count = 0
    return dict(cart_count = cart_count)