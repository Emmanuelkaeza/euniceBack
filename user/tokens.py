from rest_framework_simplejwt.tokens import AccessToken

class CustomAccessToken(AccessToken):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.payload['role'] = 'admin' if user.is_superuser else 'user'
        self.payload['user_id'] = user.id
