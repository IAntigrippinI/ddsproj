from django.db import models
from django.utils import timezone
import uuid


class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Transaction(models.Model):
    transaction_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(
        Status, related_name="transactions", on_delete=models.CASCADE
    )
    transaction_type = models.ForeignKey(
        TransactionType, related_name="transactions", on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        SubCategory, related_name="transactions", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-transaction_date",)
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return f"{self.amount} - {self.transaction_type.name} ({self.transaction_date.strftime('%Y-%m-%d')})"
