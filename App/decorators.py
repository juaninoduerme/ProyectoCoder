from django.http import HttpResponse
from django.shortcuts import redirect, render
from App.models import  Avatar

def unauthencated(view_func):
    def wrapp(request, *a, **b):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *a, **b)
    return wrapp

# sirve para mostrar tu perfil de usuario 
def perfil(ins='inicio'):
    def decorator(view_func):
        def wrapp(request, index=ins):
            avatares = Avatar.objects.filter(user=request.user.id)
            if request.user.is_authenticated:
                if avatares.exists():
                    av = avatares[0].imagen.url
                    tr = bool(av)
                    print(bool(av))
                    return render(request, f"App/{index}.html", {"url":av, "true": tr})
                else:
                    return render(request, f"App/{index}.html")
                    
            return view_func(request)
        return wrapp
    return decorator