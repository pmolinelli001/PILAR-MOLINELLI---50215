from django.shortcuts import render, redirect
from .models import*
from .forms import*
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

#_____________________________HOME

def home(request):
    return render(request,"app/index.html")


def MasInfo(request):
    return render(request,"app/mas_info.html")

def Quienes_somos(request):
    return render(request,"app/quienes_somos.html")


#________________________________ ART

class ArtList(LoginRequiredMixin,ListView):
    model = Art

class ArtCreate(LoginRequiredMixin,CreateView):
    model = Art
    fields = ['profesion_oficio','codigo_postal','matricula','año']
    success_url=reverse_lazy("art")

class ArtUpdate(LoginRequiredMixin,UpdateView):
    model = Art
    fields = ['profesion_oficio','codigo_postal','matricula','año']
    success_url=reverse_lazy("art")


class ArtDelete(LoginRequiredMixin,DeleteView):
    model = Art
    success_url=reverse_lazy("art")


#________________________Tipos de cobertura para ART

def artcob(request):
    dependiente = Dependiente.objects.all()
    independiente = TrabajoIndependiente.objects.all()
    return render(request, 'app/artcob.html', {'dependiente':dependiente, 'independiente': independiente})


#________________________________ AUTO

class AutoList(LoginRequiredMixin,ListView):
    model = Auto

class AutoCreate(LoginRequiredMixin,CreateView):
    model = Auto
    fields = ['marca_del_auto','año','precio','modelo','codigo_postal']
    success_url=reverse_lazy("auto")

class AutoUpdate(LoginRequiredMixin,UpdateView):
    model = Auto
    fields = ['marca_del_auto','año','precio','modelo','codigo_postal']
    success_url=reverse_lazy("auto")


class AutoDelete(LoginRequiredMixin,DeleteView):
    model = Auto
    success_url=reverse_lazy("auto")


#________________________Auto Tipos de Coberturas

def autocob(request):
    todo_riesgo = TodoRiesgo.objects.all()
    cobertura_parcial = CoberturaParcial.objects.all()
    return render(request, 'app/autocob.html', {'todo_riesgo':todo_riesgo, 'cobertura_parcial': cobertura_parcial})


#________________________________ HOGAR

class HogarList(LoginRequiredMixin,ListView):
    model = Hogar

class HogarCreate(LoginRequiredMixin,CreateView):
    model = Hogar
    fields = ['metros_cubiertos','codigo_postal','año','tipo_propiedad']
    success_url=reverse_lazy("hogar")

class HogarUpdate(LoginRequiredMixin,UpdateView):
    model = Hogar
    fields = ['metros_cubiertos','codigo_postal','año','tipo_propiedad']
    success_url=reverse_lazy("hogar")


class HogarDelete(LoginRequiredMixin,DeleteView):
    model = Hogar
    success_url=reverse_lazy("hogar")

def hogarcob(request):
    return render(request, 'app/hogarcob.html')


#_________________________ Eleccion del tipo de propiedad (HOGAR)
@login_required
def consultar_hogar(request):
    if request.method == 'POST':
        tipo_propiedad = request.POST.get('tipo_propiedad')
        if tipo_propiedad == 'Departamento_Dos_Ambientes':
            return redirect('hogarcob1')
        elif tipo_propiedad == 'Casa':
            return redirect('hogarcob4')
        elif tipo_propiedad == 'PH':
            return redirect('hogarcob5')
        elif tipo_propiedad == 'Departamento_Tres_Ambientes':
            return redirect('hogarcob2')
        elif tipo_propiedad == 'Departamento_Cuatro_Ambientes':
            return redirect('hogarcob3')        
    return redirect('home')


#________________________________ VIDA

class VidaList(LoginRequiredMixin,ListView):
    model = Vida

class VidaCreate(LoginRequiredMixin,CreateView):
    model = Vida
    fields = ['nombre','apellido','tipo_documento','numero_doc','numero_celular','correo_electronico','edad']
    success_url=reverse_lazy("vida")

class VidaUpdate(LoginRequiredMixin,UpdateView):
    model = Vida
    fields = ['nombre','apellido','tipo_documento','numero_doc','numero_celular','correo_electronico','edad']
    success_url=reverse_lazy("vida")


class VidaDelete(LoginRequiredMixin,DeleteView):
    model = Vida
    success_url=reverse_lazy("vida")


#________________________Adicionales (VIDA)
@login_required
def vidaresult(request):
    return render(request,"app/vidaresult.html")

#____________________________Login, Logout, Authentication, Registration

def login_request(request):
    if request.method =="POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario,password=clave)        
        if user is not None:
            login(request,user)

            try:
                avatar=Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar ="/media/avatares/default.png"
            finally: 
                request.session["avatar"]=avatar
            return render(request,"app/index.html")
        
        else:
            return redirect (reverse_lazy('login'))

    else:
        miForm=AuthenticationForm()

    return render(request,"app/login.html", {"form":miForm})



def register(request):
    if request.method =="POST":
        miForm=RegistroForm(request.POST)   
        if miForm.is_valid():
            usuario =miForm.cleaned_data.get("username")
            miForm.save()
            return redirect (reverse_lazy('home'))

    else:
        miForm=RegistroForm()

    return render(request,"app/registro.html", {"form":miForm})



#__________________________________ Aviso Suscripcion

def aviso_suscripcion(request):
    return render(request,"app/aviso_suscripcion.html")


#__________________________________ Edicion de Perfil, Contraseña, Avatar

@login_required

def editarPerfil(request):
    usuario=request.user
    if request.method =="POST":
        miForm=UserEditForm(request.POST)
        if miForm.is_valid():
            user=User.objects.get(username=usuario)
            user.email=miForm.cleaned_data.get("email")
            user.first_name=miForm.cleaned_data.get("first_name")
            user.last_name=miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else: 
        miForm=UserEditForm(instance=usuario)

    return render(request,"app/editar_perfil.html", {"form":miForm})




class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name="app/cambiar_clave.html"
    success_url=reverse_lazy('home')


#________________AGREGAR AVATAR

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()

    return render(request, "app/agregarAvatar.html", {"form": miForm} )   

#______________________BUSCAR


def buscarArt(request):
    return render(request, "app/buscar_art.html")


def encontrarArt(request):
    if 'buscar' in request.GET:
        patron = request.GET['buscar']
        print("Parámetro de búsqueda recibido:", patron)
        art_list = Art.objects.filter(profesion_oficio__icontains=patron)
        contexto = {'art_list': art_list}  # Aquí asegúrate de que estás usando 'art' como nombre del contexto
        return render(request, 'app/art_list.html', contexto)
    else:
        art_list=Art.objects.all()
        contexto = {'art_list': art_list}  # También aquí
        return render(request, 'app/art_list.html', contexto)


