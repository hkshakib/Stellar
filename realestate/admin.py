from django.contrib import admin
from .models import RealEstate


class RealEstateAdmin(admin.ModelAdmin):
    """
    Only Id, Name, Email and hired date will be visible on Admin panel
    Admin can click on Id and name and go to the required pages link.
    admin can search via a name
    every page can show upto 25 products at a time
    """
    list_display = ('id', 'name', 'email', 'date_hired')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(RealEstate, RealEstateAdmin)
