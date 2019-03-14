from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """
    Renders the cart contents page
    """
    return render(request, "cart.html")
 
    
    
def add_to_cart(request, id):
    """
    Add a quantity of the specified event to the cart
    """
    quantity=int(1)
    cart = request.session.get('cart', {})
    
    if id in cart:
        cart[id] += quantity
    else:
        cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified event to the specified amount
    """
    if request.POST.get('quantity') == '':
        request.session['cart'] = request.session.get('cart', {})
        return redirect(reverse('view_cart'))
    else:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
        print(cart)
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    

def adjust_cart_checkout(request, id):
    """
    Allow clients to adjust the cart content during checkout
    """
    if request.POST.get('quantity') == '':
        request.session['cart'] = request.session.get('cart', {})
        return redirect(reverse('checkout'))
    else:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('checkout'))
    