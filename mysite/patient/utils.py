from operator import attrgetter

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from .models import Patient


def get_patients_queryset(query=None, **kwargs):
    if query == "#all#":
        query = ""

    queryset = []
    queries = query.split(" ")

    ref_patients = Patient.objects.filter(**kwargs)

    for q in queries:
        patients = Patient.objects.filter(
            Q(incl_num__icontains=q)
            | Q(firstname__icontains=q)
            | Q(lastname__icontains=q)
            | Q(intervention__icontains=q)
            | Q(chirurgie__icontains=q)
            | Q(chirurgien__icontains=q)
        ).distinct()

        for patient in patients:
            if patient in ref_patients:
                queryset.append(patient)

    return list(set(queryset))


def get_patients_page(
    request, patients_per_page=10, filter="is_author", sort_by="date_updated"
):

    query = request.GET.get("q", "")
    kwargs = {}
    if filter == "is_author":
        kwargs["author"] = request.user

    patients = sorted(
        get_patients_queryset(query, **kwargs), key=attrgetter(sort_by), reverse=True
    )

    # Pagination
    page = request.GET.get("page", 1)
    patients_paginator = Paginator(patients, patients_per_page)
    try:
        patients = patients_paginator.page(page)
    except PageNotAnInteger:
        patients = patients_paginator.page(patients_per_page)
    except EmptyPage:
        patients = patients_paginator.page(patients_paginator.num_pages)
    if query == "":
        query = "#all#"
    return query, patients
