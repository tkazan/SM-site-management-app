from django.db import models
from PIL import Image


class Sites(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    status = models.TextField(null=True)
    status_photo = models.ImageField(null=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return "%s %s" % (self.name, self.address[:20])


class Contacts(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    phone = models.CharField(max_length=64)
    mail = models.EmailField()
    photo = models.ImageField(null=True)
    sites = models.ManyToManyField(Sites, through="SitesContacts")

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class SitesContacts(models.Model):
    sites = models.ForeignKey(Sites)
    contacts = models.ForeignKey(Contacts)
    function = models.CharField(max_length=64)

    def __str__(self):
        return "%s %s" % (self.sites.name, self.contacts.name)


class Materials(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    unit = models.CharField(max_length=64)
    providers = models.ManyToManyField("Providers", through="ProvidersMaterials")
    sites = models.ManyToManyField(Sites, through="SitesMaterials")

    def __str__(self):
        return "%s %s" % (self.name, self.description[:20])


class SitesMaterials(models.Model):
    sites = models.ForeignKey(Sites)
    materials = models.ForeignKey(Materials)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return " %s - %s - %s - %s%s" % (self.sites.name, self.materials.name, self.materials.description,
                              self.qty, self.materials.unit)


class Machines(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=64)
    operator = models.CharField(max_length=128)
    operator_phone = models.CharField(max_length=64, default="888-888-888")
    sites = models.ManyToManyField(Sites)

    def __str__(self):
        return "%s %s" % (self.name, self.description[:20])


class Contractors(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    phone = models.CharField(max_length=32, null=True)
    sites = models.ManyToManyField(Sites)

    def __str__(self):
        return self.name


class Providers(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    mail = models.EmailField()

    def __str__(self):
        return self.name


class ProvidersMaterials(models.Model):
    providers = models.ForeignKey(Providers)
    materials = models.ForeignKey(Materials)
    price = models.DecimalField(max_digits=10, decimal_places=2)

