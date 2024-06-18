from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.forms import ModelForm
from Catalog.models import Product, Version


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("views_counter",)


class VersionFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('product', css_class='form-control'),
            Field('version_number', css_class='form-control'),
            Field('version_name', css_class='form-control'),
            Field('is_current', css_class='form-check-input'),
            Submit('submit', 'Save', css_class='btn btn-primary')
        )


class VersionForm(ModelForm, VersionFormMixin):
    class Meta:
        model = Version
        fields = "__all__"
