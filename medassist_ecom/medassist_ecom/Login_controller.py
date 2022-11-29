from django.shortcuts import render
from medassist_ecom import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def Admin_Login(request):
    return render(request,"logininterface.html")
def Admin_Logout(request):
    del request.session['ADMIN']
    return render(request,"logininterface.html")

def Check_Admin_Login(request):
    try:
        DB,CMD = Pool.ConnectionPooling()
        emailid = request.POST['emailid']
        password = request.POST['password']
        query = "select * from adminlogin where emailid='{0}' and password='{1}'".format(emailid,password)
        print(query)
        CMD.execute(query)
        row=CMD.fetchone()
        print(row)
        if(row):
            request.session['ADMIN'] = row
            return render(request, "DashBoard.html",{'row':row})
        else:
            return render(request, "logininterface.html",{'message':'Invalid Emailid/Password'})
        db.close()
    except Exception as e:
        return render(request, "logininterface.html", {'message': 'Something went wrong'})

