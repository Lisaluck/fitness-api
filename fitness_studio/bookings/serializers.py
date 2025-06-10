from rest_framework import serializers
from .models import FitnessClass, Booking
from django.utils import timezone


class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'datetime', 'instructor', 'capacity', 'available_slots']


class BookingSerializer(serializers.ModelSerializer):
    class_details = FitnessClassSerializer(source='fitness_class', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email', 'booking_time', 'class_details']
        extra_kwargs = {
            'fitness_class': {'write_only': True},
        }

    def validate(self, data):
        fitness_class = data['fitness_class']

        # Check if class is in future
        if fitness_class.datetime < timezone.now():
            raise serializers.ValidationError("Cannot book past classes")

        # Check available slots
        if fitness_class.available_slots <= 0:
            raise serializers.ValidationError("No available slots")

        # Check if user already booked this class
        if Booking.objects.filter(
                fitness_class=fitness_class,
                client_email=data['client_email']
        ).exists():
            raise serializers.ValidationError("You have already booked this class")

        return data