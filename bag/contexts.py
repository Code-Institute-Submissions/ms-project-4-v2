from django.conf import settings


def bag_contents(request):
    """
    The function allows users to view items in the bag to be purchased
    and the total amount due for the products selected.
    """
    bag_items = []
    total = 0

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context
