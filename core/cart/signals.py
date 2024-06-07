from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from .cart import CartMain

@receiver(user_logged_in)
def post_login(sender, user, request, **kwargs):
    
    cart = CartMain(request)
    cart.sync_cart_items_from_db(user)


@receiver(user_logged_out)
def pre_logout(sender, user, request, **kwargs):
    print('hi in out')
    cart = CartMain(request)
    cart.merge_session_cart_in_db(user)