def get_default_results(patient):
    """
    Cette fonction est appelée avant de lancer l'algorithme pour répondre
    automatiquement aux questions, dans le cas ou l'information est accessible.
    Cette fonction n'est pas appelée lorsqu'on clique sur "Quel traitement arrêter et comment ? (algorithme complet)"

    Argument
    --------
    patient: patient.model.Patient

    Return
    ------
    results: dict
        Dictionnaire contenant certaines réponses de l'algorithme remplies en avance.
        La clé est l'ID de la question définie dans questions.QUESTIONS.
        La valeur est la réponse à la question.

    """
    results = {
        "antiplatelets": "Non",
        "aspirin1": "Non",
        "aspirin_mono": "Non",
        "clopi_mono": "Non",
        "stent_bitherapy": "Non",
        "vka": "Non",
        "doac": "Non",
        "xaban": "Non",
        "dabigatran": "Non",
    }

    for values in patient.traitements.values():
        print("")
        print(values)
        if "Antiagregant plaquettaire" in values["flags"]:
            results["antiplatelets"] = "Oui"

        if (
            values["traitement"] == "Aspirine, Asaflow, Cardioaspirine"
            and values["pathologie"] == "Prévention primaire"
        ):
            results["aspirin1"] = "Oui"

        if (
            values["traitement"] == "Aspirine, Asaflow, Cardioaspirine"
            and values["pathologie"] == "Prévention secondaire"
        ):  # TO DO: and monotherapy
            results["aspirin_mono"] = "Oui"

        if (
            values["traitement"] == "Clopidogrel, PLAVIX"
            and values["pathologie"] == "Prévention secondaire"
        ):  # TO DO: and monotherapy
            results["clopi_mono"] = "Oui"

        if values["pathologie"] == "Stents Cardiaques":
            results["stent_bitherapy"] = "Oui"

        if "AVK" in values["flags"]:
            results["vka"] = "Oui"

        if "ACOD" in values["flags"]:
            results["doac"] = "Oui"

        if "xaban" in values["flags"]:
            results["xaban"] = "Oui"

        if values["traitement"] == "Dabigatran, PRADAXA":
            results["dabigatran"] = "Oui"

    if patient.bleeding_risk:
        results["bleeding_risk"] = patient.bleeding_risk
        if patient.bleeding_risk != "intermédiaire":
            results["bleeding_risk2"] = patient.bleeding_risk
    print(results)
    return results
