from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # MovePage")

    with gm.Merger(constants.sample_xlsx) as merger:
        print(f"Document info retrieved successfully")
        moveOptions = gm.domain.options.MoveOptions(6, 1)
        merger.move_page(moveOptions)
        merger.save(constants.output_xlsx)
        print(f"Source document page was moved successfully")
        print(f"Check output: {constants.output_xlsx}")
    
    print(f"----------------------------------------------------------------------------")