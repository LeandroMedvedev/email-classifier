import pdfplumber


class FileReader:
    @staticmethod
    def read_txt(file) -> str:
        return file.read().decode("utf-8")

    @staticmethod
    def read_pdf(file) -> str:
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text
