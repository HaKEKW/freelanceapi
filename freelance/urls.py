from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_refresh'),
    # path('auth/token/', obtain_auth_token, name='token'),
    # path('auth/logout/', Logout.as_view()),


    path('executors/<int:pk>/', ExecutorRetrieveAPIView.as_view()),
    path('executors/update/<int:pk>/', ExecutorUpdateAPIView.as_view()),
    path('executors/all/', ExecutorListAPIView.as_view()),
    path('executors/new/', ExecutorCreateAPIView.as_view()),

    path('customers/<int:pk>/', CustomerRetrieveAPIView.as_view()),
    path('customers/update/<int:pk>/', CustomerUpdateAPIView.as_view()),
    path('customers/all/', CustomerListAPIView.as_view()),
    path('customers/new/', CustomerCreateAPIView.as_view()),

    path('services/<int:pk>/', ServiceRetrieveAPIView.as_view()),
    path('services/update/<int:pk>/', ServiceUpdateAPIView.as_view()),
    path('services/all/', ServiceListAPIView.as_view()),
    path('services/new/', ServiceCreateAPIView.as_view()),

    path('orders/<int:pk>/', OrderRetrieveAPIView.as_view()),
    path('orders/update/<int:pk>/', OrderUpdateAPIView.as_view()),
    path('orders/all/', OrderListAPIView.as_view()),
    path('orders/new/', OrderCreateAPIView.as_view()),

    path('tags/<int:pk>/', TagRetrieveAPIView.as_view()),
    path('tags/update/<int:pk>/', TagUpdateAPIView.as_view()),
    path('tags/all/', TagListAPIView.as_view()),
    path('tags/new/', TagCreateAPIView.as_view()),

    path('ordering/<int:pk>/', OrderingRetrieveAPIView.as_view()),
    path('ordering/update/<int:pk>/', OrderingUpdateAPIView.as_view()),
    path('ordering/all/', OrderingListAPIView.as_view()),
    path('ordering/new/', OrderingCreateAPIView.as_view()),

    path('messages/<int:pk>/', MessageRetrieveAPIView.as_view()),
    path('messages/update/<int:pk>/', MessageUpdateAPIView.as_view()),
    path('messages/all/', MessageListAPIView.as_view()),
    path('messages/new/', MessageCreateAPIView.as_view()),

    path('tickets/<int:pk>/', TicketRetrieveAPIView.as_view()),
    path('tickets/update/<int:pk>/', TicketUpdateAPIView.as_view()),
    path('tickets/all/', TicketListAPIView.as_view()),
    path('tickets/new/', TicketCreateAPIView.as_view()),

    path('review/<int:pk>/', ReviewRetrieveUpdateAPIView.as_view()),
    path('review/update/<int:pk>/', ReviewRetrieveUpdateAPIView.as_view()),
    path('review/all/', ReviewListAPIView.as_view()),
    path('review/new/', ReviewCreateAPIView.as_view()),

    path('authoring/<int:pk>/', AuthoringRetrieveAPIView.as_view()),
    path('authoring/update/<int:pk>/', AuthoringUpdateAPIView.as_view()),
    path('authoring/all/', AuthoringListAPIView.as_view()),
    path('authoring/new/', AuthoringCreateAPIView.as_view()),
]
