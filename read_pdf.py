from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

class ReadPdf():
    """Reads pdf and returns text from it."""
    def __init__(self) -> None:
        self.rsrcmgr = PDFResourceManager()
        self.retstr = StringIO()
        self.laparams = LAParams()
        self.device = TextConverter(self.rsrcmgr, self.retstr, laparams=self.laparams)
        self.interpreter = PDFPageInterpreter(self.rsrcmgr,self.device)
        self.password = ""
        self.maxpages = 0
        self.caching = True
        self.pagenos=set()

    def convert_pdf_to_txt(self, path):
        self.fp = open(path, 'rb')
        for page in PDFPage.get_pages(self.fp, self.pagenos, maxpages=self.maxpages, password=self.password, caching=self.caching, check_extractable=True):
            self.interpreter.process_page(page)
        text = self.retstr.getvalue()
        self.fp.close()
        self.device.close()
        self.retstr.close()
        return text



            

