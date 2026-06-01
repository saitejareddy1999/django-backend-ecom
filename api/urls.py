from django.urls import path
from Users import views as user_views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('Register/',user_views.RegisterView.as_view(), name='user-list'),
    path('Profile/', user_views.profileView.as_view(), name='user-profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 
]