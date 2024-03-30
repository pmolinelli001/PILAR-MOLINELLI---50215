from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Auto(models.Model):
    marca_del_auto= models.CharField(max_length=40)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=50, decimal_places=2)
    modelo = models.CharField(max_length=20)
    codigo_postal = models.CharField(max_length=7)
    def __str__(self):
        return f"{self.marca_del_auto}"
    class Meta: 
        verbose_name = "Auto"
        verbose_name_plural ="Auto"
        ordering = ["marca_del_auto"]
    
class TodoRiesgo(models.Model):
    precio=models.DecimalField(max_digits=50,decimal_places=2)
    responsabilidad_civil = models.CharField(max_length=10)
    reposicion_0km = models.CharField(max_length=10)
    daño_incendio_robototal =models.CharField(max_length=10)
    daño_parcial_por_robo =models.CharField(max_length=10)
    cerraduras=models.CharField(max_length=10)
    cristales_laterales=models.CharField(max_length=10)
    daños_por_granizo=models.CharField(max_length=10)

class CoberturaParcial(models.Model):
    precio=models.DecimalField(max_digits=50,decimal_places=2)
    responsabilidad_civil = models.CharField(max_length=10)
    reposicion_0km = models.CharField(max_length=10)
    daño_incendio_robototal =models.CharField(max_length=10)
    daño_parcial_por_robo =models.CharField(max_length=10)
    cerraduras=models.CharField(max_length=10)
    cristales_laterales=models.CharField(max_length=10)
    daños_por_granizo=models.CharField(max_length=10,)


class Hogar(models.Model):
    metros_cubiertos = models.DecimalField(max_digits=10,decimal_places=2)
    codigo_postal = models.CharField(max_length=10)
    año = models.IntegerField()
    opciones_propiedad=(
        ('Departamento_Dos_Ambientes','Departamento_Dos_Ambientes'),
        ('Casa','Casa'),
        ('PH','PH'),
        ('Departamento_Tres_Ambientes','Departamento_Tres_Ambientes'),
        ('Departamento_Cuatro_Ambientes','Departamento_Cuatro_Ambientes')
    )
    tipo_propiedad=models.CharField(max_length=30, choices=opciones_propiedad)
    def __str__(self):
        return f"{self.tipo_propiedad}"
    class Meta: 
        verbose_name = "Hogar"
        verbose_name_plural ="Hogar"
        ordering = ["tipo_propiedad"]



class Departamento_Cuatro_Ambientes(models.Model):
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=100)
    incendio = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    catastrofe_natural =models.DecimalField(max_digits=20,decimal_places=2,default=1500000)
    reposicion_de_electrodomesticos= models.DecimalField(max_digits=20,decimal_places=2,default=250000)
    robo= models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    daños_vivienda = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)

class Casa(models.Model):
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=100)
    incendio = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    catastrofe_natural =models.DecimalField(max_digits=20,decimal_places=2,default=1500000)
    reposicion_de_electrodomesticos= models.DecimalField(max_digits=20,decimal_places=2,default=250000)
    robo= models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    daños_vivienda = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)

class Ph(models.Model):
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=100)
    incendio = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    catastrofe_natural =models.DecimalField(max_digits=20,decimal_places=2,default=1500000)
    reposicion_de_electrodomesticos= models.DecimalField(max_digits=20,decimal_places=2,default=250000)
    robo= models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    daños_vivienda = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)

class Departamento_Tres_Ambientes(models.Model):
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=100)
    incendio = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    catastrofe_natural =models.DecimalField(max_digits=20,decimal_places=2,default=1500000)
    reposicion_de_electrodomesticos= models.DecimalField(max_digits=20,decimal_places=2,default=250000)
    robo= models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    daños_vivienda = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)

class Departamento_Dos_Ambientes(models.Model):
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=100)
    incendio = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    catastrofe_natural =models.DecimalField(max_digits=20,decimal_places=2,default=1500000)
    reposicion_de_electrodomesticos= models.DecimalField(max_digits=20,decimal_places=2,default=250000)
    robo= models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    daños_vivienda = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)

class Departamento_Un_Ambientes(models.Model):
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=101)
    incendio = models.DecimalField(max_digits=20,decimal_places=2,default=2500)
    catastrofe_natural =models.DecimalField(max_digits=20,decimal_places=2,default=2500)
    reposicion_de_electrodomesticos= models.DecimalField(max_digits=20,decimal_places=2,default=2000)
    robo= models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    daños_vivienda = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)

   

class Art(models.Model):
    profesion_oficio = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=7)
    matricula = models.CharField(max_length=40, default='')
    año = models.IntegerField()
    def __str__(self):
        return f"{self.profesion_oficio}"
    
    class Meta: 
        verbose_name = "Art"
        verbose_name_plural ="Art"
        ordering = ["profesion_oficio"]

class TrabajoIndependiente(models.Model):
    precio = models.DecimalField(max_digits=3,decimal_places=2,default=510)
    muerte_accidental = models.DecimalField(max_digits=8,decimal_places=2,default=1500000)
    invalidez_parcial_total_permanente =models.DecimalField(max_digits=10,decimal_places=2,default=1000000)
    gastos_asistencia_medica = models.DecimalField(max_digits=15,decimal_places=2,default=150000)

class Dependiente(models.Model):
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=1000)
    muerte_accidental = models.DecimalField(max_digits=20,decimal_places=2,default=2500000)
    invalidez_parcial_total_permanente =models.DecimalField(max_digits=20,decimal_places=2,default=1500000)
    gastos_asistencia_medica = models.DecimalField(max_digits=20,decimal_places=2,default=250000)

class Vida(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    opciones_documento = (
        ('Documento Nacional de Identidad','Documento Nacional de Identidad'),
        ('Libreta Civica','Libreta Civica'),
        ('Libreta de Enrolamiento','Libreta de Enrolamiento'),
        ('CUIT','CUIT')
    )
    tipo_documento = models.CharField(max_length=40,choices=opciones_documento)
    numero_doc = models.IntegerField(20)
    numero_celular = models.IntegerField(15)
    correo_electronico = models.EmailField(max_length=40)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class Meta: 
        verbose_name = "Vida"
        verbose_name_plural ="Vida"
        ordering = ["nombre"]
    edad = models.IntegerField(default=0)


class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatares")
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} {self.imagen}"

