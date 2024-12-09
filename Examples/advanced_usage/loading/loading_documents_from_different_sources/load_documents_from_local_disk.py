from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Advanced Usage] # Loading # LoadDocumentFromLocalDisk")

    file_path = constants.sample_docx
    with gm.Merger(file_path) as merger:
        print(f"Document loaded from local disk successfully")
    
    print(f"----------------------------------------------------------------------------")