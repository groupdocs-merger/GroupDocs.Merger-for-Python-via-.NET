import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # CrossJoinFamilyDocuments")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_doc)
        merger.join(constants.sample_docm)
        merger.save(constants.output_docx)
        print(f"Merge to: {constants.output_docx}")
    
    print(f"----------------------------------------------------------------------------")