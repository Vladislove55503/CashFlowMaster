from django import forms 
import django_filters

from .models import (Transaction, StatusAction, TypeAction, 
                     CategoryAction, SubcategoryAction)


class TransactFilter(django_filters.FilterSet):
    """
    Фильтр для транзакций, предоставляющий возможность фильтрации 
    по диапазону дат, статусу, типу, категории и подкатегории транзакций.
    
    Фильтры связаны между собой: 
        выбор типа действия обновляет доступные категории, 
        а выбор категории - доступные подкатегории.
    
    Attributes:
    -----------
    date_created: DateFromToRangeFilter
        Фильтр по диапазону дат создания транзакции
    status_act: ModelChoiceFilter
        Фильтр по статусу действия
    type_act: ModelChoiceFilter
        Фильтр по типу действия
    category_act: ModelChoiceFilter
        Фильтр по категории действия
    subcategory_act: ModelChoiceFilter
        Фильтр по подкатегории действия
    """

    date_created = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(attrs={
                                'type': 'date',
                                'class': 'form-control w-auto m-0 me-2 b-0',
                                })
    )
    status_act = django_filters.ModelChoiceFilter(
        queryset=StatusAction.objects.all(),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();',
                                   'class': 'form-select m-0'})
    )
    type_act = django_filters.ModelChoiceFilter(
        queryset=TypeAction.objects.all(),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();',
                                   'class': 'form-select m-0',
                                   })
    )
    category_act = django_filters.ModelChoiceFilter(
        queryset=CategoryAction.objects.none(),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();',
                                   'class': 'form-select m-0',
                                   })
    )
    subcategory_act = django_filters.ModelChoiceFilter(
        queryset=SubcategoryAction.objects.none(),
        widget=forms.Select(attrs={'onchange': 'this.form.submit();',
                                   'class': 'form-select m-0',
                                   })
    )

    class Meta:
        model = Transaction
        fields = ['date_created', 'status_act', 'type_act', 
                  'category_act', 'subcategory_act',]
                  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'type_act' in self.data:
            try:
                type_act_id = int(self.data.get('type_act'))
                self.filters['category_act'].queryset = (
                    CategoryAction.objects.filter(type_act_id=type_act_id)
                    )
            except Exception as e:
                print(e)

        if 'category_act' in self.data:
            try:
                category_act_id = int(self.data.get('category_act'))
                self.filters['subcategory_act'].queryset = (
                    SubcategoryAction.objects.filter(
                                            category_act_id=category_act_id)
                    )
            except Exception as e:
                print(e)