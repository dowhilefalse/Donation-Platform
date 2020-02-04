from django.contrib import admin

# Register your models here.
from .models import Organization, OrganizationContact, OrganizationDemand, Team, TeamContact
from .cache_helper import clear_by_prefix

class OrganizationContactInlineAdmin(admin.StackedInline):
    model = OrganizationContact
    extra = 0 # 去掉空行
    readonly_fields = ('add_time',)
    can_delete = True # 让Organization关联的Contact可以移除
    # exclude = ['add_time',] # 不出现的字段

class OrganizationDemandInlineAdmin(admin.StackedInline):
    model = OrganizationDemand
    extra = 0
    readonly_fields = ('add_time',)
    can_delete = True

class OrganizationAdmin(admin.ModelAdmin):
    """docstring for OrganizationAdmin"""
    list_display = ['province', 'city', 'name', 'address', 'source', 'verified', 'add_time',]
    readonly_fields = ['add_time',]
    inlines = (OrganizationContactInlineAdmin, OrganizationDemandInlineAdmin,)

    def save_model(self, request, obj, form, change):
        # print(form.changed_data)
        super(OrganizationAdmin, self).save_model(request, obj, form, change)
        clear_by_prefix('organization')

admin.site.register(Organization, OrganizationAdmin)

# -----------------------------------------------------------------------------------------

class TeamContactInlineAdmin(admin.StackedInline):
    model = TeamContact
    extra = 0
    readonly_fields = ('add_time',)
    can_delete = True

class TeamAdmin(admin.ModelAdmin):
    """docstring for OrganizationAdmin"""
    list_display = ['name', 'address', 'verified', 'add_time',]
    readonly_fields = ['add_time',]
    inlines = (TeamContactInlineAdmin,)

    def save_model(self, request, obj, form, change):
        # print(form.changed_data)
        super(TeamAdmin, self).save_model(request, obj, form, change)
        clear_by_prefix('team')

admin.site.register(Team, TeamAdmin)
