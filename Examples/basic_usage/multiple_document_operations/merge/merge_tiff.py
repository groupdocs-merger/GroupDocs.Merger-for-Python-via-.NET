import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Tiff")

    with gm.Merger(constants.sample_tiff) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_tiff)
        merger.save(constants.output_tiff)
        print(f"Merge to: {constants.output_tiff}")
    
    print(f"----------------------------------------------------------------------------")