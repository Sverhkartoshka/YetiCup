from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Championship
from .models import Team, Participant, Score

from .serializers import UsersSerializer
from .serializers import ChampionshipsSerializer
from .serializers import TeamsSerializer, ParticipantsSerializer, ScoreSerializer

class LogView(APIView):
    def post(self, request):
        user = request.data.get('user')
        if User.objects.filter(phone = user["phone"]).exists():
            usercheck = get_object_or_404(User.objects.all(), phone = user["phone"])
            if (usercheck.password == user["password"]):
                return Response("OK")
            else:
                return Response("NoPass")
        else:
            return Response("NoUser")

class RegView(APIView):
    def post(self, request):
        user = request.data.get('user')
        serializer = UsersSerializer(data=user)
        if User.objects.filter(phone = user["phone"]).exists():
            return Response(False)
        else:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(True)


class ProfileView(APIView):
    def get(self, request, pk):
        profile = get_object_or_404(User.objects.all(), pk=pk)
        serializer = UsersSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_profile = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data.get('profile')
        serializer = UsersSerializer(instance=saved_profile, data=data, 
                     partial=True)
        
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({
            "success": "Profile updated successfully"
        })
    
    def delete(self, request, pk):
        article = get_object_or_404(User.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Profile with id `{}` has been deleted".format(pk)
        }, status=204)

class TimelineView(APIView):
    def get(self, request):
        events = Championship.objects.all().order_by("date_id")
        serializer = ChampionshipsSerializer(events, many=True)
        return Response(serializer.data)


