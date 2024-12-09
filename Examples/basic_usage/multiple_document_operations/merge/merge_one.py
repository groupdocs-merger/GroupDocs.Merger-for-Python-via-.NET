import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : One")

    with gm.Merger(constants.sample_one) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_one)
        merger.save(constants.output_one)
        print(f"Merge to: {constants.output_one}")
    
    print(f"----------------------------------------------------------------------------")