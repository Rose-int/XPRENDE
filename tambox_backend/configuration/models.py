from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    auto_create_schema = True

    def __str__(self):
        return self.name
# Create your models here.
