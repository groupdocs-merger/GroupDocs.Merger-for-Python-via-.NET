from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # RotatePages")

    with gm.Merger(constants.sample_pdf) as merger:
        print(f"Document info retrieved successfully")
        rotateMode = gm.domain.options.RotateMode.ROTATE180
        rotateOptions = gm.domain.options.RotateOptions(rotateMode, [1, 2])
        merger.rotate_pages(rotateOptions)
        merger.save(constants.output_pdf)
        print(f"Source document pages were rotated successfully")
        print(f"Check output: {constants.output_pdf}")
    
    print(f"----------------------------------------------------------------------------")