from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw 
#-*- coding: future_fstrings -*-

# Create your models here.
class Website(models.Model):
		name = models.CharField(max_length=200)
		qr_code = models.ImageField(upload_to='qr_codes', blank=True)

		def __str__(self):
				return str(self.name)

		def save(self, *args, **kwargs):
				qrcode_img = qrcode.make(self.name)
				canvas = Image.new('RGB', (290, 290), 'white')
				draw = ImageDraw.Draw(canvas)
				canvas.paste(qrcode_img)
				fname = 'qr_code-{self.name}.png'
				buffer = BytesIO()
				canvas.save(buffer,'PNG')
				self.qr_code.save(fname, File(buffer), save=False)
				canvas.close()
				super().save(*args, **kwargs)
				

class MenuItem(models.Model):
		name = models.CharField(max_length=100)
		description = models.TextField()
		image = models.ImageField(upload_to='menu_images/')
		price = models.DecimalField(max_digits=10, decimal_places=2)
		category = models.ManyToManyField('Category', related_name='item')

		def __str__(self):
				return self.name

class Category(models.Model):
		name = models.CharField(max_length=100)

		def __str__(self):
				return self.name

class OrderModel(models.Model):
		created_on = models.DateTimeField(auto_now_add=True)
		price = models.DecimalField(max_digits=10, decimal_places=2)
		items = models.ManyToManyField(
				'MenuItem', related_name='order', blank=True)
		name = models.CharField(max_length=50, blank=True)
		table = models.IntegerField(max_length=20, blank=True, null=True)
		is_paid = models.BooleanField(default=False)
		is_sent = models.BooleanField(default=False)
		
		
		def __str__(self):
				# return 'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
				return self.name




















