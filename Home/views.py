from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import ClientDetailsForm, ServiceDetailsForm, Service_provider_form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Client_details, Service_details, Service_provider
from django.urls import reverse
from num2words import num2words


@login_required(login_url="/login/")
def dashboard(request):
    context = {'title': 'Dashboard'}
    return render(request, 'dashboard.html', context)

@login_required(login_url="/login/")
def logout_page(request):
    logout(request)
    return redirect("/login/")

@login_required(login_url="/login/")
def add_invoice(request):
    ClientForm = ClientDetailsForm()
    ServiceForm = ServiceDetailsForm()
    if request.method == "POST":
        form_btn = request.POST.get('form_btn')
        if form_btn=='client_form_btn':
            ClientForm = ClientDetailsForm(request.POST)
            if ClientForm.is_valid():
                name = ClientForm.cleaned_data['company_name']
                gst_number = ClientForm.cleaned_data['gst_number']
                country = ClientForm.cleaned_data['country']
                state = ClientForm.cleaned_data['state']
                address = ClientForm.cleaned_data['address']
                obj = Client_details(company_name= name,
                                     gst_number = gst_number,
                                     country = country,
                                     state = state,
                                     address = address,
                                     )
                obj.save()
                messages.success(request, "Your Client form has been updated successfully.")
                ClientForm = ClientDetailsForm()
        elif form_btn=='service_form_btn':
            ServiceForm = ServiceDetailsForm(request.POST)
            if ServiceForm.is_valid():
                client = ServiceForm.cleaned_data['client']
                description = ServiceForm.cleaned_data['description']
                quantity = ServiceForm.cleaned_data['quantity']
                amount = ServiceForm.cleaned_data['amount']
                ServiceObj = Service_details(client = client,
                                             description = description,
                                             quantity = quantity,
                                             amount = amount)
                ServiceObj.save()
                messages.success(request, "Service Form has been updated.")
                ServiceForm = ServiceDetailsForm()
    context = {'title': 'Add Invoice', 'ClientForm': ClientForm, 'ServiceForm': ServiceForm}
    return render(request, 'add_invoice.html', context)


@login_required(login_url="/login/")
def service_provider_page(request):
    data = Service_provider.objects.all().order_by('-created_at')[:10]
    if request.method == "POST":
        form = Service_provider_form(request.POST)
        if form.is_valid():
            client = form.cleaned_data['client']
            company = form.cleaned_data['company_name']
            handle_by = form.cleaned_data['handle_by']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            account_no = form.cleaned_data['account_number']
            ifsc = form.cleaned_data['ifsc_code']
            bank = form.cleaned_data['bank_name']
            gst = form.cleaned_data['gst_number']
            obj = Service_provider(client=client,
                                   company_name=company,
                                   handle_by=handle_by,
                                   email=email,
                                   phone=phone,
                                   account_number=account_no,
                                   ifsc_code=ifsc,
                                   bank_name=bank,
                                   gst_number=gst)
            obj.save()
            messages.success(request, "Service Provider has been added successfully.")
            form = Service_provider_form()
            return redirect(request.path)
    else:
        form = Service_provider_form()
    return render(request, "Service_provider.html",{'form': form, 'data': data})

@login_required(login_url="/login/")
def update_service_provider(request, id):
    obj = Service_provider.objects.get(id=id)
    if request.method == "POST":
        form = Service_provider_form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Service Provider Updated Successfully!")
    else:
        form = Service_provider_form(instance = obj)
    return render(request, "update_service_provider.html", {'form': form})


@login_required(login_url="/login/")
def delete_service(request, id):
    if request.method=='POST':
        obj = Service_provider.objects.get(id=id)
        obj.delete()
    return redirect(reverse('service_provider_page'))


@login_required(login_url="/login/")
def review_invoices(request):
    data = Client_details.objects.all().order_by("-created_at")
    return render(request, "review_Invoices.html", {'data': data})
        


@login_required(login_url="/login/")
def update_client(request, id):
    data = Client_details.objects.get(id=id)
    if request.method == "POST":
        form = ClientDetailsForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Clent details are updated successfully.")
    else:
        form = ClientDetailsForm(instance = data)
    return render(request, "update_client.html", {'form': form})

@login_required(login_url="/login/")
def delete_client(request, id):
    if request.method=="POST":
        obj = Client_details.objects.get(id=id)
        obj.delete()
    return redirect(reverse('review_invoices'))

@login_required(login_url="/login/")
def review_invoice(request, id):
    client_Data = Client_details.objects.get(id=id)
    try:
        service_provider_Data = Service_provider.objects.get(client_id=id)
    except Service_provider.DoesNotExist:
        service_provider_Data = {'key': 'val'}
    
    try:
        services_Data = Service_details.objects.filter(client_id=id)
    except Service_details.DoesNotExist:
        services_Data = {'key': 'val'}
    context =  {"clientDetails": client_Data, "ServiceProvider": service_provider_Data, "ServicesData": services_Data}
    return render(request, "review_invoice.html", context)

@login_required(login_url="/login/")
def update_service(request, id):
    data = Service_details.objects.get(id=id)
    if request.method=="POST":
        form = ServiceDetailsForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
            messages.success(request, "Service data updated Successfully.")
            return redirect(reverse('review_invoice_page', args=[data.client_id]))
    else:
        form = ServiceDetailsForm(instance = data)
    return render(request, "update_services.html", {"ServiceForm": form})

@login_required(login_url="/login/")
def delete_service(request, id):
    if request.method == "POST":
        obj = Service_details.objects.get(id=id)
        client_id = obj.client_id
        obj.delete()
    return redirect(reverse('review_invoice_page', args=[client_id]))


@login_required(login_url="/login/")
def all_invoice(request):
    data = Client_details.objects.all().order_by('-created_at')
    return render(request, "all_invoice_list.html", {"data": data})

@login_required(login_url='/login/')
def invoice_report(request, id):
    client_Data = Client_details.objects.get(id=id)
    try:
        service_provider_Data = Service_provider.objects.get(client_id=id)
    except Service_provider.DoesNotExist:
        service_provider_Data = {'key': 'val'}
    
    try:
        services_Data = Service_details.objects.filter(client_id=id)
        total = 0
        for service in services_Data:
            total += service.amount*service.quantity
        gst_amt = total*0.18
        price_with_gst = total + gst_amt
        word_amt = num2words(price_with_gst, lang='en')
    except Service_details.DoesNotExist:
        services_Data = {'key': 'val'}
    
    context = {'companyData': service_provider_Data, 'clientData': client_Data, 'servicesData': services_Data,
               'gst_amt': gst_amt, 'total': total, 'price_with_gst': price_with_gst, 'word_amt': word_amt}
    return render(request, 'Invoice.html', context)