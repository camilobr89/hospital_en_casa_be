from django.contrib import admin
from .models.user import User
from .models.patient import Patient
from .models.nurse import Nurse
from .models.medical import Medical
from .models.history import History


# Register your models here.

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Nurse)
admin.site.register(Medical)
admin.site.register(History)
