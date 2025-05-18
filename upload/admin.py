
# Register your models here.
from django.contrib import admin
from upload.models import Upload

class uploadAdmin(admin.ModelAdmin):
    display =("title" ,
"discription",
"art",
"price",)
# Register your models here.
admin.site.register(Upload,uploadAdmin)