from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to return the bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to the shopping bag"""

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
    print(request.session['bag'])
    return redirect(redirect_url)
