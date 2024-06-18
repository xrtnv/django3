from blog.models import BlogPost
from django.forms import ModelForm, forms


class BlogPostForm(ModelForm):
    banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

    class Meta:
        model = BlogPost
        fields = ("title", "content", "preview_image", "is_published")

    def clean_title(self):
        title = self.cleaned_data["title"]
        if title in self.banned_words:
            raise forms.ValidationError("Используемые слова недопустимы")
        return title

    def clean_content(self):
        content = self.cleaned_data["content"]
        if content in self.banned_words:
            raise forms.ValidationError("Используемые слова недопустимы")
        return content
