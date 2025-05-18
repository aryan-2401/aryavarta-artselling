from django.contrib import admin
from .models import Commission

class CommissionAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "phone",
        "medium",
        "price",
        "image",
"customization"
,
        "is_booked",
    )
    
admin.site.register(Commission, CommissionAdmin)
