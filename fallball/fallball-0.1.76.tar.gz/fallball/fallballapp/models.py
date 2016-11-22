from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


UNLIMITED = -1


class Application(models.Model):
    id = models.CharField(max_length=150, primary_key=True)
    owner = models.OneToOneField(User)

    def __str__(self):
        return self.id


class Reseller(models.Model):
    name = models.CharField(max_length=120)
    rid = models.CharField("Reseller ID", max_length=120)
    application = models.ForeignKey(Application)
    limit = models.IntegerField()
    # owner property is a foreign key related to User instance
    # It is needed to use token authorization
    owner = models.ForeignKey(User)

    class Meta:
        unique_together = (('application', 'name'), ('application', 'rid'))

    def __str__(self):
        return self.name

    def get_clients_amount(self):
        """
        Calculate clients amount for particular reseller
        """
        return Client.objects.filter(reseller=self).count()

    def get_usage(self):
        """
        Calculate usage of all clients for particular reseller
        """
        total = (Client.objects.filter(reseller=self)
                 .annotate(sum_usage=Sum('clientuser__usage'))
                 .aggregate(Sum('sum_usage')))['sum_usage__sum']
        return total or 0


class Client(models.Model):
    # Instance_id contains company name and used as client id
    name = models.CharField(max_length=150)
    is_integrated = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    limit = models.IntegerField()

    # Every client belongs to particular reseller
    reseller = models.ForeignKey(Reseller)

    class Meta:
        unique_together = ('reseller', 'name')

    def __str__(self):
        return self.name

    def get_usage(self):
        """
        Calculate total usage of all client users
        """
        total = ClientUser.objects.filter(client=self).aggregate(Sum('usage'))
        return total['usage__sum'] or 0

    def get_users_amount(self):
        """
        Calculate users amount for particular company
        """
        return ClientUser.objects.filter(client=self).count()

    def get_users_by_type(self):
        """
        Calculate number of users of each type for company
        """
        return {k: ClientUser.objects.filter(client=self, profile_type=k).count() for k in
                dict(ClientUser.USER_PROFILE_TYPES)}


class ClientUser(models.Model):
    DEFAULT_PROFILE = 'default'
    GOLD_PROFILE = 'gold'
    USER_PROFILE_TYPES = (
        (DEFAULT_PROFILE, 'Default'),
        (GOLD_PROFILE, 'Gold'),
    )
    email = models.EmailField()
    owner = models.OneToOneField(User)
    password = models.CharField(max_length=12, blank=True)
    usage = models.IntegerField(blank=True)
    admin = models.BooleanField(default=False)
    limit = models.IntegerField()
    client = models.ForeignKey(Client)
    profile_type = models.CharField(max_length=12, choices=USER_PROFILE_TYPES,
                                    default=DEFAULT_PROFILE)

    class Meta:
        unique_together = ('client', 'email')

    def __str__(self):
        return self.email
