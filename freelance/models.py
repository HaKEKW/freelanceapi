from django.db import models
from django.contrib.auth.models import User


class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.user}, phone: {self.phone}'


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.user}, phone: {self.phone}'


class Service(models.Model):
    SERVICE_TYPES = (
        ('1', 'Web-Dev'),
        ('2', 'Marketing'),
        ('3', 'Copywriting'),
        ('4', 'Rewriting'),
        ('5', 'Translation'),
        ('6', 'Video Montage'),
        ('7', 'Photo'),
    )

    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=SERVICE_TYPES, default='1', max_length=1)

    def __str__(self):
        return f'{self.name}, {self.get_service_type_display()}, price: {self.price}'


class Order(models.Model):
    ORDER_TYPES = (
        ('1', 'Web-Dev'),
        ('2', 'Marketing'),
        ('3', 'Copywriting'),
        ('4', 'Rewriting'),
        ('5', 'Translation'),
        ('6', 'Video Montage'),
        ('7', 'Photo'),
    )

    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=ORDER_TYPES, default='1', max_length=1)

    def __str__(self):
        return f'{self.name}, {self.get_service_type_display()}, price: {self}'


class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    ordering = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)


class Ordering(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    ordering = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    order_data = models.DateTimeField()
    deadline = models.DateTimeField()


class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    msg_data = models.DateTimeField()
    is_edited = models.BooleanField(default=False)
    desc = models.BooleanField()


class Ticket(models.Model):
    SEVERITIES = (
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'),

    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=SEVERITIES, default='1', max_length=1)
    desc = models.CharField(max_length=1000)
    ticket_date = models.DateTimeField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.get_severity_display()}, {self.ticket_date}, Is resolved? {self.is_resolved}'


class Review(models.Model):
    RATING_FIELD = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )
    rating = models.CharField(choices=RATING_FIELD, default='1', max_length=1)
    desc = models.CharField(max_length=1000)


class Authoring(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateTimeField()

    def __str__(self):
        return f'{self.author} {self.review_date}'
