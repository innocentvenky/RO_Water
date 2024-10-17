
from django.urls import path
from .views import Usercreate, Userget,Userupdate,Imagecreate,Imageupdate,Imageget,UserLoginView
from .views import Purifier_Model_Create,Purifier_Model_Retrive,Purifier_Model_Update,Purifier_Model_Delete
from .views import Address_Create,Address_Get,Address_Get_Id,Address_Update
from .views import Purifier_Details_Create,Purifier_Details_Get,Purifier_Details_Update,Purifier_Details_Delete
from .views import Feedback_Create,Feedback_Get,Feedback_Update,Feedback_Delete
from .views import Bill_Generate,Bill_Get
from .views import Service,Geting_Service_Details,Update_Service,Delete_Service


urlpatterns = [
    
    path(r"api/user_create/",Usercreate.as_view()),
    path(r"api/user_get/",Userget.as_view()),
    path(r"api/user_update/<uuid:public_id>",Userupdate.as_view()),
    path(r"api/image/",Imagecreate.as_view()),
    path(r"api/image_get/",Imageget.as_view()),
    path(r"api/image_update/<uuid:public_id>",Imageupdate.as_view()),
    path(r"api/login/",UserLoginView.as_view()),
    path(r"api/purifier_model/",Purifier_Model_Create.as_view()),
    path(r"api/purifier_model_get/",Purifier_Model_Retrive.as_view()),
    path(r"api/purifier_model_upadate/<uuid:public_id>",Purifier_Model_Update.as_view()),
    path(r"api/purifier_model_delete/<uuid:public_id>",Purifier_Model_Delete.as_view()),
    path(r'api/purifier_details_create/',Purifier_Details_Create.as_view()),
    path(r'api/purifier_details_get/',Purifier_Details_Get.as_view()),
    path(r'api/purifier_details_update/<uuid:public_id>',Purifier_Details_Update.as_view()),
    path(r'api/purifier_details_delete/<uuid:public_id>',Purifier_Details_Delete.as_view()),
    path(r'api/address/',Address_Create.as_view()),
    path(r'api/address_get/',Address_Get.as_view()),
    path(r'api/address_get_id/<uuid:user_id>',Address_Get_Id.as_view()),
    path(r'api/address_update/<uuid:public_id>',Address_Update.as_view()),
    path(r'api/feedback_create/',Feedback_Create.as_view()),
    path(r'api/feedback_get/',Feedback_Get.as_view()),
    path(r'api/feedback_update/<uuid:public_id>',Feedback_Update.as_view()),
    path(r'api/feedback_delete/<uuid:public_id>',Feedback_Delete.as_view()),
    path(r'api/bill_generate/',Bill_Generate.as_view()),
    path(r'api/bill_get/',Bill_Get.as_view()),
    path(r'api/serviceing/',Service.as_view()),
    path(r'api/get_service/',Geting_Service_Details.as_view()),
    path(r'api/update_service/<uuid:public_id>',Update_Service.as_view()),
    path(r'api/delete_service/<uuid:public_id>',Delete_Service.as_view())



]