from django.shortcuts import render

from django.http import JsonResponse

from fistApp.models import Employee
# Create your views here.


def employeeView(request):
    # Note: we are not really using the requests; just testing
    emp = {
        'id': 123,
        'name': 'Bradley',
        'salary': 100000
    }

    data = Employee.objects.all()
    response = {
        'employees': list(data.values_list()[:])
        }
    return JsonResponse(response)


    