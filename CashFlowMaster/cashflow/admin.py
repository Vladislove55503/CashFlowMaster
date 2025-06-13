from django.contrib import admin
from .models import (StatusAction, TypeAction, CategoryAction, 
					 SubcategoryAction, Transaction)


admin.site.register(StatusAction)
admin.site.register(TypeAction)
admin.site.register(CategoryAction)
admin.site.register(SubcategoryAction)
admin.site.register(Transaction)