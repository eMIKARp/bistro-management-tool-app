from django.contrib import admin
from BistroManagementToolApp.models import *

# Register your models here.

admin.site.register(IngredientAisle)
admin.site.register(IngredientCategory)
admin.site.register(IngredientSubcategory)
admin.site.register(Ingredient)
admin.site.register(IngredientsInProduct)
admin.site.register(ProductGroup)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Transaction)
admin.site.register(ProductsInTransaction)
admin.site.register(ApplicationUser)
admin.site.register(WorkScheadule)
