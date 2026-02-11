import PyPDF2
import docx

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        page_text= page.extract_text()
        if page_text:
            text += page_text
    return text


def extract_text_from_docx(file):
    doc = docx.Dcoument(file)
    return "\n".join(p.text for p in doc.paragraphs)



