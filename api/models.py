from django.db import models



    
    
class Label(models.Model):
    tracking_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    
class TrackingPackage(models.Model):
       label = models.ForeignKey(Label, on_delete=models.CASCADE)
       latest_update = models.CharField(max_length=255, blank=True, null=True)
       Update_text = models.TextField(blank=True, null=True)
       delivered_or_complain = models.TextField(blank=True, null=True)
       new_location = models.CharField(blank=True, null=True, max_length=255)
       new_location_date = models.CharField(blank=True, null=True, max_length=255)
       Arrived_location = models.CharField(blank=True, null=True, max_length=255)
       Arrived_location_date = models.CharField(blank=True, null=True, max_length=255)
       Add_date_to_next_facility = models.CharField(blank=True, null=True, max_length=255)
       package_arrived_at_Shiparama_Facility = models.TextField(blank=True, null=True)
       package_arrived_at_Shiparama_Facility_date = models.CharField(blank=True, null=True, max_length=255)
       created = models.DateField(auto_now_add=True)
       
       def __str__(self):
            return f'{self.label} - {self.latest_update}'


class Phonealert (models.Model):
    phone = models.CharField(max_length=20)
    tracking_id = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.phone} - {self.tracking_id}"  
    
  

class Complaint(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.track.tracking_id}"

       
       
        
class Support(models.Model):
    address = models.TextField()
    number = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.number} - {self.email}'
        
        



class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

        
