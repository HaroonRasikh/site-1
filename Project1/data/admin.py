from django.contrib import admin

from Xidmetler.models import title,service1,service2,service3,service4
from . models import *
from Anasahifa.models import home,description,Selector,Social
from Komanda.models import Komanda,Chart
from iş.models import Ugur,hesabat,Manager
from Anlayışlar.models import Maqala,Result,Members
from django.contrib.auth.models import Group
admin.site.unregister(Group)
#admin.site.unregister(User)
# Register your models here.
#admin.site.register(About)
#dmin.site.register(service1)
#admin.site.register(service2)
#admin.site.register(service3)


@admin.register(home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title','description','status','image']
    list_editable = ['description','status','image']
    list_display_links = ['title']
    search_fields = ['title',]
@admin.register(Selector)
class SelectorAdmin(admin.ModelAdmin):
    list_display = ['title','logo1','logo2','logo3','logo4','logo5','logo6','logo7']
    list_editable = ['logo1','logo2','logo3','logo4','logo5','logo6','logo7']
    search_fields = ['title',]
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['facebook','instagram','linkedin','whatsapp']
    list_editable =['instagram','linkedin','whatsapp']

@admin.register(description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['id','sentence']
    list_editable = ['sentence']
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name','about','image']
    list_editable = ['about','image']
    

@admin.register(about1)
class About1Admin(admin.ModelAdmin):
    list_display = ['name','slug','image','facebook','instagram','twitter']
    list_editable =['slug','image','facebook','instagram','twitter']
    search_fields = ['name','slug']

@admin.register(title)
class servictitleAdmin(admin.ModelAdmin):
    list_display = ['id','name','description']
    list_editable = ['name','description']
    search_fields = ['name','description']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(service1)
class Service1Admin(admin.ModelAdmin):
    list_display = ['name','image','about']
    list_editable = ['image','about']
    search_fields = ['name']

@admin.register(service2)
class Service2Admin(admin.ModelAdmin):
    list_display = ['subject','description']
    list_editable = ['description']
    search_fields = ['subject']


    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(service3)
class Service3Admin(admin.ModelAdmin):
    list_display = ['id','subject','description']
    list_editable = ['description']
    search_fields = ['subject']
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(service4)
class Service4Admin(admin.ModelAdmin):
    list_display = ['id','subject','description']
    list_editable = ['description']
    search_fields = ['subject']

@admin.register(Ugur)
class UgurAdmin(admin.ModelAdmin):
        list_display = ['name','title1','title2','description1','image','description2','file','facebook',
    'twitter','linkedin','date']
        list_editable = ['title1','title2','description1','image','description2','file','facebook',
    'twitter','linkedin']
        search_fields = ['title1','title2','description1']
@admin.register(hesabat)
class HesabatAdmin(admin.ModelAdmin):
    list_display = ['name','title1','title2','description1','image','description2','file','facebook',
    'twitter','linkedin','date']
    list_editable = ['title1','title2','description1','image','description2','file','facebook',
    'twitter','linkedin']
    search_fields = ['title1','title2','description1']

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['name','image','description']
    list_editable = ['image','description']
    search_fields = ['name','description']



@admin.register(Maqala)
class MaqalaAdmin(admin.ModelAdmin):
    list_display = ['name','image','description','date']
    list_editable = ['image','description']
    search_fields = ['name','description']

@admin.register(Result)
class ResultkAdmin(admin.ModelAdmin):
    list_display = ['name','image','description','date']
    list_editable = ['image','description']
    search_fields = ['name','description']



@admin.register(Members)
class AgreemnetAdmin(admin.ModelAdmin):
    list_display = ['name','image','description']
    list_editable = ['image','description']
    search_fields = ['name','description']



@admin.register(Komanda)
class KomandaAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    list_editable = ['description']
    search_fields = ['title','description']

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display=['title1','title2','description','facebook','twitter','linkedin']
    list_editable = ['title2','description','facebook','twitter','linkedin']
    search_fields = ['title1','title2','description']