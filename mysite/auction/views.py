from rest_framework import viewsets, permissions
from .models import UserProfile, Category, CarMake, Model, Car, Bet, Comment
from .serializers import *
from allauth.account.views import SignupView
from .forms import CustomSignupForm


class CustomSignupView(SignupView):
    form_class = CustomSignupForm


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        user_profile = self.get_object()
        if user_profile.user == self.request.user:
            serializer.save()
        else:
            # Если пользователь не является владельцем профиля, вы можете выбрать, как обрабатывать это,
            # например, возвращать ошибку или проигнорировать запрос.
            # В этом примере я возвращаю ошибку 403 Forbidden.
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Вы не можете изменить профиль другого пользователя")



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        if instance.user == self.request.user:
            serializer.save()
        else:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Вы не можете изменить машину другого пользователя")


class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)