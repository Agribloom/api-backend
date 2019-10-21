#  * This file is part of recharge-me project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Transaction


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['get_username_or_fullname', 'email', 'phone_number']
    list_filter = ['date_joined', 'last_login', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'phone_number']
    fieldsets = UserAdmin.fieldsets + (
        ('KYC', {'fields': ('phone_number', 'gender', 'date_of_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('KYC', {'fields': ('phone_number', 'gender', 'date_of_birth')}),
    )
    
    model = CustomUser

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    
    list_display = ['owner', 'amount', 'status', 'transaction_type']
    list_filter = ['status', 'transaction_type']
    search_fields = ['owner__username', 'owner__first_name', 'owner__last_name']
    raw_id_fields = ['owner']
