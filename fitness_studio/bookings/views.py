from rest_framework import generics, status
from rest_framework.response import Response
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils import timezone
from django.db.models import Q
from rest_framework.views import APIView


class FitnessClassListView(generics.ListAPIView):
    serializer_class = FitnessClassSerializer

    def get_queryset(self):
        queryset = FitnessClass.objects.filter(datetime__gt=timezone.now())

        # Timezone conversion if provided
        timezone_param = self.request.query_params.get('timezone', None)
        if timezone_param:
            # Note: Actual conversion happens in serializer
            pass

        return queryset


class BookClassView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Update available slots
        fitness_class = serializer.validated_data['fitness_class']
        fitness_class.available_slots -= 1
        fitness_class.save()

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ClientBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        email = self.request.query_params.get('email')
        if not email:
            return Booking.objects.none()

        # Remove the future classes filter to show all bookings
        return Booking.objects.filter(
            client_email=email
        ).select_related('fitness_class')