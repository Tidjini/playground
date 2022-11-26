class RedirectAuthenticationUserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if args[0]:
            print("print this section")
            return

        print("else print this instead")
        response = super(RedirectAuthenticationUserMixin, self).dispatch(
            request, *args, **kwargs
        )
        return response


c = RedirectAuthenticationUserMixin()
c.dispatch(None, 1)
