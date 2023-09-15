from django.db import models

# Create your models here.

class Client_details(models.Model):
    company_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.company_name}--{self.gst_number}"


class Service_details(models.Model):
    client = models.ForeignKey(Client_details, on_delete=models.CASCADE, related_name='services')
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    Created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Service --> {self.client}"

class Service_provider(models.Model):
    client = models.ForeignKey(Client_details, on_delete=models.CASCADE, related_name='service_provider')
    company_name = models.CharField(max_length=100)
    handle_by = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    account_number = models.BigIntegerField()
    ifsc_code = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name}, Client: {self.client}"
