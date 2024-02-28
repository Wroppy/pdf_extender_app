from PyPDF2 import PdfReader, PdfWriter

class PDFScaler:
    def __init__(self):
        self.pdf = PdfWriter()

    def write_pdf(self, path: str):
        """
        Given a directory path, write the PDF to the path
        
        :param path: The requested directory of the pdf 
        """ 
        
        with open(path, "wb") as file:
            self.pdf.write(file)

    def scale_pdf(self, pdf_filename: str, scale_factor: float):
        """
        Given a pdf and scaling, increases the whitespace on the right side of the pdf
        by the given factor

        :param pdf_filename: The path to the file of the pdf
        :param scale_factor: The factor at which the file's width increases by
        """
        pdf = PdfReader(pdf_filename)

        new_pdf = PdfWriter()

        # Adds white margin to the right of the screen
        for page in pdf.pages:
            x, y = page.mediabox.lower_right
            page.mediabox.lower_right = (scale_factor * float(x), float(y))

            x, y = page.cropbox.lower_right
            page.cropbox.lower_right = (scale_factor * float(x), float(y))

            new_pdf.add_page(page)

        self.pdf = new_pdf
