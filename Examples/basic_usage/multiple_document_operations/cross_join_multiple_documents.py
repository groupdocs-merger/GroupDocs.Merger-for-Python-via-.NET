import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # CrossJoinMultipleDocuments")

    with gm.Merger(constants.sample_pdf) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_docx)
        merger.join(constants.sample_xlsx)
        merger.join(constants.sample_pptx)
        merger.save(constants.output_pdf)
        print(f"Merge to: {constants.output_pdf}")
    
    print(f"----------------------------------------------------------------------------")