from django import forms


class BaseForm(forms.ModelForm):
    DEFAULT_INPUT_CLASS = "input-field pl-10"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.setdefault("class", self.DEFAULT_INPUT_CLASS)
