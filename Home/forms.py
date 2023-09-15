from django import forms 
from .models import Client_details, Service_details, Service_provider



# --------------------------------------------------------------------------------------
class ClientDetailsForm(forms.ModelForm):
    class Meta:
        model = Client_details
        fields = ["company_name", "gst_number", "country", "state", "address"]
        labels = {
            "company_name": "Company Name",
            "gst_number": "GST",
            "country": "Country",
            "state": "State",
            "address": "Address"
        }
    def __init__(self, *args, **kwargs):
        super(ClientDetailsForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class ServiceDetailsForm(forms.ModelForm):
    class Meta:
        model = Service_details
        fields = ["client", "description", "quantity", "amount"]
        labels = {
            "client": "Client",
            "description": "Description",
            "quantity": "Quantity",
            "amount": "Amount"
        }
    def __init__(self, *args, **kwargs):
        super(ServiceDetailsForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
            self.fields[field_name].widget.attrs['class'] = 'form-control'

#--------------------------------------------------------------------------------------

class Service_provider_form(forms.ModelForm):
    class Meta:
        model = Service_provider
        fields = ["client", "company_name", "handle_by", "email", "phone", "account_number", "ifsc_code", "bank_name", "gst_number"]
        labels = {
            "client": "Client",
            "company_name": "Company", 
            "handle_by": "Handle By",
            "email": "Email",
            "phone": "Phone NO.",
            "account_number": "Account Number",
            "ifsc_code": "IFSC Code",
            "bank_name": "Bank Name",
            "gst_number": "GST No."
        }
    
    def __init__(self, *args, **kwargs):
        super(Service_provider_form, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True
            field.widget.attrs['class'] = 'form-control'