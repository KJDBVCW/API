# views.py
from django.shortcuts import render, redirect
from .models import Drink
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import DrinkSerializer
from rest_framework.permissions import AllowAny
# ViewSet cho đồ uống
class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [AllowAny]
# Hàm thêm món đồ uống
def add_item(request):
    if request.method == "POST":
        # Lấy dữ liệu từ form POST
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image_url = request.POST.get('image_url', '')

        # Lưu vào cơ sở dữ liệu
        try:
            drink = Drink.objects.create(
                name=name,
                price=price,
                description=description,
                image_url=image_url
            )
            return redirect('home')  # Chuyển hướng về trang chủ sau khi thêm món

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    # Xử lý GET request, trả về form thêm món đồ uống
    return render(request, 'drinks_api/add.html')
# Hàm view cho trang chủ
def home(request):
    return render(request, 'drinks_api/home.html')
