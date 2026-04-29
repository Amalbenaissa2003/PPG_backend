from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import NotesEleve
from .coefficients import COEFFICIENTS, NIVEAU_TO_SECTION

User = get_user_model()

LABELS = {
    'mathematiques':'Mathématiques','physique':'Physique',
    'sciences_naturelles':'Sciences naturelles','informatique':'Informatique',
    'technologie':'Technologie','arabe':'Arabe','francais':'Français',
    'anglais':'Anglais','philosophie':'Philosophie','histoire_geo':'Histoire-Géo',
    'education_islamique':'Éd. islamique','economie':'Économie',
    'gestion':'Gestion','sport':'Sport',
}

class NotesEleveSerializer(serializers.ModelSerializer):
    points_forts_labels   = serializers.SerializerMethodField()
    points_faibles_labels = serializers.SerializerMethodField()
    coefficients_section  = serializers.SerializerMethodField()  # ← renvoie les coeffs au front

    class Meta:
        model  = NotesEleve
        fields = [
            # Notes
            'mathematiques','physique','sciences_naturelles','informatique',
            'technologie','arabe','francais','anglais','philosophie',
            'histoire_geo','education_islamique','economie','gestion','sport',
            # Indicateurs (read-only)
            'moyenne_generale','moyenne_ponderee','niveau_global',
            'points_forts','points_faibles',
            'points_forts_labels','points_faibles_labels',
            'score_scientifique','score_litteraire',
            'score_economique','score_informatique',
            'coefficients_section',
            'updated_at',
        ]
        read_only_fields = [
            'moyenne_generale','moyenne_ponderee','niveau_global',
            'points_forts','points_faibles',
            'points_forts_labels','points_faibles_labels',
            'score_scientifique','score_litteraire',
            'score_economique','score_informatique',
            'coefficients_section','updated_at',
        ]

    def get_points_forts_labels(self, obj):
        return [LABELS.get(m, m) for m in obj.points_forts]

    def get_points_faibles_labels(self, obj):
        return [LABELS.get(m, m) for m in obj.points_faibles]

    def get_coefficients_section(self, obj):
        """Renvoie les coefficients de la section de l'élève au frontend."""
        spec   = getattr(obj.user, 'specialite', None)
        niveau = getattr(obj.user, 'niveau', None)
        key    = spec if (spec and spec in COEFFICIENTS) else NIVEAU_TO_SECTION.get(niveau, 'tronc_commun')
        return COEFFICIENTS.get(key, {})

    def validate(self, attrs):
        # Au moins 2 matières saisies
        notes_saisies = [k for k, v in attrs.items() if v is not None]
        if len(notes_saisies) < 2:
            raise serializers.ValidationError("Saisis au moins 2 matières.")
        return attrs