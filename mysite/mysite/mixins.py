from django.contrib.auth.mixins import LoginRequiredMixin


class AuthorRequiredMixin(LoginRequiredMixin):
    """Verify that the current user has right to modify."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_author:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
