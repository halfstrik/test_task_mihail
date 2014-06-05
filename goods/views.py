import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from goods.models import Stuff, Property


def home_view(request):
    return render_to_response('index.html')


def get_stuff_view(request):
    result = []
    for stuff in get_stuff(request.GET.get('amount', None), None):
        item = {'name': stuff.name, 'description': stuff.description}
        try:
            item['property'] = stuff.property.value
        except Property.DoesNotExist:
            item['property'] = None
        result.append(item)

    return HttpResponse(json.dumps(result))


def get_stuff(amount, property_name):
    return list(Stuff.objects.all()[:amount])
