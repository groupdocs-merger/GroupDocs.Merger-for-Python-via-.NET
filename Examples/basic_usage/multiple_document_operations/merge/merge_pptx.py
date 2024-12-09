import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Pptx")

    with gm.Merger(constants.sample_pptx) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_pptx)
        merger.save(constants.output_pptx)
        print(f"Merge to: {constants.output_pptx}")
    
    print(f"----------------------------------------------------------------------------")