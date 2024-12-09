import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Zip")

    with gm.Merger(constants.sample_zip) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_zip)
        merger.save(constants.output_zip)
        print(f"Merge to: {constants.output_zip}")
    
    print(f"----------------------------------------------------------------------------")