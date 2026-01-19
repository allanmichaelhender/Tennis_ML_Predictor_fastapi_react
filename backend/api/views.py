from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Predictions, Players
from .serializers import (
    PredictionsSerializer,
    PredictionsGuestSerializer,
    PlayersSerializer,
)
from .predictor_functions import (
    logistic_regression_predict,
    random_forest_predict,
    decision_tree_predict,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
        p1 = serializer.validated_data.get("player1_id")
        p2 = serializer.validated_data.get("player2_id")
        m_date = serializer.validated_data.get("match_date")

        # Call your prediction functions
        [[p2_log, p1_log]] = logistic_regression_predict(
            player1_id=p1, player2_id=p2, match_date=m_date
        )
        [[p2_rf, p1_rf]] = random_forest_predict(
            player1_id=p1, player2_id=p2, match_date=m_date
        )
        [[p2_dt, p1_dt]] = decision_tree_predict(
            player1_id=p1, player2_id=p2, match_date=m_date
        )

        serializer.save(
            author=self.request.user,
            player1WinOddsLogistic=p1_log,
            player2WinOddsLogistic=p2_log,
            player1WinOddsRForest=p1_rf,
            player2WinOddsRForest=p2_rf,
            player1WinOddsDTree=p1_dt,
            player2WinOddsDTree=p2_dt,
        )


class PredictionsCreateGuest(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = PredictionsGuestSerializer(data=request.data)
        if serializer.is_valid():
            p1 = serializer.validated_data.get("player1_id")
            p2 = serializer.validated_data.get("player2_id")
            m_date = serializer.validated_data.get("match_date")

            # Your prediction functions
            [[p2_log, p1_log]] = logistic_regression_predict(p1, p2, m_date)
            [[p2_rf, p1_rf]] = random_forest_predict(p1, p2, m_date)
            [[p2_dt, p1_dt]] = decision_tree_predict(p1, p2, m_date)

            # Update the validated data with results
            results = serializer.validated_data
            results.update(
                {
                    "player1WinOddsLogistic": p1_log,
                    "player2WinOddsLogistic": p2_log,
                    "player1WinOddsRForest": p1_rf,
                    "player2WinOddsRForest": p2_rf,
                    "player1WinOddsDTree": p1_dt,
                    "player2WinOddsDTree": p2_dt,
                }
            )

            return Response(results, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictionsDelete(generics.DestroyAPIView):
    serializer_class = PredictionsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Predictions.objects.filter(author=user)


class PlayersView(generics.ListAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = [AllowAny]

