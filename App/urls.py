from django.urls import path
from App import views
urlpatterns = [
    #INICIO
    path('', views.inicio, name="Inicio"),
    path('detalleBlog', views.detalleBlog, name="detalleBlog"),
    #ABOUT
    path('about', views.sobreNosotros, name="SobreNosotros"),
    #JUEGOS PC
    path('JuegosPc', views.juegosPc, name="JuegosPc"),
    path('JuegosPcForm', views.juegosPcFormulario, name="JuegosPcFormulario"),
    path('EliminarJuegosPc/<juego_nombre>/', views.eliminarJuegosPc, name="EliminarJuegosPc"),
    path('EditarJuegosPc/<juego_nombre>/', views.editarJuegosPc, name="EditarJuegosPc"),
    #JUEGOS CONSOLA
    path('JuegosConsola', views.juegosConsola, name="JuegosConsola"),
    path('juegosConsolaForm', views.juegosConsolaFormulario, name="JuegosConsolaFormulario"),
    path('EliminarJuegosConsola/<juego_nombre>/', views.eliminarJuegosConsola, name="EliminarJuegosConsola"),
    path('EditarJuegosConsola/<juego_nombre>/', views.editarJuegosConsola, name="EditarJuegosConsola"),
    #NOTICIAS
    path('Noticias', views.noticias, name="Noticias"),
    path('EliminarNoticias/<noticia_titulo>/', views.eliminarNoticia, name="EliminarNoticias"),
    path('noticiasForm', views.noticiasFormulario, name="NoticiasFormulario"),
    path('EditarNoticias/<noticia_titulo>/', views.editarNoticia, name="EditarNoticias"),
    #BÚSQUEDA
    path('Busqueda', views.busqueda, name="BusquedaJuegosPc"),
    path('Buscar', views.buscar),
    #LOGIN
    path('login', views.logins, name='Login'),
    path('registrar', views.registers, name='Registrar'),
    path('logout', views.logouts, name='Logout'),
    path('Cuenta', views.accounts, name='Accounts'),
]