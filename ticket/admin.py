from django.contrib import admin

from user.tasks import send_link_email_task
from django.shortcuts import render

from .models import Plan, Payment, Ticket,ReffealCode
from django.http import HttpResponse
from django import forms

from io import StringIO 
import csv
from django.contrib.admin.helpers import ActionForm

class Reffreal(admin.ModelAdmin):
    exclude = ( 'usage',)
    list_display = ('owner', 'code','usage')

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('Person', 'name', 'quantity')
    search_fields = ('Person__email', 'name')
    actions = ['download_csv']
    def download_csv(self, request, queryset):

    

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(["name", "email", "quanty", "phone"])

        for querry in queryset:
            phone=""
        
            if querry.Person.student:
                phone=querry.Person.student.phone_number
            elif querry.Person.ca:
                phone=querry.Person.ca.phone_number
            elif querry.Person.proff:
                phone=querry.Person.proff.phone_number
            print(phone)
            writer.writerow([querry.Person,querry.Person.email,querry.quantity,phone])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response


admin.site.register(Plan)
admin.site.register(Payment)



        
admin.site.register(Ticket, TicketsAdmin)
          

        
# Register your models here.
