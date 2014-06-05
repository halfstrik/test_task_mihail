from django.views import generic
from goods.models import Stuff


class StuffIndexView(generic.ListView):
    template_name = 'goods/stuff_index.html'
    context_object_name = 'stuffs'

    def get_queryset(self):
        return Stuff.objects.all()
