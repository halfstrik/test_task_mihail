import simplejson as json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from goods.models import Stuff, Property


def home_view(request):
    return render_to_response('index.html')


def get_stuff_view(request):
    result = []
    for stuff in get_stuff(request.GET.get('amount', None), request.GET.get('property_value', None)):
        item = {'name': stuff.name, 'description': stuff.description, 'price': stuff.price,
                'imageUrl': stuff.image.url}
        try:
            item['property'] = stuff.property.value
        except Property.DoesNotExist:
            item['property'] = None
        result.append(item)

    return HttpResponse(json.dumps(result, use_decimal=True))


def get_stuff(amount, property_value):
    manager = Stuff.objects
    if property_value is not None:
        manager = manager.filter(property__value=property_value)
    return list(manager.all()[:amount])


def get_property_values_view(request):
    result = []
    for prop in get_properties():
        result.append(prop.value)
    return HttpResponse(json.dumps(result))


def get_properties():
    return list(Property.objects.all())
