from django.forms.widgets import SplitDateTimeWidget
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.http import Http404


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

class SuperuserRequiredMixin(UserPassesTestMixin):

    raise_exception = True

    def test_func(self) -> bool:
        """Test if the user is a superuser.

        Returns:
            bool: True if the user is a superuser, otherwise False.
        """
        return self.request.user.is_superuser if self.request.user.is_authenticated else False

    def handle_no_permission(self):
        """Handle the case when the user does not have the required permission.

        Returns:
            HttpResponse: Redirect to the login page or raise a 404 exception
            if the user is authenticated.
        """
        if self.raise_exception and self.request.user.is_authenticated:
            raise Http404
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name(),
        )
    
class StaffRequiredMixin(UserPassesTestMixin):

    raise_exception = True

    def test_func(self) -> bool:
        """Test if the user is a staff.

        Returns:
            bool: True if the user is a staff, otherwise False.
        """
        return self.request.user.is_staff if self.request.user.is_authenticated else False

    def handle_no_permission(self):
        """Handle the case when the user does not have the required permission.

        Returns:
            HttpResponse: Redirect to the login page or raise a 404 exception if the user is authenticated.
        """
        if self.raise_exception and self.request.user.is_authenticated:
            raise Http404
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name(),
        )
    
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import Http404
from django.contrib.auth.views import redirect_to_login

class UserObjectPermissionMixin(UserPassesTestMixin):
    """
    Mixin to control access based on user level:
    - Staff or higher can access any object.
    - Active users can only access objects they own (object.user).
    """
    raise_exception = True

    def test_func(self) -> bool:
        user = self.request.user
        obj = self.get_object()

        if not user.is_authenticated:
            return False

        if user.is_staff:
            return True

        return user.is_active and hasattr(obj, 'user') and user.id == obj.user.id

    def handle_no_permission(self):
        if self.raise_exception and self.request.user.is_authenticated:
            raise Http404
        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name(),
        )
