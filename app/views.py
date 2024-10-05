from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.conf import settings
import stripe
from django.http import HttpResponse
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
from decouple import config
import time

def product_page(request):
    stripe.api_key = config('STRIPE_SECRET_kEY_TEST')
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1Q5sVMJiwAR9PFp9uFGgpjpr',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=config('REDIRECT_DOMAIN') + 'payment_successfull',
            cancel_url=config('REDIRECT_DOMAIN') + 'payment_cancelled',
        )
        
        return redirect(checkout_session.url, code=303)
            
    return render(request, 'product_page.html')


def success_buy(request):
    # sucesso ao comprar
    stripe.api_key = config('STRIPE_SECRET_KEY_TEST') # Substituir essa parte do settings pela chave da API.
    checkout_session_id = request.GET.get('session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    user_id = request.user.user_id
    user_payment = Payment.objects.get(user=user_id)
    user_payment.stripe_checkout_id = checkout_session_id
    user_payment.save()
    return render(request, 'payment_successful.html', {'customer': customer})

def cancelled_buy(request):
    # erro na transação
    return render(request, 'payment_cancelled.html')

@csrf_exempt
def stripe_webhook(request):
	stripe.api_key = config('STRIPE_SECRET_KEY_TEST')
	time.sleep(10)
	payload = request.body
	signature_header = request.META['HTTP_STRIPE_SIGNATURE']
	event = None
	try:
		event = stripe.Webhook.construct_event(
			payload, signature_header, config('STRIPE_WEBHOOK_SECRET_TEST')
		)
	except ValueError as e:
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError as e:
		return HttpResponse(status=400)
	if event['type'] == 'checkout.session.completed':
		session = event['data']['object']
		session_id = session.get('id', None)
		time.sleep(15)
		user_payment = Payment.objects.get(stripe_checkout_id=session_id)
		user_payment.payment_status = 'completed'
		user_payment.save()
	return HttpResponse(status=200)