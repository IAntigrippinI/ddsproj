from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.TransactionListView.as_view(), name="transaction_list"),
    path(
        "transaction/create/",
        views.TransactionCreateView.as_view(),
        name="transaction_create",
    ),
    path(
        "transaction/<uuid:pk>/edit/",
        views.TransactionUpdateView.as_view(),
        name="transaction_edit",
    ),
    path(
        "transaction/<uuid:pk>/delete/",
        views.TransactionDeleteView.as_view(),
        name="transaction_delete",
    ),
    path(
        "transaction-types/",
        views.TransactionTypeListView.as_view(),
        name="transaction_type_list",
    ),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "category/create/", views.CategoryCreateView.as_view(), name="category_create"
    ),
    path(
        "category/<int:pk>/edit/",
        views.CategoryUpdateView.as_view(),
        name="category_edit",
    ),
    path(
        "category/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path(
        "subcategories/", views.SubCategoryListView.as_view(), name="subcategory_list"
    ),
    path(
        "subcategory/create/",
        views.SubCategoryCreateView.as_view(),
        name="subcategory_create",
    ),
    path(
        "subcategory/<int:pk>/edit/",
        views.SubCategoryUpdateView.as_view(),
        name="subcategory_edit",
    ),
    path(
        "subcategory/<int:pk>/delete/",
        views.SubCategoryDeleteView.as_view(),
        name="subcategory_delete",
    ),
    path("statuses/", views.StatusListView.as_view(), name="status_list"),
    path("status/create/", views.StatusCreateView.as_view(), name="status_create"),
    path("status/<int:pk>/edit/", views.StatusUpdateView.as_view(), name="status_edit"),
    path(
        "status/<int:pk>/delete/",
        views.StatusDeleteView.as_view(),
        name="status_delete",
    ),
    path(
        "transaction-type/create/",
        views.TransactionTypeCreateView.as_view(),
        name="transaction_type_create",
    ),
    path(
        "transaction-type/<int:pk>/edit/",
        views.TransactionTypeUpdateView.as_view(),
        name="transaction_type_edit",
    ),
    path(
        "transaction-type/<int:pk>/delete/",
        views.TransactionTypeDeleteView.as_view(),
        name="transaction_type_delete",
    ),
]
