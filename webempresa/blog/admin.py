from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')
    # nos permite mostrar columnas
    list_display =('title', 'author', 'published','post_categories',)
    # pendiente si queremos ordenar por un elemento, debemos colocar la coma, para que django entienda que es una tupla ('elemento',)
    ordering = ('author', 'published')

    # si queremos buscar por author debemos usar la doble barra baja y el atributo o campo
    # los campos manytomany no se pueden mostrar por columna de forma tradicional
    search_fields = ('title','content','author__username','categories__name')

    # para filtrar por fecha
    date_hierarchy = 'published'

    # normalmente los campos de filtrado son relaciones, cosas que se repiten
    
    list_filter =('author__username','categories__name')

    # creacion de campos propios

    def post_categories(self, obj):
        # esto genera una cadena de caracteres con todas las categorias separadas  por comas
        return ",".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, PostAdmin)


