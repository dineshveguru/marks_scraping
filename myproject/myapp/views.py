from django.shortcuts import render

# Create your views here.


def calculate(request):
    if request.method == "POST":
        num1 = int(request.POST["num1"])
        num2 = int(request.POST["num2"])
        result = num1 + num2
        return render(request, "myapp/result.html", {"result": result})
    return render(request, "myapp/calculate.html")
