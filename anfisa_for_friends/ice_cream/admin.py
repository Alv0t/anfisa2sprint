from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Wrapper, Topping


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',      
    )


# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )  
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

    
admin.site.empty_value_display = 'Не задано'

admin.site.register(Category, CategoryAdmin)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Wrapper)
admin.site.register(Topping)