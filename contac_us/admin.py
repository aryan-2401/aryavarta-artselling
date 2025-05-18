from django.contrib import admin
from .models import Contact

class contactAdmin(admin.ModelAdmin):
    display = (
        'email',
        'phone',
        'state',
        'city',
        'address',
     
    )
admin.site.register(Contact,contactAdmin)
