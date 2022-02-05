from ast import Try
from mailbox import mbox
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import pre_save, post_save
from django.db.models import Sum
from django.dispatch.dispatcher import receiver




GENDER_CHOICES = (
    ('PREFER NOT TO MENTION', 'PREFER NOT TO MENTION'),
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
)

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Date of birth', null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.username}'



class Address(models.Model):
    user = models.ForeignKey(MyUser, related_name='user_address',on_delete=models.CASCADE)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    is_current = models.BooleanField(default=True)
    is_permanent = models.BooleanField()

    def __str__(self) -> str:
        return f'{self.address1} {self.address2} {self.state} {self.city} {self.zip_code}'

# @receiver(post_save, sender=Address)
# def update_address(sender, instance, **kwargs):
#     """Aggregates from number of hours on Employee Logs"""
#     id = instance.employee.id
#     number_of_hours = MyUser.objects.filter(employee = instance.employee).aggregate(Sum('number_of_hours_today'))
#     salary_data = Salary.objects.get(staff_id=id)
#     salary_data.number_of_hours = number_of_hours['number_of_hours_today__sum']
#     salary_data.save()

class Contact(models.Model):
    user = models.ForeignKey(MyUser,related_name='user_contact',on_delete=models.CASCADE)
    number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user} {self.number}'


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='profiles/', null=True, default='default-image.png')
    address = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    
@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created,**kwargs):
    """Create a profile after signup"""
    if created:
        Profile.objects.create(user = instance)
        