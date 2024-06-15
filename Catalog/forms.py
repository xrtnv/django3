from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.forms import ModelForm, forms
from Catalog.models import Product, BlogPost, Version


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("views_counter",)


class BlogPostForm(ModelForm):
    banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = BlogPost
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data["title"]
        if title in self.banned_words:
            raise forms.ValidationError("Используемые слова недопустимы")

    def clean_content(self):
        content = self.cleaned_data["content"]
        if content in self.banned_words:
            raise forms.ValidationError("Используемые слова недопустимы")


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

