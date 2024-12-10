from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # SwapPages")

    with gm.Merger(constants.sample_pptx) as merger:
        print(f"Document info retrieved successfully")
        swapOptions = gm.domain.options.SwapOptions(3, 6)
        merger.swap_pages(swapOptions)
        merger.save(constants.output_pptx)
        print(f"Source document pages were swapped successfully")
        print(f"Check output: {constants.output_pptx}")
    
    print(f"----------------------------------------------------------------------------")