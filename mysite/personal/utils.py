import os
import random

import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template

# pdf options, https://wkhtmltopdf.org/usage/wkhtmltopdf.txt for more options
PDF_OPTIONS = {
    "page-size": "A4",
    "margin-top": "0in",
    "margin-right": "0in",
    "margin-bottom": "0in",
    "margin-left": "0in",
}


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
