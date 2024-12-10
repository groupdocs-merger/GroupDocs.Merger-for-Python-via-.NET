from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # RemovePages")

    with gm.Merger(constants.sample_vsdx) as merger:
        print(f"Document info retrieved successfully")
        removeOptions = gm.domain.options.RemoveOptions([3, 5])
        merger.remove_pages(removeOptions)
        merger.save(constants.output_vsdx)
        print(f"Source document pages were removed successfully")
        print(f"Check output: {constants.output_vsdx}")
    
    print(f"----------------------------------------------------------------------------")