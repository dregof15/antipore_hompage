from django.shortcuts import render
from .models import Customer

# Create your views here.


def index(request):
    # return render(request, 'pybo/starbuckskorea.html')
    return render(request, 'pybo/starbuckskorea.html')

# def index(request):
#     customer_list = Customer.objects.order_by('-name')
#     context = {'customer_list': customer_list}
#     return render(request, 'pybo/customer_list.html', context)


def detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    return render(request, 'pybo/customer_detail.html', context)


def location_page(request):
    return render(request, 'pybo/location_page.html')


def loading_page(request):
    return render(request, 'pybo/loading_page.html')
