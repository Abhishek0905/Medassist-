from django.shortcuts import render
from medassist_ecom import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt


def Brand_Interface(request):
    try:
        admin = request.session['ADMIN']
        return render(request, 'brandinterface.html')
    except:
        return render(request, 'logininterface.html')
@xframe_options_exempt
def Submit_Brand(request):
    try:
        DB,CMD= Pool.ConnectionPooling()
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        brandname = request.POST['brandname']
        contactperson = request.POST['contactperson']
        mobileno = request.POST['mobileno']
        status = request.POST['status']
        brandicon = request.FILES['brandicon']
        Q = "insert into brand(brandname,contactperson,mobileno,status,brandicon,categoryid,subcategoryid) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(brandname,contactperson,mobileno,status,brandicon.name,categoryid,subcategoryid)
        F = open("d:/medassist_ecom/assets/"+brandicon.name,'wb')
        for chunk in brandicon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'brandinterface.html',{'message':'Record submitted'})
    except Exception as e:
        print("Error:",e)
        return render(request, 'brandinterface.html', {'message': 'Record Not submitted'})
@xframe_options_exempt
def Display_All_Brand(request):
    try:
        admin = request.session['ADMIN']
    except:
        return render(request, 'logininterface.html')
    try:
        DB,CMD=Pool.ConnectionPooling()
        Q="select * from brand"
        CMD.execute(Q)
        records=CMD.fetchall()
        DB.close()
        return render(request,'DisplayAllBrands.html',{'records':records})
    except Exception as e:
        return render(request,'DisplayAllBrands.html', {'records': None})

@xframe_options_exempt
def Edit_Brand(request):
  try:
    DB,CMD=Pool.ConnectionPooling()
    brandname=request.GET['brandname']
    contactperson=request.GET['contactperson']
    mobileno=request.GET['mobileno']
    status=request.GET['status']
    categoryid = request.GET['categoryid']
    subcategoryid = request.GET['subcategoryid']
    brandid=request.GET['brandid']
    Q="update brand set brandname='{0}',contactperson='{1}',mobileno='{2}',status='{3}',categoryid={4},subcategoryid={5} where brandid={6}".format(brandname,contactperson,mobileno,status,categoryid,subcategoryid,brandid)
    print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Delete_Brand(request):
  try:
    DB,CMD=Pool.ConnectionPooling()
    brandid = request.GET['brandid']
    Q="delete from brand  where  brandid={0}".format(brandid)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Edit_BrandIcon(request):
  try:
    DB,CMD=Pool.ConnectionPooling()
    brandid = request.POST['brandid']
    brandicon = request.FILES['brandicon']
    Q="update brand set brandicon='{0}' where  brandid={1}".format(brandicon.name,brandid)
    print(Q)
    F = open("d:/medassist_ecom/assets/" + brandicon.name, 'wb')
    for chunk in brandicon.chunks():
      F.write(chunk)
    F.close()
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def fetch_all_brand_json(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        subcategoryid=request.GET['subcategoryid']
        Q = "select * from brand where subcategoryid={0}".format(subcategoryid)
        print(Q)
        cmd.execute(Q)
        records = cmd.fetchall()
        db.close()
        return JsonResponse({'data': records}, safe=False)

    except Exception as e:
        print("Error:",e)
        return JsonResponse({'data': None}, safe=False)

