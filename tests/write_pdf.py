import sys
import pathlib
sys.path.insert(0, f"{pathlib.Path().resolve()}\\")

from utils import PDFScaler


def test_pdf_scaler():
    path_in = "tests/placeholder_pdf.pdf"
    factor = 0.5
    path_out = "tests/test_out.pdf"

    print(f"Scaling pdf: {path_in} by {factor}x")
    scaler = PDFScaler()
    scaler.scale_pdf(path_in, factor)

    scaler.write_pdf(path_out)
    print(f"Written to: {path_out}")


if __name__ == "__main__":
    test_pdf_scaler()
