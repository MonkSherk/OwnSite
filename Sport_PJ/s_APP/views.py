from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Store, Product, Category

# List views
def store_list(request):
    stores = Store.objects.all()
    return render(request, 's_APP/store_list.html', {'stores': stores})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 's_APP/category_list.html', {'categories': categories})

# Detail views
def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    products = Product.objects.filter(store=store)
    return render(request, 's_APP/store_detail.html', {'store': store, 'products': products})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 's_APP/category_detail.html', {'category': category, 'products': products})

# Create views
def add_store(request):
    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES['image']
        description = request.POST['description']
        Store.objects.create(name=name, image=image, description=description)
        return redirect('store_list')
    return render(request, 's_APP/store_form.html')

# Update views
def edit_store(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        store.name = request.POST['name']
        if 'image' in request.FILES:
            store.image = request.FILES['image']
        store.description = request.POST['description']
        store.save()
        return redirect('store_detail', pk=pk)
    return render(request, 's_APP/store_form.html', {'store': store})

# Delete views
def delete_store(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == "POST":
        store.delete()
        return redirect('store_list')
    return render(request, 's_APP/store_confirm_delete.html', {'store': store})
