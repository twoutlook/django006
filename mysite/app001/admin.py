from django.contrib import admin

# Register your models here.
# from .models import Customer
from .models import Item000
from .models import Item001
from .models import Item002
from .models import Item003
from .models import Item004
from .models import Spec
from .models import Cust

from django.contrib import admin
# admin.site.register(Customer)

class Item000Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6']
admin.site.register(Item000,Item000Admin)


class SpecAdmin(admin.ModelAdmin):
    list_display=['field1','field2']
admin.site.register(Spec,SpecAdmin)

class CustAdmin(admin.ModelAdmin):
    list_display=['field1','field2']
admin.site.register(Cust,CustAdmin)

class Item002Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6','field7']
admin.site.register(Item002,Item002Admin)

class Item004Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6','field7']
admin.site.register(Item004,Item004Admin)

#  r01c2 = models.CharField(default=".",max_length=99,verbose_name="几号机")
#     r01c4 = models.CharField(default=".",max_length=99,verbose_name="吨位")
#     r01c6 = models.CharField(default=".",max_length=99,verbose_name="人员")
#     r01c8 = models.CharField(default=".",max_length=99,verbose_name="日期")
 
class Item001Admin(admin.ModelAdmin):
    fieldsets = [
        ('壓鑄機', {'fields': ['field1',]}),
        ('噸位人員日期', {'fields': [ 'field1a','r01c6','r01c8',], 'classes': ['collapse']}),
        ('結構 - 格林柱', {'fields': ['r03c3','r03c4','r03c5','r03c6','r03c7',], 'classes': ['collapse']}),
        ('結構 - 機架底座', {'fields': ['r04c3','r04c4','r04c5','r04c6','r04c7',], 'classes': ['collapse']}),
        # ('結構', {'fields': [ 'field2a1','field2a2','field2a3','field2a4','field2a5','field2a6',], 'classes': ['collapse']}),
        # ('液壓油', {'fields': [ 'field2b1','field2b2','field2b3','field2b4',], 'classes': ['collapse']}),
        # ('潤滑等', {'fields': [ 'field2c1','field2d1','field2e1','field2f1','field2g1','field2h1',], 'classes': ['collapse']}),
        # ('零件', {'fields': [ 'field3',], 'classes': ['collapse']}),
        # ('進度', {'fields': [ 'field4a','field4b','field4c',], 'classes': ['collapse']}),
    ]

    list_display=[
        'field1', 'field1a','r01c6','r01c8',
        'r03c3','r03c4','r03c5','r03c6','r03c7',
        'r04c3','r04c4','r04c5','r04c6','r04c7',
        
     ]
admin.site.register(Item001,Item001Admin)


class Item003Admin(admin.ModelAdmin):
    fieldsets = [
        ('壓鑄機', {'fields': ['field1', 'field1a',]}),
        ('結構', {'fields': [ 'field2a1','field2a2','field2a3','field2a4','field2a5','field2a6',], 'classes': ['collapse']}),
        ('液壓油', {'fields': [ 'field2b1','field2b2','field2b3','field2b4',], 'classes': ['collapse']}),
        ('潤滑等', {'fields': [ 'field2c1','field2d1','field2e1','field2f1','field2g1','field2h1',], 'classes': ['collapse']}),
        ('零件', {'fields': [ 'field3',], 'classes': ['collapse']}),
        ('進度', {'fields': [ 'field4a','field4b','field4c',], 'classes': ['collapse']}),
    ]

    list_display=[
        'field1', 'field1a',
        'field2a1','field2a2','field2a3','field2a4','field2a5','field2a6',
        'field2b1','field2b2','field2b3','field2b4',
        'field2c1','field2d1','field2e1','field2f1','field2g1','field2h1',
    ]
admin.site.register(Item003,Item003Admin)


# admin.site.register(Item000)


# admin.site.register(Item001)
# admin.site.register(Item002)
# admin.site.register(Item003)
# admin.site.register(Item004)
# admin.site.register(Spec)
