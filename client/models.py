from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=100)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    # def save(self, verbosity=1, *args, **kwargs):
    #     tenant = super().save(verbosity, *args, **kwargs)
    #     domain = Domain()
    #     domain.domain = self.schema_name + '.localhost'
    #     domain.tenant = self
    #     domain.is_primary = True
    #     domain.save()
    #     return tenant

class Domain(DomainMixin):
    pass
