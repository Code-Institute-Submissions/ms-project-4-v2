from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    The function allows users to view items in the bag to be purchased
    and the total amount due for the products selected.
    """
    bag_items = []
    total = 0
    # to access the shopping bag
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
