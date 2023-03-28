from django.contrib import admin
from .models import User, Income, Expense, Saving, FuturePlan

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined')

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'description', 'date')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'description', 'date', 'category')

@admin.register(Saving)
class SavingAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'goal', 'target_date')

@admin.register(FuturePlan)
class FuturePlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'estimated_cost', 'target_date')
