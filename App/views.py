from django.shortcuts import render, redirect
from App.models import JuegosDePc, JuegosDeConsola, Noticias, Avatar
from App.forms import JuegosDePcFormulario, JuegosDeConsolaFormulario, NoticiasFormulario, Userregister, CustomForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .decorators import unauthencated, perfil

#INICIO
@perfil(ins='inicio')
def inicio(request):
    # avatares = Avatar.objects.filter(user=request.user.id)
    #  print(avatares.exists())
    # if request.user.is_authenticated:
    #     if avatares.exists():
    #         av = avatares[0].imagen.url
    #         tr = bool(av)
    #         ex = avatares.exists()
    #         print(bool(av))

    #         return render(request, "App/inicio.html", {"url":av, "true": tr})
    #     else:
    #         return render(request, "App/inicio.html")
    return render(request, "App/inicio.html")

#ABOUT

@login_required
def sobreNosotros(request):
    return render(request, "App/about.html")

#JUEGOS DE PC
@login_required
def juegosPc(request):
    juegosPc = JuegosDePc.objects.all()
    contexto = {"juegosPc": juegosPc}
    return render(request, f"App/juegosPc.html", contexto)

@login_required
def juegosPcFormulario(request):
    
    if request.method == 'POST':
        miFormulario = JuegosDePcFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            juego = JuegosDePc(nombre=informacion['nombre'], fechaDeLanzamiento=informacion['fechaDeLanzamiento'], genero=informacion['genero'], sinopsis=informacion['sinopsis'])
            juego.save()
            return render(request, "App/inicio.html")
    else:
        miFormulario = JuegosDePcFormulario()

    return render(request, "App/juegosPcForm.html", {"miFormulario":miFormulario})

@login_required
def editarJuegosPc(request, juego_nombre):
    
    juegoPc = JuegosDePc.objects.get(nombre=juego_nombre)
    
    if request.method == 'POST':
        
        miFormulario = JuegosDePcFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            juegoPc.nombre = informacion['nombre']
            juegoPc.fechaDeLanzamiento = informacion['fechaDeLanzamiento']
            juegoPc.genero = informacion['genero']
            juegoPc.sinopsis = informacion['sinopsis']
            juegoPc.save()
            return render(request, "App/inicio.html")
    else:
        miFormulario = JuegosDePcFormulario(initial={'nombre': juegoPc.nombre, 'fechaDeLanzamiento': juegoPc.fechaDeLanzamiento, 'genero': juegoPc.genero, 'sinopsis': juegoPc.sinopsis})

    return render(request, "App/editarJuegosPc.html", {"miFormulario":miFormulario, "juego_nombre": juego_nombre})

@login_required
def eliminarJuegosPc(request, juego_nombre):
    
    #Eliminación del objeto
    juegoPc = JuegosDePc.objects.get(nombre=juego_nombre)
    juegoPc.delete()
    
    #Regreso al menú principal
    juegosPc = JuegosDePc.objects.all()
    contexto = {"juegosPc": juegosPc}
    return render(request, "App/juegosPc.html", contexto)

#JUEGOS DE CONSOLA

@login_required
def juegosConsola(request):
    juegosConsola = JuegosDeConsola.objects.all()
    contexto = {"juegosConsola": juegosConsola}
    return render(request, "App/juegosConsola.html", contexto)

@login_required
def juegosConsolaFormulario(request):

    if request.method == 'POST':
        miFormulario = JuegosDeConsolaFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            juego = JuegosDeConsola(nombre=informacion['nombre'], fechaDeLanzamiento=informacion['fechaDeLanzamiento'], genero=informacion['genero'], consola=informacion['consola'], sinopsis=informacion['sinopsis'])
            juego.save()
            return render(request, "App/inicio.html")
    else:
        miFormulario = JuegosDeConsolaFormulario()

    return render(request, "App/juegosConsolaForm.html", {"miFormulario":miFormulario})

@login_required
def editarJuegosConsola(request, juego_nombre):
    
    juegoConsola = JuegosDeConsola.objects.get(nombre=juego_nombre)
    
    if request.method == 'POST':
        
        miFormulario = JuegosDeConsolaFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            juegoConsola.nombre = informacion['nombre']
            juegoConsola.fechaDeLanzamiento = informacion['fechaDeLanzamiento']
            juegoConsola.genero = informacion['genero']
            juegoConsola.consola = informacion['consola']
            juegoConsola.sinopsis = informacion['sinopsis']
            juegoConsola.save()
            return render(request, "App/inicio.html")
    else:
        miFormulario = JuegosDePcFormulario(initial={'nombre': juegoConsola.nombre, 'fechaDeLanzamiento': juegoConsola.fechaDeLanzamiento, 'genero': juegoConsola.genero, 'consola': juegoConsola.consola, 'sinopsis': juegoConsola.sinopsis})

    return render(request, "App/editarJuegosConsola.html", {"miFormulario":miFormulario, "juego_nombre": juego_nombre})

@login_required
def eliminarJuegosConsola(request, juego_nombre):
    
    #Eliminación del objeto
    juegoConsola = JuegosDeConsola.objects.get(nombre=juego_nombre)
    juegoConsola.delete()
    
    #Regreso al menú principal
    juegosConsola = JuegosDeConsola.objects.all()
    contexto = {"juegosConsola": juegosConsola}
    return render(request, "App/juegosConsola.html", contexto)

#NOTICIAS

@login_required
def noticias(request):
    noticias = Noticias.objects.all()
    contexto = {"noticias": noticias}
    return render(request, "App/noticias.html", contexto)

@login_required
def noticiasFormulario(request):

    if request.method == 'POST':
        miFormulario = NoticiasFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            noticia = NoticiasFormulario(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], cuerpo=informacion['cuerpo'])
            noticia.save()
            return render(request, "App/inicio.html")
    else:
        miFormulario = NoticiasFormulario()

    return render(request, "App/noticiasForm.html", {"miFormulario":miFormulario})

@login_required
def editarNoticia(request, noticia_titulo):
    
    noticia = Noticias.objects.get(titulo=noticia_titulo)
    
    if request.method == 'POST':
        
        miFormulario = JuegosDeConsolaFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            noticia.titulo = informacion['titulo']
            noticia.subtitulo = informacion['fechaDeLanzamiento']
            noticia.cuerpo = informacion['genero']
            noticia.save()
            return render(request, "App/inicio.html")
    else:
        miFormulario = Noticias(initial={'titulo': noticia.titulo, 'subtitulo': noticia.subtitulo, 'cuerpo': noticia.cuerpo})

    return render(request, "App/editarNoticias.html", {"miFormulario":miFormulario, "noticia_titulo": noticia_titulo})

@login_required
def eliminarNoticia(request, noticia_titulo):
    
    #Eliminación del objeto
    noticia = Noticias.objects.get(titulo=noticia_titulo)
    noticia.delete()
    
    #Regreso al menú principal
    noticias = Noticias.objects.all()
    contexto = {"noticias": noticias}
    return render(request, "App/noticias.html", contexto)

#BUSQUEDA

@login_required
def busqueda(request):
    return render(request, "App/BuscarJuegoPc.html")

@login_required
def buscar(request):
    if(request.GET["nombre"]):
        nombre = request.GET["nombre"]
        juegosPc = JuegosDePc.objects.filter(nombre__icontains = nombre)
        return render(request, "App/ResultadoBusqueda.html", {"juegos": juegosPc, "nombre": nombre})
    else:
        respuesta = "No enviaste datos :("

    return HttpResponse(respuesta)

# USUARIOS

@unauthencated
def logins(request):
    if request.method == "POST":
        loginfm = AuthenticationForm(request, data=request.POST)
        if loginfm.is_valid():
            user = loginfm.cleaned_data.get('username')
            passw = loginfm.cleaned_data.get('password')

            Pusers = authenticate(username=user, password=passw)

            if Pusers is not  None:
                login(request, Pusers)
                return redirect("/")
            else:
                return render(request, "App/inicio.html", {"mensaje":f"error datos incorrectos"})
        else:
            print('errors')
            return render(request, "App/inicio.html", {"mensaje":f"error formulario erroneo"})
    loginfm = AuthenticationForm()
    return render(request, "App/login.html", {"login":loginfm})    

@unauthencated
def registers(request):

    if request.method == "POST":

        registerfm = Userregister(request.POST)

        if registerfm.is_valid():
            
            user  = registerfm.cleaned_data["username"]
            registerfm.save()
            messages.success(request, "ha sido creado existoso usuario")
            print('exitoso')
            # return render(request, "App/login.html", {"mensaje":"ha sido creado existosa usuario :)"})
            return redirect('/login')
        else:
            print('nada')

    else:
        registerfm = Userregister()
        
    return render(request, "App/register.html", {"register":registerfm})
    
@login_required(login_url='/login')
def logouts(request):
    logout(request)
    return render(request, "App/logout.html")

@login_required(login_url='/login')
def accounts(request):
    user = request.user
    if request.method == 'POST':
        usersfm = CustomForm(request.POST, instance=user)
        if usersfm.is_valid():
            user.save()
            return render(request, 'App/accounts.html')
    else:
        usersfm = CustomForm(initial={'email':user.email,'last_name':user.last_name,'first_name':user.first_name, 'username':user.username})

    return render(request, "App/accounts.html", {"accountsfm":usersfm, "user":user})

def detalleBlog(request):
    return render(request, "App/detalleBlog.html")