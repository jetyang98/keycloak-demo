from django.shortcuts import HttpResponse

# Create your views here.
def admin(request):
    return HttpResponse("only admin can see")


def customer(request):
    return HttpResponse("only customer can see")
