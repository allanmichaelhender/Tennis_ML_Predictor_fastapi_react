from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Predictions, Players
from .serializers import PredictionsSerializer, PlayersSerializer
from .predictor_functions import logistic_regression_predict, random_forest_predict, decision_tree_predict

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PredictionsListCreate(generics.ListCreateAPIView):
    serializer_class = PredictionsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Predictions.objects.filter(author=user)
    
    def perform_create(self, serializer):
        # Access the data from validated_data
        p1 = serializer.validated_data.get('player1_id')
        p2 = serializer.validated_data.get('player2_id')
        m_date = serializer.validated_data.get('match_date')

        print("here")
        # Call your prediction functions
        [p2_log, p1_log] = logistic_regression_predict(player1_id=p1, player2_id=p2, match_date=m_date)
        # [p2_rf, p1_rf] = random_forest_predict(player1_id=p1, player2_id=p2, match_date=m_date)
        # [p2_dt, p1_dt] = decision_tree_predict(player1_id=p1, player2_id=p2, match_date=m_date)
        print("here2")
        print(p2_log,p1_log)

        serializer.save(
            author=self.request.user,
            player1WinOddsLogistic=p1_log,
            player2WinOddsLogistic=p2_log,
            # player1WinOddsRForest=p1_rf,
            # player2WinOddsRForest=p2_rf,
            # player1WinOddsDTree=p1_dt,
            # player2WinOddsDTree=p2_dt
        )

class PredictionsDelete(generics.DestroyAPIView):
    serializer_class = PredictionsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Predictions.objects.filter(author=user)

class PlayersView(generics.ListAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    


