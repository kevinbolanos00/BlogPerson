from django.contrib import admin
from django import forms
from home.models import Blog
from home.models import HojaDeVida

# Register your models here.
class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Blog
        fields = "__all__"

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)

from django.forms import FileInput
from django.db import models
from .models import HojaDeVida

class HojaDeVidaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida')
    search_fields = ['titulo']
    readonly_fields = ('fecha_subida',)
    formfield_overrides = {
        models.FileField: {'widget': FileInput(attrs={'accept': 'application/pdf'})},
    }

admin.site.register(HojaDeVida, HojaDeVidaAdmin)