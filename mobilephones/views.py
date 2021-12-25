from django.shortcuts import render, HttpResponseRedirect, reverse

from mobilephones import models, forms


# Create your views here.
def indexView(request):
    phones = models.Phone.objects.all()
    context = {
        'phones': phones,
    }
    return render(request, 'index.html', context)


def brandsView(request):
    brands = models.Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'brands.html', context)


def phonesView(request):
    phones = models.Phone.objects.all()
    context = {
        'phones': phones,
    }
    return render(request, 'phones.html', context)


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
    form = forms.PhoneForm
    if request.method == 'POST':
        form = forms.PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mobilephones:phones'))
    context = {
        'title': 'Add Phone',
        'form': form,
    }
    return render(request, 'form.html', context)


def editPhoneView(request, id):
    current_phone = models.Phone.objects.get(id=id)
    form = forms.PhoneForm(instance=current_phone)
    if request.method == 'POST':
        form = forms.PhoneForm(data=request.POST, files=request.FILES, instance=current_phone)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mobilephones:phones'))

    context = {
        'title': 'Edit Phone',
        'form': form,
    }
    return render(request, 'form.html', context)


def deletePhoneView(request, id):
    current_phone = models.Phone.objects.get(id=id)
    current_phone.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
