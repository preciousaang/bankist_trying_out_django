from django.forms import ModelForm, Textarea, TextInput
from blug.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "w-1/4 shadow-lg resize-none h-8 text-lg p-2 text-gray-600"
                },
            ),
            "body": Textarea(
                attrs={
                    "class": "w-1/4 shadow-lg resize-none text-gray-600 text-lg p-2 "
                }
            ),
        }
