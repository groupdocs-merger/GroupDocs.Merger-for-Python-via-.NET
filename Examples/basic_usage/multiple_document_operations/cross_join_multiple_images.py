import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # MultipleDocumentOperations # CrossJoinMultipleImages")

    with gm.Merger(constants.sample_png) as merger:
        print(f"Document info retrieved successfully")
        image_join_options = gm.domain.options.ImageJoinOptions(gm.domain.options.ImageJoinMode.VERTICAL);
        merger.join(constants.sample_bmp, image_join_options)
        merger.join(constants.sample_jpg, image_join_options)
        merger.join(constants.sample_gif, image_join_options)
        merger.save(constants.output_png)
        print(f"Merge to: {constants.output_png}")
    
    print(f"----------------------------------------------------------------------------")