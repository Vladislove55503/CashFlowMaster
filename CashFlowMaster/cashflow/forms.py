from datetime import date

from django import forms
from .models import (Transaction, StatusAction, TypeAction, 
                     CategoryAction, SubcategoryAction)


class TransactCreateUpdateForm(forms.ModelForm):
    """Форма для создания и обновления транзакции.
    
    Содержит поля для заполнения всех атрибутов модели Transaction.
    
    Attributes:
    -----------
    date_created: DateField
        Поле для выбора даты создания транзакции 
        с предустановленным значением текущей даты
    """

    date_created = forms.DateField(
                            initial=date.today(), 
                            widget=forms.SelectDateWidget(
                                years=range(1949, date.today().year + 1),
                                ))

    class Meta:
        model = Transaction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TransactCreateUpdateForm, self).__init__(*args, **kwargs)
        self.fields['date_created'].widget.attrs.update({
                                        'class': 'form-select w-auto me-2'})
        self.fields['status_act'].widget.attrs.update({
                                        'class': 'form-select'})
        self.fields['type_act'].widget.attrs.update({
                                        'class': 'form-select'})
        self.fields['category_act'].widget.attrs.update({
                                        'class': 'form-select'})
        self.fields['subcategory_act'].widget.attrs.update({
                                        'class': 'form-select'})
        self.fields['amount'].widget.attrs.update({
                                        'class': 'form-control'})
        self.fields['comment'].widget.attrs.update({
                                        'class': 'form-control'})


class StatusActionForm(forms.ModelForm):
    """Форма для создания и обновления объекта модели StatusAction.
    
    Attributes:
    -----------
    name: CharField
        Поле для ввода названия
    """

    class Meta:
        model = StatusAction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StatusActionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
                                        'class': 'form-control mt-3'})


class TypeActionForm(forms.ModelForm):
    """Форма для создания и обновления объекта модели TypeAction.
    
    Attributes:
    -----------
    name: CharField
        Поле для ввода названия
    """

    class Meta:
        model = TypeAction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TypeActionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
                                        'class': 'form-control mt-3'})


class CategoryActionForm(forms.ModelForm):
    """Форма для создания и обновления объекта модели CategoryAction.
    
    Содержит поля для заполнения всех атрибутов модели CategoryAction.

    Attributes:
    -----------
    type_act: ModelChoiceField
        Поле для выбора связи с объектом TypeAction
    name: CharField
        Поле для ввода названия
    """

    class Meta:
        model = CategoryAction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryActionForm, self).__init__(*args, **kwargs)
        self.fields['type_act'].widget.attrs.update({
                                        'class': 'form-select'})
        self.fields['name'].widget.attrs.update({
                                        'class': 'form-control mt-3'})


class SubcategoryActionForm(forms.ModelForm):
    """Форма для создания и обновления объекта модели SubcategoryAction.
    
    Содержит поля для заполнения всех атрибутов модели SubcategoryAction.

    Attributes:
    -----------
    category_act: ModelChoiceField
        Поле для выбора связи с объектом CategoryAction
    name: CharField
        Поле для ввода названия
    """

    class Meta:
        model = SubcategoryAction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SubcategoryActionForm, self).__init__(*args, **kwargs)
        self.fields['category_act'].widget.attrs.update({
                                        'class': 'form-select'})
        self.fields['name'].widget.attrs.update({
                                        'class': 'form-control mt-3'})