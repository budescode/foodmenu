import json
from django.shortcuts import render, redirect
from django.views import View
from django .db.models import Q
from .models import MenuItem, Category, OrderModel

# Create your views here.
class Index(View):
		def get(self, request, *args, **kwargs):
				return render(request, 'customer/index.html')

class About(View):
		def get(self, request, *args, **kwargs):
				return render(request, 'customer/about.html')

class Order(View):
		def get(self, request, *args, **kwargs):
				#get every item from each category
				meals = MenuItem.objects.filter(category__name__contains='Meal')
				drinks = MenuItem.objects.filter(category__name__contains='Drink')

				# pass into context
				context = {
						'meals': meals,
						'drinks': drinks,
				}
				# render into template
				return render(request, 'customer/order.html', context)

		def post(self, request, *args, **kwargs):
				order_items = {
						'items': []
				}

				items = request.POST.getlist('items[]')

				for item in items:
						menu_item = MenuItem.objects.get(pk__contains=int(item))
						item_data = {
								'id': menu_item.pk,
								'name': menu_item.name,
								'price': menu_item.price,
						}
						
						order_items['items'].append(item_data)
						
						price = 0
						item_ids = []

				for item in order_items['items']:
						price += item['price']
						item_ids.append(item['id'])
						
				order = OrderModel.objects.create(price=price)
				order.items.add(*item_ids)

				context = {
						'items': order_items['items'],
						'price': price
				}
						
				return render(request, 'customer/order_confirmation.html', context)

class Menu(View):
		def get(self, request, *args, **kwargs):
				menu_items = MenuItem.objects.all()

				context = {
						'menu_items': menu_items				
				}
				
				return render(request, 'customer/menu.html', context)

class MenuSearch(View):
		def get(self, request, *args, **kwargs):
				query = self.request.GET.get("q")

				menu_items = MenuItem.objects.filter(
						Q(name__icontains=query) |
						Q(price__icontains=query) |
						Q(description__icontains=query)
				)

				context = {
						'menu_items': menu_items
				}

				return render(request, 'customer/menu.html', context)

















		
