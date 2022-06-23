from django.contrib import admin
from main.models import Category5, Product, Contact11, Subcribe,OrderData, Order, Categories


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','img','price']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message','sent_at']

    # list_filter = ['sent_at']

    # search_fields =  ['email','number_of_telephone','message','sent_at']

    # list_editable = ['number_of_telephone']

class SubcribeAdmin(admin.ModelAdmin):
    list_display = ['email','sent_at']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','product','price','count','total_sum']


class OrderDataAdmin(admin.ModelAdmin):
    list_display = ['name','number','email','address','message']


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name','img']



admin.site.register(Category5, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact11, ContactAdmin)
admin.site.register(Subcribe, SubcribeAdmin)
admin.site.register(OrderData, OrderDataAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Categories, CategoriesAdmin)