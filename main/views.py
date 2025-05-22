from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Transaction, TransactionType, Status, Category, SubCategory
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import datetime


# Create your views here.
def transaction_list(request):
    transactions = Transaction.objects.all()

    return render(request, "main/transaction/list.html", {"transactions": transactions})


class TransactionListView(ListView):
    model = Transaction
    template_name = "main/transaction/list.html"
    context_object_name = "transactions"
    ordering = ["-transaction_date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")
        category_id = self.request.GET.get("category")
        subcategory_id = self.request.GET.get("subcategory")
        transaction_type_id = self.request.GET.get("transaction_type")
        status_id = self.request.GET.get("status")

        if start_date:
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                queryset = queryset.filter(transaction_date__gte=start_date)
            except ValueError:
                pass

        if end_date:
            try:
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
                queryset = queryset.filter(transaction_date__lte=end_date)
            except ValueError:
                pass

        if category_id:
            queryset = queryset.filter(category__category_id=category_id)

        if subcategory_id:
            queryset = queryset.filter(category_id=subcategory_id)

        if transaction_type_id:
            queryset = queryset.filter(transaction_type_id=transaction_type_id)

        if status_id:
            queryset = queryset.filter(status_id=status_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["start_date"] = self.request.GET.get("start_date", "")
        context["end_date"] = self.request.GET.get("end_date", "")
        context["categories"] = Category.objects.all()
        context["subcategories"] = SubCategory.objects.all()
        context["transaction_types"] = TransactionType.objects.all()
        context["statuses"] = Status.objects.all()
        context["selected_category"] = self.request.GET.get("category", "")
        context["selected_subcategory"] = self.request.GET.get("subcategory", "")
        context["selected_transaction_type"] = self.request.GET.get(
            "transaction_type", ""
        )
        context["selected_status"] = self.request.GET.get("status", "")
        return context


class TransactionCreateView(CreateView):
    model = Transaction
    template_name = "main/transaction/form.html"
    fields = [
        "amount",
        "description",
        "status",
        "transaction_type",
        "category",
        "transaction_date",
    ]
    success_url = reverse_lazy("main:transaction_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить транзакцию"
        return context


class TransactionUpdateView(UpdateView):
    model = Transaction
    template_name = "main/transaction/form.html"
    fields = [
        "amount",
        "description",
        "status",
        "transaction_type",
        "category",
        "transaction_date",
    ]
    success_url = reverse_lazy("main:transaction_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать транзакцию"
        return context


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = "main/transaction/confirm_delete.html"
    success_url = reverse_lazy("main:transaction_list")


class TransactionTypeListView(ListView):
    model = TransactionType
    template_name = "main/transaction_type/list.html"
    context_object_name = "types"


# Category views
class CategoryListView(ListView):
    model = Category
    template_name = "main/category/list.html"
    context_object_name = "categories"


class CategoryCreateView(CreateView):
    model = Category
    template_name = "main/category/form.html"
    fields = ["name", "description"]
    success_url = reverse_lazy("main:category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить категорию"
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "main/category/form.html"
    fields = ["name", "description"]
    success_url = reverse_lazy("main:category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать категорию"
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "main/category/confirm_delete.html"
    success_url = reverse_lazy("main:category_list")


# SubCategory views
class SubCategoryListView(ListView):
    model = SubCategory
    template_name = "main/subcategory/list.html"
    context_object_name = "subcategories"


class SubCategoryCreateView(CreateView):
    model = SubCategory
    template_name = "main/subcategory/form.html"
    fields = ["name", "description", "category"]
    success_url = reverse_lazy("main:subcategory_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить подкатегорию"
        return context


class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    template_name = "main/subcategory/form.html"
    fields = ["name", "description", "category"]
    success_url = reverse_lazy("main:subcategory_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать подкатегорию"
        return context


class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = "main/subcategory/confirm_delete.html"
    success_url = reverse_lazy("main:subcategory_list")


# Status views
class StatusListView(ListView):
    model = Status
    template_name = "main/status/list.html"
    context_object_name = "statuses"


class StatusCreateView(CreateView):
    model = Status
    template_name = "main/status/form.html"
    fields = ["name"]
    success_url = reverse_lazy("main:status_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить статус"
        return context


class StatusUpdateView(UpdateView):
    model = Status
    template_name = "main/status/form.html"
    fields = ["name"]
    success_url = reverse_lazy("main:status_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать статус"
        return context


class StatusDeleteView(DeleteView):
    model = Status
    template_name = "main/status/confirm_delete.html"
    success_url = reverse_lazy("main:status_list")


# TransactionType views
class TransactionTypeCreateView(CreateView):
    model = TransactionType
    template_name = "main/transaction_type/form.html"
    fields = ["name"]
    success_url = reverse_lazy("main:transaction_type_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Добавить тип транзакции"
        return context


class TransactionTypeUpdateView(UpdateView):
    model = TransactionType
    template_name = "main/transaction_type/form.html"
    fields = ["name"]
    success_url = reverse_lazy("main:transaction_type_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактировать тип транзакции"
        return context


class TransactionTypeDeleteView(DeleteView):
    model = TransactionType
    template_name = "main/transaction_type/confirm_delete.html"
    success_url = reverse_lazy("main:transaction_type_list")
