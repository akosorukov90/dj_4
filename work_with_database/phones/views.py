from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = []
    sort = request.GET.get("sort", "id")
    if sort == 'name':
        for phone in Phone.objects.all().order_by('name'):
            name = phone.name
            price = phone.price
            image = phone.image
            slug = phone.slug
            phones.append({'name': name, 'price': price, 'image': image, 'slug': slug})
        context = {'phones': phones}
        return render(request, template, context)
    elif sort == 'price_min':
        for phone in Phone.objects.all().order_by('price'):
            name = phone.name
            price = phone.price
            image = phone.image
            slug = phone.slug
            phones.append({'name': name, 'price': price, 'image': image, 'slug': slug})
        context = {'phones': phones}
        return render(request, template, context)
    elif sort == 'price_max':
        for phone in Phone.objects.all().order_by('-price'):
            name = phone.name
            price = phone.price
            image = phone.image
            slug = phone.slug
            phones.append({'name': name, 'price': price, 'image': image, 'slug': slug})
        context = {'phones': phones}
        return render(request, template, context)
    else:
        for phone in Phone.objects.all():
            name = phone.name
            price = phone.price
            image = phone.image
            slug = phone.slug
            phones.append({'name': name, 'price': price, 'image': image, 'slug': slug})
        context = {'phones': phones}
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = []
    phone = Phone.objects.get(slug=slug)
    name = phone.name
    price = phone.price
    image = phone.image
    r_date = phone.release_date
    release_date = r_date.strftime("%d.%m.%Y")
    lte_exists = phone.lte_exists
    phones.append({'name': name, 'price': price, 'release_date': release_date, 'lte_exist': lte_exists, 'image': image})
    context = {'phones': phones}
    return render(request, template, context)
