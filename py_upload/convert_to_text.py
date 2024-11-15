import fitz


class PDFLoader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):
        doc = fitz.open(self.pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text


def convert_pdf_to_text():
    loader = PDFLoader(
        '../public/pdf/spec-book-0924.pdf')
    text = loader.extract_text()
    return text
