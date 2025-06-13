from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import (CreateView, UpdateView, TemplateView, 
                                  ListView, DeleteView)
from django.urls import reverse_lazy

from django_filters.views import FilterView

from .models import (Transaction, StatusAction, TypeAction, 
                     CategoryAction, SubcategoryAction)
from .filters import TransactFilter
from .forms import (TransactCreateUpdateForm, StatusActionForm, TypeActionForm, 
                    CategoryActionForm, SubcategoryActionForm)


class MainView(FilterView):
    """Представление для главной страницы.

    Предоставляет список транзакций с возможностью фильтрации по дате, 
    статусу, типу, категории и подкатегории. 
    Сортирует по убыванию даты в date_created.

    Представление использует TransactFilter для фильтрации данных 
    и оптимизирует запросы через предварительную загрузку связанных объектов.

    Attributes:
    ----------
    model: Transaction
        Модель, с которой работает представление
    template_name: str
        Путь к шаблону для отображения списка транзакций
    filterset_class: TransactFilter
        Класс фильтра, используемый для фильтрации данных
    """

    model = Transaction
    template_name = 'cashflow/main.html' 
    filterset_class = TransactFilter

    def get_queryset(self):
        return (super().get_queryset()
                       .order_by('-date_created')
                       .select_related('status_act', 'type_act', 
                                       'category_act', 'subcategory_act',))


class ReferenceManage(TemplateView):
    """Представление для управления справочниками.
    
    Предоставляет доступ к справочникам:
    - Статусы транзакций
    - Типы транзакций
    - Категории транзакций
    - Подкатегории транзакций

    Attributes:
    ----------
    template_name: str
        Шаблон для отображения страницы управления справочниками.
    
    Methods:
    -------
    get_context_data(**kwargs)
        Переопределён для динамического изменения контекстных данных. 
        Загружает все необходимые справочники в контекст шаблона
        для их отображения и управления.
    """

    template_name = 'cashflow/reference_manage.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_act_qs'] = StatusAction.objects.all()
        context['type_act_qs'] = TypeAction.objects.all()
        context['category_act_qs'] = CategoryAction.objects.all()
        context['subcategory_act_qs'] = SubcategoryAction.objects.all()
        return context


# Transaction

class TransactCreateView(CreateView):
    """Представление для создания транзакции."""
    model = Transaction
    form_class = TransactCreateUpdateForm
    template_name = 'cashflow/transaction/create_transact.html'
    success_url = reverse_lazy('cashflow:main')


class TransactDetailView(DetailView):
    """Представление для отображения полей транзакции."""
    model = Transaction
    template_name = 'cashflow/transaction/detail_transact.html'
    context_object_name = 'obj'


class TransactUpdateView(UpdateView):
    """Представление для обновления транзакции."""
    model = Transaction
    form_class = TransactCreateUpdateForm
    template_name = 'cashflow/transaction/update_transact.html'
    success_url = reverse_lazy('cashflow:main')


class TransactDeleteView(DeleteView):
    """Представление для удаления транзакции."""
    model = Transaction
    context_object_name = 'obj'
    template_name = 'cashflow/transaction/delete_transact.html'
    success_url = reverse_lazy('cashflow:main')


# StatusAction

class StatusActionCreateView(CreateView):
    """Представление для создания статуса транзакций."""
    model = StatusAction
    form_class = StatusActionForm
    template_name = 'cashflow/generic/create_model_action.html'
    extra_context = {'obj_name': 'статус'}
    success_url = reverse_lazy('cashflow:reference_manage')


class StatusActionUpdateView(UpdateView):
    """Представление для обновления статуса транзакций."""
    model = StatusAction
    form_class = StatusActionForm
    template_name = 'cashflow/generic/update_model_action.html'
    extra_context = {'obj_name': 'статус'}
    success_url = reverse_lazy('cashflow:reference_manage')


class StatusActionDeleteView(DeleteView):
    """Представление для удаления статуса транзакций."""
    model = StatusAction
    context_object_name = 'obj'
    template_name = 'cashflow/generic/delete_model_action.html'
    extra_context = {'obj_name': 'статус'}
    success_url = reverse_lazy('cashflow:reference_manage')


# TypeAction

class TypeActionCreateView(CreateView):
    """Представление для создания типа транзакций."""
    model = TypeAction
    form_class = TypeActionForm
    template_name = 'cashflow/generic/create_model_action.html'
    extra_context = {'obj_name': 'тип'}
    success_url = reverse_lazy('cashflow:reference_manage')


class TypeActionUpdateView(UpdateView):
    """Представление для обновления типа транзакций."""
    model = TypeAction
    form_class = TypeActionForm
    template_name = 'cashflow/generic/update_model_action.html'
    extra_context = {'obj_name': 'тип'}
    success_url = reverse_lazy('cashflow:reference_manage')


class TypeActionDeleteView(DeleteView):
    """Представление для удаления типа транзакций."""
    model = TypeAction
    context_object_name = 'obj'
    template_name = 'cashflow/generic/delete_model_action.html'
    extra_context = {'obj_name': 'тип'}
    success_url = reverse_lazy('cashflow:reference_manage')


# CategoryAction

class CategoryActionCreateView(CreateView):
    """Представление для создания категории транзакций."""
    model = CategoryAction
    form_class = CategoryActionForm
    template_name = 'cashflow/generic/create_model_action.html'
    extra_context = {'obj_name': 'категория'}
    success_url = reverse_lazy('cashflow:reference_manage')


class CategoryActionUpdateView(UpdateView):
    """Представление для обновления категории транзакций."""
    model = CategoryAction
    form_class = CategoryActionForm
    template_name = 'cashflow/generic/update_model_action.html'
    extra_context = {'obj_name': 'категория'}
    success_url = reverse_lazy('cashflow:reference_manage')


class CategoryActionDeleteView(DeleteView):
    """Представление для удаления категории транзакций."""
    model = CategoryAction
    context_object_name = 'obj'
    template_name = 'cashflow/generic/delete_model_action.html'
    extra_context = {'obj_name': 'категория'}
    success_url = reverse_lazy('cashflow:reference_manage')


# SubcategoryAction

class SubcategoryActionCreateView(CreateView):
    """Представление для создания подкатегории транзакций."""
    model = SubcategoryAction
    form_class = SubcategoryActionForm
    template_name = 'cashflow/generic/create_model_action.html'
    extra_context = {'obj_name': 'подкатегория'}
    success_url = reverse_lazy('cashflow:reference_manage')


class SubcategoryActionUpdateView(UpdateView):
    """Представление для обновления подкатегории транзакций."""
    model = SubcategoryAction
    form_class = SubcategoryActionForm
    template_name = 'cashflow/generic/update_model_action.html'
    extra_context = {'obj_name': 'подкатегория'}
    success_url = reverse_lazy('cashflow:reference_manage')


class SubcategoryActionDeleteView(DeleteView):
    """Представление для удаления подкатегории транзакций."""
    model = SubcategoryAction
    context_object_name = 'obj'
    template_name = 'cashflow/generic/delete_model_action.html'
    extra_context = {'obj_name': 'подкатегория'}
    success_url = reverse_lazy('cashflow:reference_manage')