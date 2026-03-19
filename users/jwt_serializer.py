from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['is_staff'] = user.is_staff

        return token

# The CustomTokenSerializer extends the TokenObtainPairSerializer to include additional claims in the JWT token.
# The get_token method is overridden to add the username and is_staff status of the user to the token's payload. This allows the client to access these details directly from the token without needing to make additional API calls.
# @classmethod is used to indicate that the method is a class method, which means it can be called on the class itself rather than on an instance of the class.
#super() is used to call the get_token method of the parent class (TokenObtainPairSerializer) to ensure that the standard token generation process is preserved while allowing us to add our custom claims.

