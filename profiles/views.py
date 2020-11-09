from rest_framework import response, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProfileSerializer


class SignupView(views.APIView):
    def post(self, request):
        serialzier = ProfileSerializer(data=request.data)
        if serialzier.is_valid():
            profile = serialzier.save()
            refresh = RefreshToken.for_user(profile.user)
            data = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return response.Response(data, status.HTTP_201_CREATED)

        return response.Response(
            serialzier.errors, status.HTTP_400_BAD_REQUEST
        )


class MeView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        request.user
        phones = [
            {
                "number": p.number,
                "area_code": p.area_code,
                "country_code": p.country_code,
            }
            for p in request.user.profile.phones.all()
        ]
        data = {
            "first_name": request.user.profile.first_name,
            "last_name": request.user.profile.last_name,
            "email": request.user.email,
            "phones": phones,
            "created_at": request.user.created_at,
            "last_login": request.user.last_login,
        }
        return response.Response(data, status=status.HTTP_200_OK)
