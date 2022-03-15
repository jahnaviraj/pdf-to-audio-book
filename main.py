import argparse
from read_pdf import ReadPdf
from convert_to_audio import AudioBook

def parse_args():
    parser = argparse.ArgumentParser(description="PDF to audio book.")
    parser.add_argument("-p", "--path", help="PDF path.")
    args = parser.parse_args()
    return args


def main():
    pdf_reader = ReadPdf()
    audio_book = AudioBook()
    args = parse_args()
    if args.path:
        text = pdf_reader.convert_pdf_to_txt(args.path)
        audio_book.generate_audio(text)
    else:
        print("Path is required.")

if __name__ == "__main__":
    main()



