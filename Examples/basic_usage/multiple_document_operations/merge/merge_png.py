import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # Merge : Png")

    with gm.Merger(constants.sample_png) as merger:
        print(f"Document info retrieved successfully")
        image_join_mode = gm.domain.options.ImageJoinMode.HORIZONTAL
        image_join_options = gm.domain.options.ImageJoinOptions(image_join_mode)
        merger.join(constants.sample_png, join_options = image_join_options)
        merger.save(constants.output_png)
        print(f"Merge to: {constants.output_png}")
    
    print(f"----------------------------------------------------------------------------")