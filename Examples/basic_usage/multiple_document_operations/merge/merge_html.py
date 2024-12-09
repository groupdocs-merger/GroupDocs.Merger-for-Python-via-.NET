import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Html")

    with gm.Merger(constants.sample_html) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_html)
        merger.save(constants.output_html)
        print(f"Merge to: {constants.output_html}")
    
    print(f"----------------------------------------------------------------------------")