from rest_framework import serializers

from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id','name', 'cuisine', 'location')
