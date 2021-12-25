from django.shortcuts import render, HttpResponseRedirect, reverse

from mobilephones import models, forms


# Create your views here.
def indexView(request):
    context = {

    }
    return render(request, 'index.html', context)


def brandsView(request):
    brands = models.Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'brands.html', context)


def productsView(request):
    context = {

    }
    return render(request, 'products.html', context)


def addBrandView(request):
    form = forms.BrandForm
    if request.method == 'POST':
        form = forms.BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mobilephones:brands'))
    context = {
        'title': 'Add Brand',
        'form': form,
    }
    return render(request, 'form.html', context)


def editBrandView(request, id):
    current_brand = models.Brand.objects.get(id=id)
    form = forms.BrandForm(instance=current_brand)
    if request.method == 'POST':
        form = forms.BrandForm(request.POST, instance=current_brand)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mobilephones:brands'))
    context = {
        'title': 'Edit Brand',
        'form': form,
    }
    return render(request, 'form.html', context)


def deleteBrandView(request, id):
    current_brand = models.Brand.objects.get(id=id)
    current_brand.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def addPhoneView(request):
    context = {
        'title': 'Add Phone'
    }
    return render(request, 'form.html', context)


def editPhoneView(request, id):
    context = {
        'title': 'Edit Phone'
    }
    return render(request, 'form.html', context)


def deletePhoneView(request, id):
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
