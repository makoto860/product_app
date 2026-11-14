from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    # 商品一覧を取得
    products = Products.objects.all()

    # HTMLに商品データを渡す
    return render(request, 'products/index.html', {
        'products': products
    })
