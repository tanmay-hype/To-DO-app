from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenSerializer(TokenObtainPairSerializer):#CustomTokenSerializer is a custom serializer that extends the TokenObtainPairSerializer provided by the Simple JWT library. It allows for customizing the JWT token generation process, such as adding custom claims to the token payload.
    @classmethod
    def get_token(cls, user):
        print("custom jwt working")
        token = super().get_token(user)
        token['username'] = user.username
        token['is_staff'] = user.is_staff
        return token
# The get_token method is overridden to add custom claims to the token payload. In this case, the username of the user is added as a claim in the token. This allows clients to access the username directly from the token without needing to make additional API calls to retrieve user information.  
#  @classmethod is used to indicate that the method is a class method, which means it can be called on the class itself rather than on an instance of the class. This is necessary because the get_token method is called by the Simple JWT library when generating tokens, and it needs to be able to access the method without needing an instance of the CustomTokenSerializer class.
# super() is used to call the get_token method of the parent class (TokenObtain
# PairSerializer) to ensure that the standard token generation process is preserved while allowing us to add our custom claims. This way, we can leverage the existing functionality of the parent class while extending it with our custom logic.
