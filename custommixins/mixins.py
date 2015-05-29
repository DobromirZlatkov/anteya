from django.core.exceptions import PermissionDenied


class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
