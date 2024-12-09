import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Epub")

    with gm.Merger(constants.sample_epub) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_epub)
        merger.save(constants.output_epub)
        print(f"Merge to: {constants.output_epub}")
    
    print(f"----------------------------------------------------------------------------")