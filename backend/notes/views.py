from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import NotesEleve
from .serializers import NotesEleveSerializer


class NotesView(APIView):
    """
    GET    /api/notes/   → récupère les notes de l'utilisateur connecté
    POST   /api/notes/   → crée ou met à jour les notes (upsert)
    DELETE /api/notes/   → supprime les notes
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            notes = NotesEleve.objects.get(user=request.user)
            return Response(NotesEleveSerializer(notes).data)
        except NotesEleve.DoesNotExist:
            return Response(
                {"detail": "Aucune note saisie pour le moment."},
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request):
        """Crée ou met à jour les notes (upsert)."""
        try:
            notes = NotesEleve.objects.get(user=request.user)
            serializer = NotesEleveSerializer(notes, data=request.data, partial=True)
        except NotesEleve.DoesNotExist:
            serializer = NotesEleveSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message": "Notes sauvegardées avec succès ✅",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            NotesEleve.objects.get(user=request.user).delete()
            return Response({"message": "Notes supprimées."})
        except NotesEleve.DoesNotExist:
            return Response({"detail": "Aucune note à supprimer."}, status=status.HTTP_404_NOT_FOUND)
