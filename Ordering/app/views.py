from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .models import Customer, Order, OrderItem, Delivery
from .forms import CustomerForm, ItemForm, OrderForm, OrderItemForm, DeliveryForm

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return redirect('home')

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', '/home/')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def add_order(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        item_form = ItemForm(request.POST)
        order_form = OrderForm(request.POST)
        order_item_form = OrderItemForm(request.POST)
        delivery_form = DeliveryForm(request.POST)

        if all([
            customer_form.is_valid(), 
            item_form.is_valid(), 
            order_form.is_valid(),
            order_item_form.is_valid(), 
            delivery_form.is_valid()
        ]):
            customer = customer_form.save()
            item = item_form.save()
            order = order_form.save(commit=False)
            order.customer = customer
            order.save()

            order_item = order_item_form.save(commit=False)
            order_item.order = order
            order_item.item = item
            order_item.save()

            delivery = delivery_form.save(commit=False)
            delivery.order = order
            delivery.save()

            return redirect('records')
        else:
            print("Form Errors:", customer_form.errors, item_form.errors, order_form.errors)
    else:
        customer_form = CustomerForm()
        item_form = ItemForm()
        order_form = OrderForm()
        order_item_form = OrderItemForm()
        delivery_form = DeliveryForm()

    return render(request, 'add_order.html', {
        'customer_form': customer_form,
        'item_form': item_form,
        'order_form': order_form,
        'order_item_form': order_item_form,
        'delivery_form': delivery_form,
    })
@login_required
def records(request):
    orders = Order.objects.select_related('customer').prefetch_related('items')
    return render(request, 'records.html', {'orders': orders})
@login_required
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, instance=order.customer)
        order_form = OrderForm(request.POST, instance=order)
        order_item_form = OrderItemForm(request.POST, instance=order.items.first())
        delivery_form = DeliveryForm(request.POST, instance=order.delivery_set.first())

        if all([
            customer_form.is_valid(), 
            order_form.is_valid(), 
            order_item_form.is_valid(), 
            delivery_form.is_valid()
        ]):
            customer_form.save()
            order_form.save()
            order_item_form.save()
            delivery_form.save()
            return redirect('records')
    else:
        customer_form = CustomerForm(instance=order.customer)
        order_form = OrderForm(instance=order)
        order_item_form = OrderItemForm(instance=order.items.first())
        delivery_form = DeliveryForm(instance=order.delivery_set.first())

    return render(request, 'edit_order.html', {
        'order': order,
        'customer_form': customer_form,
        'order_form': order_form,
        'order_item_form': order_item_form,
        'delivery_form': delivery_form,
    })

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('records')

    return render(request, 'delete_order.html', {'order': order})

def order_list(request):
    search_query = request.GET.get('search', '')
    orders = Order.objects.all()

    if search_query:
        orders = orders.filter(
            Q(id__icontains=search_query) | 
            Q(customer__name__icontains=search_query) |
            Q(customer__age__icontains=search_query) |
            Q(customer__address__icontains=search_query) |
            Q(customer__phone__icontains=search_query)
        )

    return render(request, 'records.html', {'orders': orders})
