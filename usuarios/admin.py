from django.contrib import admin
from .models import Usuario
# Register your models here.

admin.site.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    search_field = ('nome', 'email')
    readonly_fields = ('senha',)