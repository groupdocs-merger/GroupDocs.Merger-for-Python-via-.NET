import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Xlsx")

    with gm.Merger(constants.sample_xlsx) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_xlsx)
        merger.save(constants.output_xlsx)
        print(f"Merge to: {constants.output_xlsx}")
    
    print(f"----------------------------------------------------------------------------")