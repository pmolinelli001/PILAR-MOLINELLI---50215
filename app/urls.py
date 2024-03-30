
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
#_____________________________HOME
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('quienes_somos/', Quienes_somos, name="quienes_somos"),
    path('mas_info/', MasInfo, name="mas_info"),



#______________________________AUTO

    path('auto/',AutoList.as_view(), name="auto"),
    path('autoCreate/',AutoCreate.as_view(), name="autoCreate"),
    path('autoUpdate/<int:pk>/',AutoUpdate.as_view(), name="autoUpdate"),
    path('autoDelete/<int:pk>/',AutoDelete.as_view(), name="autoDelete"),
    path('autocob/',autocob, name="autocob"),


#______________________________VIDA 

    path('vida/',VidaList.as_view(), name="vida"),
    path('vidaresult/',vidaresult, name="vidaresult"),    
    path('vidaCreate/',VidaCreate.as_view(), name="vidaCreate"),
    path('vidaUpdate/<int:pk>/',VidaUpdate.as_view(), name="vidaUpdate"),
    path('vidaDelete/<int:pk>/',VidaDelete.as_view(), name="vidaDelete"),

#______________________________HOGAR 

    path('hogar/',HogarList.as_view(), name="hogar"),
    path('hogarCreate/',HogarCreate.as_view(), name="hogarCreate"),
    path('hogarUpdate/<int:pk>/',HogarUpdate.as_view(), name="hogarUpdate"),
    path('hogarDelete/<int:pk>/',HogarDelete.as_view(), name="hogarDelete"),
    path('hogarcob/',hogarcob, name="hogarcob"),
#______________________________ART 

    path('art/',ArtList.as_view(), name="art"),
    path('artCreate/',ArtCreate.as_view(), name="artCreate"),
    path('artUpdate/<int:pk>/',ArtUpdate.as_view(), name="artUpdate"),
    path('artDelete/<int:pk>/',ArtDelete.as_view(), name="artDelete"),
    path('artcob/',artcob, name="artcob"),

#______________________________Login, Logout,Registration

    path('login/',login_request, name="login"),
    path('logout/',LogoutView.as_view(template_name="app/logout.html"), name="logout"),
    path('aviso_suscripcion/',aviso_suscripcion, name="aviso_suscripcion"),    
    path('registro/',register, name="registro"),

#______________________________Editar Perfil
    path('perfil/',editarPerfil, name="perfil"),

#_______________________________Cambiar clave
    path('<int:pk>/password/',CambiarClave.as_view(), name="cambiar_clave"),

#_________________________________AVATAR
    path('agregar_avatar/',agregarAvatar, name="agregar_avatar"),


#____________________ Busqueda
    path('buscar_art/', buscarArt, name="buscar_art"),
    path('encontrar_art/', encontrarArt, name="encontrar_art")
]



