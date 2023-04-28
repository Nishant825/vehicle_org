from django.contrib import admin
from .models  import *



@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(SubOrganisation)
class SubOrganisationAdmin(admin.ModelAdmin):
    list_display = ['id','sub_name','org_name']

@admin.register(SubOrganisationData)
class SubOrganisationDataAdmin(admin.ModelAdmin):
    list_display = ['id','sub_name','sub_org_name']


# admin.site.register(Organisation)
# admin.site.register(SubOrganisation)
# admin.site.register(SubOrganisationData)