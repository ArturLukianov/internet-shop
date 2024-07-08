import telebot
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product, Review

from .config import API_TOKEN, CHAT_ID

bot = telebot.TeleBot(API_TOKEN)


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {
        'products': products
    })

def view_product(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        review = Review(author=author, rating=int(rating), text=text, product=product)
        review.save()

    reviews = product.review_set.all()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews
    })


def payment(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get('fullname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        print(name, address, phone)
        bot.send_message(CHAT_ID, f'''💸 Заказ: {product.name} ({product.price} рублей)
        
ФИО заказчика: {name}
Адрес доставки: {address}
Телефон: {phone}''')
        return redirect('/success')


    return render(request, 'payment.html', {
        'product': product
    })

def payment_success(request):
    return render(request, 'success.html')