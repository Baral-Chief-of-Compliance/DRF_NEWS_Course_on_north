from django.contrib import admin
from news.models import News
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class NewsClassForm(forms.ModelForm):
    textNews = forms.CharField(label="Содержиомое новости", widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsClassAdmin(admin.ModelAdmin):
    list_display = ("title", "datePublished")
    list_filter = ("datePublished",)
    search_fields = ("title",)
    form = NewsClassForm
    save_on_top = True
    save_as = True


admin.site.register(News, NewsClassAdmin)