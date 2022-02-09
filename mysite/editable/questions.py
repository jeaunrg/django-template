help = """
Ce fichier contient toutes les questions et réponses qui peuvent être appelées par
l'algorithme. Une infinitée de question peut-être ajoutée et l'ordre n'a pas d'importance.

Chaque question/réponse est de la forme suivante:

'id_question': {
    'question': '<question complète ?>',
    'answers':  ['réponse1', 'réponse2', ...]
},


"""


from .data import ALGO_CHOICES

QUESTIONS = {
    "algo": {
        "question": "Quel algorithme voulez-vous suivre ?",
        "answers": ALGO_CHOICES,
    },
    # --------------------- ANTIPLATELETS ------------------------------#
    "antiplatelets": {
        "question": "Le patient prend-il des anti-agrégants plaquettaires ?",
        "answers": ["Oui", "Non"],
    },
    "aspirin1": {
        "question": "Aspirine en prévention primaire ?",
        "answers": ["Oui", "Non"],
    },
    "aspirin_mono": {
        "question": "Aspirine en monotherapie et prévention secondaire ?",
        "answers": ["Oui", "Non"],
    },
    "clopi_mono": {
        "question": "Clopidogrel en monotherapie et prévention secondaire ?",
        "answers": ["Oui", "Non"],
    },
    "stent_bitherapy": {
        "question": "Bithérapie pour les stents coronaires ?",
        "answers": ["Oui", "Non"],
    },
    "stent_condition": {
        "question": """Un de ces critères est-il vrai ?
    Stent <1 mois
    Stent <6 mois avec un haut risque de thrombose
    Infarctus du myocarde <6 mois""",
        "answers": ["Oui", "Non"],
    },
    # --------------------- VKA ------------------------------#
    "vka": {"question": "Le patient prend-il des VKA ?", "answers": ["Oui", "Non"]},
    "thromboembolism_risk": {
        "question": "Quel est le risque de thromboemobolisme ?",
        "answers": ["faible", "élevé"],
    },
    # --------------------- DOAC ------------------------------#
    "doac": {"question": "Le patient prend-il des DOAC ?", "answers": ["Oui", "Non"]},
    "xaban": {"question": "Le patient prend-il des xaban ?", "answers": ["Oui", "Non"]},
    "dabigatran": {
        "question": "Le patient prend-il du dabigatran ?",
        "answers": ["Oui", "Non"],
    },
    "cockroft_1": {"question": "Cockroft > 30mL/min", "answers": ["Oui", "Non"]},
    "cockroft_2": {
        "question": "Cockroft",
        "answers": ["<30 mL/min", "30-49 mL/min", "> 50 mL/min"],
    },
    "venous_thrombo": {
        "question": "Un thrombophylaxis veineux est-il indiqué ?",
        "answers": ["Oui", "Non"],
    },
    # --------------------- Autre ------------------------------#
    "bleeding_risk": {
        "question": "Quel est le risque d'hémorragie pendant l'opération ?",
        "answers": ["faible", "intermédiaire", "élevé"],
    },
    "bleeding_risk2": {
        "question": "Quel est le risque d'hémorragie pendant l'opération ?",
        "answers": ["faible", "élevé"],
    },
}
