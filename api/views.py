from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Label, TrackingPackage
from rest_framework.permissions import AllowAny
from .serializers import LabelSerializer, TrackingPackageSerializer, ContactMessageSerializer, PhonealertSerializer



class LabelAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """
        Optional: List all labels
        """
        labels = Label.objects.all()
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new label. Email is sent automatically via signals.
        """
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            # Save the label instance
            label = serializer.save()

            # At this point, your post_save signal will trigger and send the email
            # No need to call send_email_to_user here

            return Response(
                {
                    "message": "Label created successfully",
                    "label": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TrackingAPIView(APIView):
    permission_classes = [AllowAny]  # Allow access to anyone

    def get(self, request, tracking_id):
        try:
            # Try to find the Label object by the tracking_id
            track = Label.objects.get(tracking_id=tracking_id)
        except Label.DoesNotExist:
            # Return an error if the tracking_id doesn't exist
            return Response(
                {"error": "Invalid tracking ID, label not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Get related TrackingPackage objects
        packages = TrackingPackage.objects.filter(label=track)

        # Serialize the Label data
        track_data = LabelSerializer(track).data

        # Serialize the related TrackingPackage objects
        package_data = TrackingPackageSerializer(packages, many=True).data

        # Return the response containing both the label and the packages
        return Response({
            "track": track_data,
            "packages": package_data  # will be empty list if no packages
        })





class PingAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "pong"})
    
    
    

# views.py


class ContactAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # triggers signal to send email
            return Response({"message": "Message sent successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



# class PhonealertAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = PhonealertSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "Alert set"})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhonealertAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Request Data:", request.data)  # Log incoming data for debugging
        serializer = PhonealertSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Alert set"})
        else:
            print("Validation errors:", serializer.errors)  # Print validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
