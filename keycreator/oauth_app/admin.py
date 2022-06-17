from django.contrib import admin
from .models import Category, LeverKeyModel, PinKeyModel, StandartSizeLeverKey, StandartSizePinKey, ListKey

# Register your models here.

admin.site.register(Category)
admin.site.register(LeverKeyModel)
admin.site.register(PinKeyModel)
admin.site.register(StandartSizeLeverKey)
admin.site.register(StandartSizePinKey)
admin.site.register(ListKey)
