from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("get-details/", views.UserDetailAPI.as_view()),

    path('register/', views.RegisterUserAPIView.as_view()),

    path('api/token/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('chatlistfriends/<str:sender>/<str:reciver>', views.getFrindsChats),

    path('chatlistfriends/<str:sender>/<str:reciver>/create',
         views.createMessageToFriend),

    path('chatlistfriends/<str:sender>',
         views.getFrindsChatsList),

    path('deleteMessage/<int:pk>',
         views.deleteMessage),

    path('createUserProfile/',
         views.createUserProfile),

    path('userProfileUpdate/<str:username>',
         views.userProfileUpdate),

    path('getprofile/<str:user>',
         views.getprofile),

]
