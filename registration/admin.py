from django.contrib import admin

# Register your models here.
# from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(BaseUserAdmin):
   # The forms to add and change user instances
   form = UserAdminChangeForm
   add_form = UserAdminCreationForm

   # The fields to be used in displaying the User model.
   # These override the definitions on the base UserAdmin
   # that reference specific fields on auth.User.
   list_display = ('username', 'phone', 'is_superuser',)
   list_filter = ('is_superuser',)
   fieldsets = (
       (None, {'fields': ('password',)}),
       ('Personal info', {'fields': ('username', 'phone',)}),
       ('Permissions', {'fields': ('is_staff', 'is_superuser',)}),
   )
   # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
   # overrides get_fieldsets to use this attribute when creating a user.
   add_fieldsets = (
       (None, {
           'classes': ('wide',),
           'fields': ('username', 'phone', 'password1', 'password2')}
       ),
   )
   search_fields = ('username', 'phone',)
   ordering = ('username', 'phone',)
   filter_horizontal = ()

admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)
