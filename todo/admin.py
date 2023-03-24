from django.contrib import admin
from .models import Contact
# Register your models here.
class ItemView(admin.ModelAdmin):
    list_display=['id','name','email','phone']
admin.site.register(Contact,ItemView)

