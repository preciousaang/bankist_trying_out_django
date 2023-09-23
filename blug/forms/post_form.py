from django.forms import ModelForm, Textarea, TextInput
from blug.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        widgets = {
            "title": TextInput(
                attrs={"class": "w-1/4 h-8 text-2xl text-gray-600  ring-0"}
            ),
            "body": Textarea(attrs={"class": "w-1/4 text-gray-600 text-2xl "}),
        }
