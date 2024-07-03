from django import forms
from django.forms import ModelForm
from catalog.models import Product, Version


class ProductForm(ModelForm):
    """Пользователи могут создавать новые продукты"""

    class Meta:
        model = Product
        #fields = "__all__"
        exclude = ('owner',)

    def except_words_from_text(self, field_name, error_text):

        excepted_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        cleaned_data = self.cleaned_data.get(field_name)

        for word in excepted_words:
            if word in cleaned_data:
                raise forms.ValidationError(error_text + f': ("{word}")')

        return cleaned_data

    def clean_name(self):
        return self.except_words_from_text(
            "name", "Ошибка, связанная с названием Продукта"
        )

    def clean_description(self):
        return self.except_words_from_text(
            "description", "Ошибка, связанная с описанием Продукта"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


#            field.help_text = 'Раз, два, три! Ура!'  # Выводит текст подсказки, для описания вводимых данных


class VersionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

    #            field.help_text = 'Раз, два, три! Ура!'  # Выводит текст подсказки, для описания вводимых данных

    class Meta:
        model = Version  # Обязательно указываем модель
        fields = "__all__"  # и перечисляем поля для отображения
