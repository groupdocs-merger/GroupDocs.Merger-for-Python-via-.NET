import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Docx")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_docx)
        merger.save(constants.output_docx)
        print(f"Merge to: {constants.output_docx}")
    
    print(f"----------------------------------------------------------------------------")