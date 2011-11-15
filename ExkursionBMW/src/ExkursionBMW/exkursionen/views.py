from django.template import Context, loader
from exkursionen.models import Exkursion
from django.http import HttpResponse

def liste(request):
    exkurse = Exkursion.objects.all().order_by('id')

    t = loader.get_template('liste.tpl')
    c = Context({
        'exkurse': exkurse
    })
    return HttpResponse(t.render(c))
