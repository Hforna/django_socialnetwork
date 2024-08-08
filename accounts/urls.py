from django.urls import path, include
from .views import *
from .api import *
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

routerr = SimpleRouter()
routerr.register("/user", UserViewApi)
print(routerr.urls)
router_profile = SimpleRouter()
router_profile.register("/profiles", ProfileViewApi, basename="get-profile")
router_post = SimpleRouter()
router_post.register("/posts", PostViewApi)

urlpatterns = [
    path("/signup", SignUp.as_view(), name="sign_up"),
    path("/login", login_page, name="login"),
    path("/logout", logouts, name="logout"),
    path("/create_user", create_user, name="create_user"),
    path("/email_reset_password", email_reset_password, name="email_reset_password"),
    path("/verify_email", verify_email, name="verify_email"),
    path("/reset_password", reset_password, name="reset_password"),
    # Api endpoints
    path('/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/api/token/refresh/', TokenRefreshView.as_view(), name='token_verify'),
    path('/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("/api", include(routerr.urls)),
    path("/api", include(router_profile.urls)),
    path("/api", include(router_post.urls))
    
]
