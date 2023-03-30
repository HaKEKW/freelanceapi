from rest_framework import generics, status, permissions
from rest_framework.exceptions import PermissionDenied

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class ExecutorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = (permissions.AllowAny, )


class ExecutorUpdateAPIView(generics.UpdateAPIView):
    # queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Executor.objects.filter(user=user)


class ExecutorCreateAPIView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer


class ExecutorListAPIView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class CustomerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateAPIView(generics.UpdateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateCustomerSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ServiceRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateAPIView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ServiceCreateAPIView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ServiceListAPIView(generics.ListAPIView):
    # queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        params = self.request.query_params

        service_type = params.get('service', None)
        price = params.get('price', None)
        executor = params.get('executor', None)

        if service_type:
            queryset = queryset.filter(service=service_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        return queryset


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderListAPIView(generics.ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        params = self.request.query_params

        service_type = params.get('service', None)
        price = params.get('price', None)
        customer = params.get('customer', None)

        if service_type:
            queryset = queryset.filter(service=service_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        return queryset


class TagRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateAPIView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class TagCreateAPIView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class OrderingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class OrderingUpdateAPIView(generics.UpdateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderingCreateAPIView(generics.CreateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderingListAPIView(generics.ListAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class MessageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateAPIView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class MessageCreateAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class MessageListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        params = self.request.query_params

        executor = params.get('executor', None)
        customer = params.get('customer', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        if from_date:
            queryset = queryset.filter(from_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(to_date__lte=to_date)

        return queryset


class TicketRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketUpdateAPIView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class TicketCreateAPIView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class TicketListAPIView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ReviewRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class AuthoringRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer


class AuthoringUpdateAPIView(generics.UpdateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AuthoringCreateAPIView(generics.CreateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


class AuthoringListAPIView(generics.ListAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer

# class TicketAPIView(APIView):
#     def get(self, request):
#         queryset = Ticket.objects.all()
#         serializer_class = TicketSerializer(queryset, many=True)
#         return Response({'tickets': serializer_class.data})
