from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # ChangePageOrientation")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        orientationMode = gm.domain.options.OrientationMode.LANDSCAPE
        orientationOptions = gm.domain.options.OrientationOptions(orientationMode, [3, 4])
        merger.change_orientation(orientationOptions)
        merger.save(constants.output_docx)
        print(f"Source document changed orientation successfully")
        print(f"Check output: {constants.output_docx}")
    
    print(f"----------------------------------------------------------------------------")