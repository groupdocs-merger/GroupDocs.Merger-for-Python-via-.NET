import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Txt")

    with gm.Merger(constants.sample_txt) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_txt)
        merger.save(constants.output_txt)
        print(f"Merge to: {constants.output_txt}")
    
    print(f"----------------------------------------------------------------------------")