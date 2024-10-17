from rest_framework import serializers
from .models import User,Image,PurifierModel,PurifierDetails,Feedback,Address
from .models import Billing,Servicing

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'




class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                print("\nUser is not exist\n")
                raise serializers.ValidationError("Invalid email or password")
            print("\npassword is...!",user.password)
            if user.password!=password:
                print("worng password..!",password,"\n")
                raise serializers.ValidationError("Invalid email or password")
            
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("Both fields are required")



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'


class PurifierModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurifierModel
        fields='__all__'
    
class PurifierdeatilsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurifierDetails
        fields='__all__'

    
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields='__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'
class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Billing
        fields='__all__'
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicing
        fields='__all__'
