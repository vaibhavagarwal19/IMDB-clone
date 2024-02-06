from rest_framework import serializers
from app1.models import Movie

#########  ModelSerializer ###########

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['name','description']
        # exclude = ['active']

    def get_len_name(self, object):
        length = len(object.name)
        return length



    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value


####### validators    
# def name_length(value):
#         if len(value) < 2: 
#             raise serializers.ValidationError("Name is too short")   
#         return value 

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description =serializers.CharField()
#     active = serializers.BooleanField(read_only=True)

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance , validated_data):    # instance carrries old values and validated_data carries new values
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    ####### field level validation 
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

    ####### object level validation
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and description cannot be same")
    #     else:
    #         return data
        
    