from django.shortcuts import render
from .models import User, Image
from .models import PurifierDetails,PurifierModel,Address,Feedback,Billing,Servicing
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, ImageSerializer,UserLoginSerializer
from .serializers import FeedbackSerializer,PurifierdeatilsSerializer,PurifierModelSerializer,AddressSerializer
from .serializers import BillingSerializer,ServiceSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from .utils import get_tokens_for_user
from rest_framework.permissions import IsAuthenticated


class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = get_tokens_for_user(user)
            return Response({
                'public_id': user.public_id,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'email':user.email,
                'phone_number':user.phone_number,
                'password':user.password,
                'Token': tokens['access'],
                'refresh': tokens['refresh'],
               
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User Create
class Usercreate(GenericAPIView, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        if User.objects.filter(email=request.data.get('email')).exists():
            return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        elif User.objects.filter(phone_number=request.data.get('phone_number')).exists():
            return Response({'error': 'User with this Phone Number already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = self.create(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)
            return response

# Getting Users
class Userget(GenericAPIView, ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

# Updating Users
class Userupdate(GenericAPIView, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'public_id'  # Use 'id' or any other field you want to use for lookup
    permission_classes = [IsAuthenticated]
    def patch(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': 'User updated successfully!'}, status=status.HTTP_200_OK)
        return response

# Image Upload
class Imagecreate(GenericAPIView, CreateModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if Image.objects.filter(user_id=request.data.get('user_id')).exists():
            return Response({'error': 'Profile already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = self.create(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                return Response({'message': 'Image created successfully!'}, status=status.HTTP_201_CREATED)
            return response

# Getting Images
class Imageget(GenericAPIView, ListModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# Updating Images
class Imageupdate(GenericAPIView, UpdateModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'public_id'
    permission_classes = [IsAuthenticated]
    def patch(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': 'Image updated successfully!'}, status=status.HTTP_200_OK)
        return response
    
class Purifier_Model_Create(GenericAPIView,CreateModelMixin):
    queryset=PurifierModel.objects.all()
    serializer_class=PurifierModelSerializer
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        response = self.create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'created successfully!'}, status=status.HTTP_201_CREATED)
        return response
    


class Purifier_Model_Retrive(GenericAPIView,ListModelMixin):
    queryset=PurifierModel.objects.all()
    serializer_class=PurifierModelSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class Purifier_Model_Update(GenericAPIView,UpdateModelMixin):
    queryset=PurifierModel.objects.all()
    serializer_class=PurifierModelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='public_id'
    def patch(self,request,*args,**kwargs):
        response = self.update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': ' updated successfully!'}, status=status.HTTP_200_OK)
        return response
    
class Purifier_Model_Delete(GenericAPIView,DestroyModelMixin):
    queryset=PurifierModel.objects.all()
    serializer_class=PurifierModelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='public_id'
    def delete(self,request,*args,**kwargs):
        response=self.destroy(request,*args,**kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response({'message': ' deleted successfully!'}, status=status.HTTP_200_OK)
        return response
    
#creating Purifiers
    
class Purifier_Details_Create(GenericAPIView,CreateModelMixin):
    queryset=PurifierDetails.objects.all()
    serializer_class=PurifierdeatilsSerializer
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        response=self.create(request,*args,**kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'Message : New Purifier added..!'},status=status.HTTP_201_CREATED)

#Geting Purifiers detatils..
class Purifier_Details_Get(GenericAPIView,ListModelMixin):
    queryset=PurifierDetails.objects.all()
    serializer_class=PurifierdeatilsSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

#Updateing Purifiers details...
class Purifier_Details_Update(GenericAPIView,UpdateModelMixin):
    queryset=PurifierDetails.objects.all()
    serializer_class=PurifierdeatilsSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='public_id'
    def patch(self,request,*args,**kwargs):
        response = self.update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': ' updated successfully!'}, status=status.HTTP_200_OK)
        return response

class Purifier_Details_Delete(GenericAPIView,DestroyModelMixin):
    queryset=PurifierDetails.objects.all()
    serializer_class=PurifierdeatilsSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='public_id'
    def delete(self,request,*args,**kwargs):
        response=self.destroy(request,*args,**kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response({'message': ' deleted successfully!'}, status=status.HTTP_200_OK)
        return response
        

class Address_Create(GenericAPIView,CreateModelMixin):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer
    permission_classes = [IsAuthenticated]
    def post(self,request,*args,**kwargs):
        if Address.objects.filter(user_id=request.data.get('user_id')).exists():
            return Response({'error': 'Profile already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = self.create(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                return Response({'message': 'Address created successfully!'}, status=status.HTTP_201_CREATED)
            return response
class Address_Get(GenericAPIView,ListModelMixin):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
class Address_Get_Id(GenericAPIView,RetrieveModelMixin):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='user_id'
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class Address_Update(GenericAPIView,UpdateModelMixin):
    queryset=Address.objects.all()
    serializer_class=AddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field='public_id'
    def patch(self,request,*args,**kwargs):
        response = self.update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': ' updated successfully!'}, status=status.HTTP_200_OK)
        return response

#create Billinging
class Bill_Generate(GenericAPIView,CreateModelMixin):
    queryset=Billing.objects.all()
    serializer_class=BillingSerializer
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        response=self.create(request,*args,**kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'Message : New Billing Generate..!'},status=status.HTTP_201_CREATED)   
        return response

#getting Billing generate....
class Bill_Get(GenericAPIView,ListModelMixin):
    queryset=Billing.objects.all()
    serializer_class=BillingSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
#create Service...

class Service(GenericAPIView,CreateModelMixin):
    queryset=Servicing.objects.all()
    serializer_class=ServiceSerializer
    permission_classes=[IsAuthenticated]
    def post(self,request,*args,**kwargs):
        response=self.create(request,*args,**kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message: Our request is successfully create ....'},status=status.HTTP_201_CREATED)
        return response
    
#geting services....
class Geting_Service_Details(GenericAPIView,ListModelMixin):
    queryset=Servicing.objects.all()
    serializer_class=ServiceSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

#update service
class Update_Service(GenericAPIView,UpdateModelMixin):
    queryset=Servicing.objects.all()
    serializer_class=ServiceSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='public_id'
    def patch(self,request,*args,**kwargs):
        response = self.update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': ' updated successfully!'}, status=status.HTTP_200_OK)
        return response
class Delete_Service(GenericAPIView,DestroyModelMixin):
    queryset=Servicing.objects.all()
    serializer_class=ServiceSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='public_id'
    def delete(self,request,*args,**kwargs):
        response=self.destroy(request,*args,**kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response({'message': ' deleted successfully!'}, status=status.HTTP_200_OK)
        return response




#Create feedback...
class Feedback_Create(GenericAPIView,CreateModelMixin):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    permission_classes=[IsAuthenticated]
    def post(self, request, *args, **kwargs):
        response=self.create(request,*args,**kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'Message : New Feedback added..!'},status=status.HTTP_201_CREATED)   
        return response

#getting feedback 
class Feedback_Get(GenericAPIView,ListModelMixin):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
# Feedback update  
class Feedback_Update(GenericAPIView,UpdateModelMixin):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='public_id'
    def patch(self,request,*args,**kwargs):
        response = self.update(request,*args,**kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': ' updated successfully!'}, status=status.HTTP_200_OK)
        return response
# Feedback delete
class Feedback_Delete(GenericAPIView,DestroyModelMixin):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer
    permission_classes=[IsAuthenticated]
    lookup_field='public_id'
    def delete(self,request,*args,**kwargs):
        response=self.destroy(request,*args,**kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response({'message': ' deleted successfully!'}, status=status.HTTP_200_OK)
        return response



