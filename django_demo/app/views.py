from django.shortcuts import HttpResponse, redirect
from django.http.request import HttpRequest
from django.http import HttpResponseForbidden
from django_demo import settings
import jwt
from jwt import PyJWKClient

jwks_client = PyJWKClient(settings.JWKS_ENDPOINT)


def verify(request: HttpRequest, role: str):
    token = request.headers.get("Authorization", None)
    if(token == None or token[:7] != "Bearer "):
        return False

    token = token[7:]
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    data = jwt.decode(
        token,
        signing_key.key,
        algorithms = ["RS256"],
        audience = "account",
        issuer = "http://127.0.0.1:8080/auth/realms/demo"
    )
    roles = data.get("realm_access", {"roles": []}).get("roles", [])

    return role in roles

# Create your views here.
def admin(request):
    if(not verify(request, "ROLE_ADMIN")):
        return HttpResponseForbidden("403 Forbidden")

    return HttpResponse("only admin can see")



def customer(request):
    if(not verify(request, "ROLE_CUSTOMER")):
        return HttpResponseForbidden("403 Forbidden")

    return HttpResponse("only customer can see")
