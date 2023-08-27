from django.shortcuts import redirect, render
from CRUD_APP.models import Employees
# Create your views here.
def INDEX(request):

    emp = Employees.objects.all()

    context = {
        "emp":emp,
        "length":len(emp)
    }

    return render(request, 'index.html',context)


def ADD(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(name = name,
                        email = email,
                        address = address,
                        phone = phone
                        )
        emp.save()        
        return redirect('home')
    # return render(request, 'index.html')

# def EDIT(request):

#     emp = Employees.objects.all()
#     context = {
#         "emp":emp,
#     }
#     return redirect(request, 'index.html',context)



def UPDATE(request,id):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
                        id = id,
                        name = name,
                        email = email,
                        address = address,
                        phone = phone
                        )
        emp.save() 
        return redirect('home') 


    return redirect(request, 'index.html')

def DELETE(request,id):
        emp = Employees.objects.filter(id = id).delete()
        return redirect('home')
