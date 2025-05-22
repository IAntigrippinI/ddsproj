from django.contrib import admin

# Register your models here.
from .models import Category, SubCategory, Status, Transaction, TransactionType


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "description"]
    search_fields = ["name", "description", "category__name"]
    list_filter = ["category"]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        "transaction_id",
        "amount",
        "transaction_type",
        "status",
        "category",
        "category_id",
        "description",
        "transaction_date",
        "created_at",
    ]
    list_display_links = [
        "transaction_id",
    ]
    list_editable = [
        "amount",
        "transaction_type",
        "status",
        "category",
        "category_id",
        "description",
        "transaction_date",
    ]
    list_filter = [
        "status",
        "transaction_type",
        "category",
        "category_id",
        "transaction_date",
    ]
    search_fields = ["transaction_id", "description", "amount"]
    readonly_fields = ["transaction_id", "created_at"]
