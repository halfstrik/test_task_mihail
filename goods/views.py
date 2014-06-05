from django.views import generic
from goods.models import Stuff


class StuffIndexView(generic.ListView):
    template_name = u'goods/stuff_index.html'
    context_object_name = u'stuffs'

    def get_queryset(self):
        return Stuff.objects.all()
