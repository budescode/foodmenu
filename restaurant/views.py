from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel
from .models import MenuItem, Category


class Signup(View):
		def get(self, request, *args, **kwargs):
				if request.method == 'POST':
						form = UserCreationForm(request.POST)
						if form.is_valid():
								form.save()
								return redirect('Index')
				else:
						form = UserCreationForm()
				return render(request, 'registration/signup.html',{
				'form': form
})

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
		def get(self, request, *args, **kwargs):
				#get the current date
				today = datetime.today()
				orders = OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

				#loop through the orders and add the price value, check if order is not sent
				unsent_orders = []
				total_revenue = 0
				for order in orders:
						total_revenue += order.price

						if not order.is_sent:
								unsent_orders.append(order)

				#pass total number of orders and total revenue into template
				context = {
						'orders': unsent_orders,
						'total_revenue': total_revenue,
						'total_orders': len(orders)
				}

				return render(request, 'restaurant/dashboard.html', context)

		def test_func(self):
				return self.request.user.groups.filter(name='Staff').exists()

class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
		def get(self, request, pk, *args, **kwargs):
				order = OrderModel.objects.get(pk=pk)
				context = {
						'order': order
				}
				
				return render(request, 'restaurant/order-details.html', context)
			
		def post(self, request, pk, *args, **kwargs):
				order = OrderModel.objects.get(pk=pk)
				order.is_sent = True
				order.save()

				context = {
						'order': order
				}

				return render(request, 'restaurant/order-details.html', context)


		def test_func(self):
				return self.request.user.groups.filter(name='Staff').exists()






















