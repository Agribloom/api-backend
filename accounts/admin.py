#  * This file is part of recharge-me project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Transaction
from .admin_actions import export_as_csv_action


class ActiveInvestment(admin.SimpleListFilter):
    title = 'active investment'
    parameter_name = 'active_investment'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.annotate(
                user_investments=Count('investment')
            ).filter(
                user_investments__gt=0
            )
        elif value == 'No':
            return queryset.annotate(
                user_investments=Count('investment')
            ).filter(
                user_investments=0
            )
        return queryset


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        'get_username_or_fullname',
        'email', 'phone_number',
        'has_active_investement'
    ]
    list_filter = [
        ActiveInvestment,
        'date_joined',
        'last_login',
        'is_active',
        'is_staff',
    ]
    actions = [
        export_as_csv_action("CSV Export", fields=[
            'username',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'bank_name',
            'account_name',
            'account_number'
        ])
    ]
    search_fields = ['username', 'email', 'phone_number']
    fieldsets = UserAdmin.fieldsets + (
        ('KYC', {'fields': ('phone_number', 'gender', 'date_of_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('KYC', {'fields': ('phone_number', 'gender', 'date_of_birth')}),
    )

    def has_active_investement(self, obj):
        return obj.investment_set.count() > 0
    has_active_investement.boolean = True

    model = CustomUser


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = ['owner', 'amount', 'status', 'transaction_type']
    list_filter = ['status', 'transaction_type']
    search_fields = [
        'owner__username',
        'owner__first_name',
        'owner__last_name'
    ]
    raw_id_fields = ['owner']
