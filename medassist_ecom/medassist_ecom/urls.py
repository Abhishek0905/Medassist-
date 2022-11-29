"""medassist_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import Category_Controller
from . import SubCategory_Controller
from . import Brand_Controller
from . import Product_Controller
from . import Login_controller
from . import User_Controller


urlpatterns = [
    path('admin/', admin.site.urls),
    # CATEGORY
    path('categoryinterface/', Category_Controller.Category_Interface),
    path('submitcategory', Category_Controller.Submit_Category),
    path('displayallcategories/', Category_Controller.Display_All_Category),
    path('editcategory/', Category_Controller.Edit_Category),
    path('deletecategory/', Category_Controller.Delete_Category),
    path('editcategoryicon', Category_Controller.Edit_CategoryIcon),
    path('fetch_all_category_json', Category_Controller.Fetch_All_Category_JSON),
    # SUBCATEGORY
    path('subcategoryinterface/', SubCategory_Controller.SubCategory_Interface),
    path('submitsubcategory', SubCategory_Controller.Submit_SubCategory),
    path('displayallsubcategories/', SubCategory_Controller.Display_All_Subcategory),
    path('editsubcategory/', SubCategory_Controller.Edit_Subcategory),
    path('deletesubcategory/', SubCategory_Controller.Delete_Subcategory),
    path('editsubcategoryicon', SubCategory_Controller.Edit_SubcategoryIcon),
    path('fetchallsubcategoriesjson/', SubCategory_Controller.fetch_all_subcategory_json),
    # BRAND
    path('brandinterface/', Brand_Controller.Brand_Interface),
    path('submitbrand', Brand_Controller.Submit_Brand),
    path('displayallbrand/', Brand_Controller.Display_All_Brand),
    path('editbrand/', Brand_Controller.Edit_Brand),
    path('deletebrand/', Brand_Controller.Delete_Brand),
    path('editbrandicon', Brand_Controller.Edit_BrandIcon),
    path('fetchallbrandjson/', Brand_Controller.fetch_all_brand_json),
    # PRODUCT
    path('productinterface/', Product_Controller.Product_Interface),
    path('submitproduct', Product_Controller.Submit_Product),
    path('displayallproduct/', Product_Controller.Display_All_Product),
    path('editproduct/', Product_Controller.Edit_Product),
    path('deleteproduct/', Product_Controller.Delete_Product),
    path('editproducticon', Product_Controller.Edit_ProductIcon),
    # LOGIN
    path('logininterface/', Login_controller.Admin_Login),
    path('adminlogout/', Login_controller.Admin_Logout),
    path('checkadminlogin',Login_controller.Check_Admin_Login),
    # USER
    path('home/',User_Controller.Index),
    path('fetch_all_user_category/',User_Controller.Fetch_All_Category_JSON),
    path('fetch_all_products/',User_Controller.Fetch_All_Products),
    path('fetch_all_subcategory_json/',User_Controller.Fetch_All_SubCategory_JSON),
    path('buy_product/',User_Controller.Buy_Product),
    path('add_to_cart/',User_Controller.AddToCart),
    path('fetch_cart/',User_Controller.FetchCart),
]
