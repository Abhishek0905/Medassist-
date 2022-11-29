from django.shortcuts import render
from medassist_ecom import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt

def Product_Interface(request):
    try:
        admin = request.session['ADMIN']
        return render(request, 'productinterface.html')
    except:
        return render(request, 'logininterface.html')
@xframe_options_exempt
def Submit_Product(request):
    try:
        DB,CMD= Pool.ConnectionPooling()
        productname = request.POST['productname']
        productprice = request.POST['productprice']
        offerprice = request.POST['offerprice']
        packingtype = request.POST['packingtype']
        saleststus = request.POST['salestatus']
        quantity = request.POST['quantity']
        status = request.POST['status']
        rating = request.POST['rating']
        producticon = request.FILES['producticon']
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        brandid=request.POST['brandid']
        Q = "insert into product(productname,productprice,offerprice,packingtype,salestatus,quantity,status,rating,producticon,categoryid,subcategoryid,brandid) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(productname,productprice,offerprice,packingtype,saleststus,quantity,status,rating,producticon.name,categoryid,subcategoryid,brandid)
        F = open("d:/medassist_ecom/assets/"+producticon.name,'wb')
        for chunk in producticon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'productinterface.html',{'message':'Record submitted'})
    except Exception as e:
        print("Error:",e)
        return render(request, 'productinterface.html', {'message': 'Record Not submitted'})
@xframe_options_exempt
def Display_All_Product(request):
    try:
        admin = request.session['ADMIN']
    except:
        return render(request, 'logininterface.html')
    try:
        DB,CMD=Pool.ConnectionPooling()
        Q="select * from product"
        CMD.execute(Q)
        records=CMD.fetchall()
        DB.close()
        return render(request,'DisplayAllProduct.html',{'records':records})
    except Exception as e:
        return render(request,'DisplayAllProduct.html', {'records': None})

@xframe_options_exempt
def Edit_Product(request):
  try:
    DB,CMD=Pool.ConnectionPooling()
    productname = request.GET['productname']
    productprice = request.GET['productprice']
    offerprice = request.GET['offerprice']
    packingtype = request.GET['packingtype']
    saleststus = request.GET['salestatus']
    quantity = request.GET['quantity']
    status = request.GET['status']
    rating = request.GET['rating']
    categoryid = request.GET['categoryid']
    subcategoryid = request.GET['subcategoryid']
    brandid = request.GET['brandid']
    productid=request.GET['productid']
    Q="update product set productname='{0}',productprice='{1}',offerprice='{2}',packingtype='{3}',salestatus='{4}',quantity='{5}',status='{6}',rating='{7}',categoryid={8},subcategoryid={9},brandid={10} where productid={11}".format(productname,productprice,offerprice,packingtype,saleststus,quantity,status,rating,categoryid,subcategoryid,brandid,productid)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)
@xframe_options_exempt
def Delete_Product(request):
  try:
    DB,CMD=Pool.ConnectionPooling()
    productid = request.GET['productid']
    Q="delete from product where productid={0}".format(productid)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
      print("Error:",e)
      return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Edit_ProductIcon(request):
  try:
    DB,CMD=Pool.ConnectionPooling()
    productid = request.POST['productid']
    producticon = request.FILES['producticon']
    Q="update product set producticon='{0}' where productid={1}".format(producticon.name,productid)
    print(Q)
    F = open("d:/medassist_ecom/assets/" + producticon.name, 'wb')
    for chunk in producticon.chunks():
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
        query = "select * from brand where subcategoryid={0}".format(subcategoryid)
        cmd.execute(query)
        records = cmd.fetchall()
        db.close()
        return JsonResponse({'data': records}, safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'data': None}, safe=False)