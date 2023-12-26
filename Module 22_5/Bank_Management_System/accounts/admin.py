from django.contrib import admin
from . models import UserBankAccount, UserAddress
# Register your models here.
# admin.site.register(UserBankAccount)
# admin.site.register(UserAddress)


class UserBankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_type', 'account_number',
                    'birthdate', 'gender', 'initial_deposit_date', 'balance')
    search_fields = ['user__username', 'account_number']


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'city', 'postal_code', 'country')
    search_fields = ['user__username', 'street_address',
                     'city', 'postal_code', 'country']


admin.site.register(UserBankAccount, UserBankAccountAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
