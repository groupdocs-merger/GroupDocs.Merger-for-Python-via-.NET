import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Vsdx")

    with gm.Merger(constants.sample_vsdx) as merger:
        print(f"Document info retrieved successfully")
        merger.join(constants.sample_vsdx)
        merger.save(constants.output_vsdx)
        print(f"Merge to: {constants.output_vsdx}")
    
    print(f"----------------------------------------------------------------------------")