# notes/coefficients.py — fichier séparé propre

COEFFICIENTS = {

    # ── 1ère secondaire — Tronc commun ───────────────────────────────
    'tronc_commun': {
        'mathematiques':      {'coeff': 4, 'type': 'principale'},
        'sciences_naturelles':{'coeff': 3, 'type': 'principale'},
        'physique':           {'coeff': 3, 'type': 'principale'},
        'arabe':              {'coeff': 4, 'type': 'principale'},
        'francais':           {'coeff': 3, 'type': 'principale'},
        'anglais':            {'coeff': 3, 'type': 'principale'},
        'histoire_geo':       {'coeff': 2, 'type': 'secondaire'},
        'education_islamique':{'coeff': 2, 'type': 'secondaire'},
        'informatique':       {'coeff': 2, 'type': 'secondaire'},
        'philosophie':        {'coeff': 1, 'type': 'secondaire'},
    },

    # ── 2ème — Section Math/Sciences/Technique (base scientifique) ───
    'scientifique': {
        'mathematiques':      {'coeff': 5, 'type': 'principale'},
        'physique':           {'coeff': 4, 'type': 'principale'},
        'sciences_naturelles':{'coeff': 4, 'type': 'principale'},
        'informatique':       {'coeff': 3, 'type': 'principale'},
        'arabe':              {'coeff': 2, 'type': 'secondaire'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
        'histoire_geo':       {'coeff': 1, 'type': 'secondaire'},
        'philosophie':        {'coeff': 1, 'type': 'secondaire'},
        'sport':              {'coeff': 1, 'type': 'secondaire'},
    },

    # ── 2ème — Économie et Gestion ───────────────────────────────────
    'economique': {
        'economie':           {'coeff': 5, 'type': 'principale'},
        'gestion':            {'coeff': 4, 'type': 'principale'},
        'mathematiques':      {'coeff': 3, 'type': 'principale'},
        'arabe':              {'coeff': 2, 'type': 'secondaire'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
        'histoire_geo':       {'coeff': 1, 'type': 'secondaire'},
        'informatique':       {'coeff': 1, 'type': 'secondaire'},
    },

    # ── 2ème — Lettres ───────────────────────────────────────────────
    'lettres_2': {
        'arabe':              {'coeff': 5, 'type': 'principale'},
        'philosophie':        {'coeff': 4, 'type': 'principale'},
        'histoire_geo':       {'coeff': 4, 'type': 'principale'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
        'mathematiques':      {'coeff': 1, 'type': 'secondaire'},
    },

    # ── Bac — Mathématiques ──────────────────────────────────────────
    'mathematiques': {
        'mathematiques':      {'coeff': 6, 'type': 'principale'},
        'physique':           {'coeff': 5, 'type': 'principale'},
        'informatique':       {'coeff': 3, 'type': 'principale'},
        'sciences_naturelles':{'coeff': 2, 'type': 'secondaire'},
        'philosophie':        {'coeff': 2, 'type': 'secondaire'},
        'arabe':              {'coeff': 2, 'type': 'secondaire'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
        'sport':              {'coeff': 1, 'type': 'secondaire'},
    },

    # ── Bac — Sciences expérimentales ────────────────────────────────
    'sciences_exp': {
        'sciences_naturelles':{'coeff': 6, 'type': 'principale'},
        'physique':           {'coeff': 5, 'type': 'principale'},
        'mathematiques':      {'coeff': 4, 'type': 'principale'},
        'philosophie':        {'coeff': 2, 'type': 'secondaire'},
        'arabe':              {'coeff': 2, 'type': 'secondaire'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
    },

    # ── Bac — Sciences techniques ────────────────────────────────────
    'sciences_tech': {
        'technologie':        {'coeff': 6, 'type': 'principale'},
        'mathematiques':      {'coeff': 4, 'type': 'principale'},
        'physique':           {'coeff': 4, 'type': 'principale'},
        'informatique':       {'coeff': 2, 'type': 'secondaire'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
        'arabe':              {'coeff': 2, 'type': 'secondaire'},
        'philosophie':        {'coeff': 1, 'type': 'secondaire'},
    },

    # ── Bac — Informatique ───────────────────────────────────────────
    'sciences_info': {
        'informatique':       {'coeff': 6, 'type': 'principale'},
        'mathematiques':      {'coeff': 5, 'type': 'principale'},
        'physique':           {'coeff': 4, 'type': 'principale'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
        'arabe':              {'coeff': 2, 'type': 'secondaire'},
        'philosophie':        {'coeff': 1, 'type': 'secondaire'},
    },

    # ── Bac — Économie et Gestion ────────────────────────────────────
    'eco_gestion': {
        'economie':           {'coeff': 6, 'type': 'principale'},
        'gestion':            {'coeff': 5, 'type': 'principale'},
        'mathematiques':      {'coeff': 3, 'type': 'principale'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
        'arabe':              {'coeff': 2, 'type': 'secondaire'},
        'histoire_geo':       {'coeff': 2, 'type': 'secondaire'},
    },

    # ── Bac — Lettres ────────────────────────────────────────────────
    'lettres_bac': {
        'philosophie':        {'coeff': 6, 'type': 'principale'},
        'arabe':              {'coeff': 5, 'type': 'principale'},
        'histoire_geo':       {'coeff': 4, 'type': 'principale'},
        'francais':           {'coeff': 3, 'type': 'secondaire'},
        'anglais':            {'coeff': 3, 'type': 'secondaire'},
    },

    # ── Bac — Sport ──────────────────────────────────────────────────
    'sport_bac': {
        'sport':              {'coeff': 6, 'type': 'principale'},
        'sciences_naturelles':{'coeff': 4, 'type': 'principale'},
        'mathematiques':      {'coeff': 3, 'type': 'principale'},
        'francais':           {'coeff': 2, 'type': 'secondaire'},
        'anglais':            {'coeff': 2, 'type': 'secondaire'},
        'arabe':              {'coeff': 2, 'type': 'secondaire'},
        'philosophie':        {'coeff': 1, 'type': 'secondaire'},
    },
}

# Mapping niveau → section par défaut (quand pas de spécialité)
NIVEAU_TO_SECTION = {
    '7eme':  'college',
    '8eme':  'college',
    '9eme':  'college',
    '1ere':  'tronc_commun',
    '2eme_s': 'scientifique',  # fallback
    '3eme_s': 'mathematiques', # fallback
    '4eme_s': 'mathematiques', # fallback
}