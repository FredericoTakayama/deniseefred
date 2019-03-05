from django.contrib import admin

# Register your models here.
from mainsite.models import Guest

# admin.site.register(Guest)

# @admin.register
class GuestAdmin(admin.ModelAdmin):
    # definicao da tabela
    list_display = ('id', 'name', 'last_name', 'has_presence', 'family_quantity', 'num_of_babies', 'num_of_children')
    # cria uma lista do lado
    # list_filter = ('has_presence', 'last_update')
    list_filter = ['has_presence']
    # organização dos campos
    fields = [
            # ('id'),
            ('name', 'last_name',),
            ('gender', 'has_presence', 'is_vip', 'main_inviter', 'invited_by'),
            'address',
            ('max_family_quantity', 'family_quantity'),
            ('num_of_babies', 'num_of_children'),        
    ]

admin.site.register(Guest, GuestAdmin)