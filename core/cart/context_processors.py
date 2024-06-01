from .cart import CartMain

def cart_processor(request):
    cart = CartMain(request)
    return {"cart": cart}
