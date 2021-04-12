from django.db import models
from django.utils.timezone import now
# Create your models here.
# modelo de usuarios de django, contendra todos los usuarios registrados en el panel de administrador
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name ="categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=200, verbose_name="Titulo")

    content = models.TextField(verbose_name="Contenido")
    # utilizamos timezone para establecer la hora por defecto en el campo publiched
    published = models.DateTimeField(verbose_name="fecha de publicacion", default= now)

    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)

    # compos relacionados
   
   # el autor lo importaremos del modelo de django user
   # pasandole como primer argumento User, enlazamos a los usuarios como si fueran autores de cada entrada
   # la alternativa a usar cascada y que se borrer todas las entradas asociadas es usasr protect, pero si usas protect deja el campo como null true y blank true
    author = models.ForeignKey(User,verbose_name="Autor", on_delete=models.CASCADE)

    # podremos crear campos manualmente desde el administrador con esto
    # related_name, nos permite cambiar el nombre de la relacion, por defecto seria post_set
    categories = models.ManyToManyField(Category, verbose_name="Categorias",related_name="get_post")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name ="entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title




