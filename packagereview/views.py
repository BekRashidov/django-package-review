from honeypot.decorators import check_honeypot
from django.shortcuts import render


@check_honeypot(field_name='email')
def contact(request):
    return render(request, "contact.html")
