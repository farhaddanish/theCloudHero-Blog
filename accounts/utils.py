from django.contrib.auth.tokens import PasswordResetTokenGenerator
class TokenGenertor(PasswordResetTokenGenerator):
    pass

generate_token = TokenGenertor()
