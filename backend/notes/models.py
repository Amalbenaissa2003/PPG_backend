from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from .coefficients import COEFFICIENTS, NIVEAU_TO_SECTION


class NotesEleve(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    # ── Toutes les matières possibles (nullable) ─────────────────
    mathematiques         = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    physique              = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    sciences_naturelles   = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    informatique          = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    technologie           = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    arabe                 = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    francais              = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    anglais               = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    philosophie           = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    histoire_geo          = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    education_islamique   = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    economie              = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    gestion               = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    sport                 = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(20)])

    # ── Indicateurs calculés ─────────────────────────────────────
    moyenne_generale      = models.FloatField(null=True, blank=True)
    moyenne_ponderee      = models.FloatField(null=True, blank=True)  # avec coefficients
    niveau_global         = models.CharField(max_length=20, blank=True)
    points_forts          = models.JSONField(default=list, blank=True)
    points_faibles        = models.JSONField(default=list, blank=True)
    score_scientifique    = models.FloatField(null=True, blank=True)
    score_litteraire      = models.FloatField(null=True, blank=True)
    score_economique      = models.FloatField(null=True, blank=True)
    score_informatique    = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Notes élève'

    def __str__(self):
        return f"Notes de {self.user.get_full_name()}"

    def _get_section_key(self):
        """Détermine la clé de section selon niveau + spécialité de l'user."""
        spec  = getattr(self.user, 'specialite', None)
        niveau = getattr(self.user, 'niveau', None)
        if spec and spec in COEFFICIENTS:
            return spec
        return NIVEAU_TO_SECTION.get(niveau, 'tronc_commun')

    def calculer_indicateurs(self):
        section_key = self._get_section_key()
        coeffs      = COEFFICIENTS.get(section_key, {})

        # Toutes les notes disponibles
        ALL_FIELDS = [
            'mathematiques','physique','sciences_naturelles','informatique',
            'technologie','arabe','francais','anglais','philosophie',
            'histoire_geo','education_islamique','economie','gestion','sport',
        ]
        notes_dispo = {f: getattr(self, f) for f in ALL_FIELDS if getattr(self, f) is not None}

        if not notes_dispo:
            return

        # ── Moyenne simple (toutes matières saisies) ──────────────
        self.moyenne_generale = round(
            sum(notes_dispo.values()) / len(notes_dispo), 2
        )

        # ── Moyenne pondérée (selon coefficients de la section) ───
        total_points = 0
        total_coeffs = 0
        for mat, note in notes_dispo.items():
            coeff = coeffs.get(mat, {}).get('coeff', 1)
            total_points += note * coeff
            total_coeffs += coeff

        self.moyenne_ponderee = round(total_points / total_coeffs, 2) if total_coeffs else None

        # ── Niveau global (basé sur moyenne pondérée) ─────────────
        m = self.moyenne_ponderee or self.moyenne_generale
        if m >= 16:   self.niveau_global = 'Excellent'
        elif m >= 13: self.niveau_global = 'Bien'
        elif m >= 10: self.niveau_global = 'Passable'
        else:         self.niveau_global = 'Insuffisant'

        # ── Points forts / faibles ────────────────────────────────
        self.points_forts  = [k for k, v in notes_dispo.items() if v >= 14]
        self.points_faibles = [k for k, v in notes_dispo.items() if v < 10]

        # ── Scores domaines (moyenne pondérée par domaine) ────────
        def score_domaine(matieres_domaine):
            items = [(mat, notes_dispo[mat], coeffs.get(mat, {}).get('coeff', 1))
                     for mat in matieres_domaine if mat in notes_dispo]
            if not items:
                return None
            return round(
                sum(n * c for _, n, c in items) / sum(c for _, _, c in items), 2
            )

        self.score_scientifique = score_domaine(['mathematiques','physique','sciences_naturelles'])
        self.score_informatique = score_domaine(['mathematiques','physique','informatique'])
        self.score_litteraire   = score_domaine(['francais','arabe','anglais','philosophie','histoire_geo'])
        self.score_economique   = score_domaine(['mathematiques','economie','gestion','anglais','francais'])

    def save(self, *args, **kwargs):
        self.calculer_indicateurs()
        super().save(*args, **kwargs)