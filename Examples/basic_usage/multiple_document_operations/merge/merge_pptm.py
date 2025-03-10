import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Pptm")

    with gm.Merger(constants.sample_pptm) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_pptm)
        merger.save(constants.output_pptm)
        print(f"Merge to: {constants.output_pptm}")
    
    print(f"----------------------------------------------------------------------------")