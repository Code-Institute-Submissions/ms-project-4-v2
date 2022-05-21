from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ A view to return the checkout page """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L1sCdJrZt59IP2KMILh8Wr2TsCGuriGspBbzeD2BBlzyjdQ44UKyZwxzqvrjVhVZQEdQsIltkLthfn4mHEtVR8Z00IXJM2YHD',
        'client_secret': 'sk_test_51L1sCdJrZt59IP2KLiQLlNmc7cLhD2RBG3X3Oe5Rx2UOETeZulpic2IWUjReZ38HcwoDRxhdIvwhmU37jAt9X2HW00avw1HHBQ',
    }

    return render(request, template, context)
