from django.forms.widgets import SplitDateTimeWidget


class FormMixins:
    """
    A mixin for Django forms to apply placeholders and autocomplete="off"
    using the `placeholders` dictionary in the form's Meta class.

    Special handling for SplitDateTimeWidget (separate date and time placeholders).
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attr_autocomplete()
        self.attr_placeholder()

    def attr_autocomplete(self):
        for field in self.fields.values():
            field.widget.attrs.setdefault("autocomplete", "off")

    def attr_placeholder(self):
        placeholders = getattr(self.Meta, "placeholders", {})

        for field, placeholder in placeholders.items():
            field = self.fields[field]
            widget = field.widget

            if isinstance(widget, SplitDateTimeWidget):
                if isinstance(placeholder, (list, tuple)) and len(placeholder) == 2:
                    date_widget, time_widget = widget.widgets
                    date_widget.attrs.setdefault("placeholder", placeholder[0])
                    time_widget.attrs.setdefault("placeholder", placeholder[1])
                else:
                    widget.widgets[0].attrs.setdefault("placeholder", placeholder)
                    widget.widgets[1].attrs.setdefault("placeholder", placeholder)
            else:
                widget.attrs.setdefault("placeholder", placeholder)
