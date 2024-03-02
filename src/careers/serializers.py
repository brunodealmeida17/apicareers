from rest_framework import serializers

from .models import Career



class CareerSerializer(serializers.ModelSerializer):   
    """
    Serializer for the Career model.

    This serializer is used to convert Career model instances into JSON representations.

    Attributes:
        id (int): The unique identifier for the career.
        username (str): The username of the career owner.
        create_datetime (datetime): The datetime when the career was created.
        title (str): The title of the career.
        content (str): The content of the career.
    """
     
    class Meta:
        model = Career
        fields = (
            'id',
            'username',
            'create_datetime',
            'title',
            'content',
           
        )
