class FakeAuthMiddleware:
    """A tiny fake middleware that injects a `fake_user` attribute and a header
    into the request for local development and tests.

    It should NOT be used in production. It is useful to simulate an authenticated
    user or to add deterministic metadata while developing the frontend.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # attach a simple fake user-like object
        request.fake_user = {
            'id': 1,
            'username': 'fake_user',
            'is_staff': False,
        }

        # also set a header that views can inspect
        request.META.setdefault('HTTP_X_FAKE_AUTH', '1')

        response = self.get_response(request)
        return response
