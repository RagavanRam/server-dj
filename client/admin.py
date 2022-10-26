from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from client.models import Client

# Register your models here.

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'schema_name')

        def has_add_permission(self, request) -> bool:
                return False
