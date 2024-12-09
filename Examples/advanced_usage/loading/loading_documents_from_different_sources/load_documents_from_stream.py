from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Advanced Usage] # Loading # LoadDocumentFromStream")

    stream = get_file_stream()
    with gm.Merger(stream) as merger:
        print(f"Document loaded from stream successfully")
    
    print(f"----------------------------------------------------------------------------")

def get_file_stream():
    file_path = constants.sample_docx
    return open(file_path, "rb")