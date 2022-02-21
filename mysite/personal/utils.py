import os
import random

import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template
from editable.settings import PDF_OPTIONS


def generate_pdf(template, context={}, save_filename="outut.pdf", download=False):
    template = get_template(template)
    html = template.render(context)
    pdfkit.from_string(html, "tmp.pdf", options=PDF_OPTIONS)
    pdf = open("tmp.pdf", "rb")
    response = HttpResponse(pdf.read(), content_type="application/pdf")
    if download:
        response["Content-Disposition"] = "attachment; filename={}".format(
            save_filename
        )
    pdf.close()
    os.remove("tmp.pdf")
    return response
