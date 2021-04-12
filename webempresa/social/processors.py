# extenderemos el contexto
from .models import Link

def ctx_dict(request):
    # queremos que la variable test pueda ser usada en cualquier template
    ctx = {}
    
    links = Link.objects.all()
    
    for link in links:
        ctx[link.key] = link.url


    return ctx