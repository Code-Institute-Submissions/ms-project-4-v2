from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_bag(request):
    """ A view to return the bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Function to add product to the shopping bag.
    Creates session variable which contains all the items the user
    adds to bag.
    """

    quantity = int(request.POST.get('quantity'))
    # where to redirect the user once an item is added to bag
    redirect_url = request.POST.get('redirect_url')

    # Code Institute Boutique Ado project
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Update the quantity of the specified product. """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove specified product from the shopping bag. """

    bag = request.session.get('bag', {})

    bag.pop(item_id)

    request.session['bag'] = bag
    return HttpResponse(status=200)
