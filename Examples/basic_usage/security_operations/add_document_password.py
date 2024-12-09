import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SecurityOperations # AddDocumentPassword")

    with gm.Merger(constants.sample_pptx) as merger:
        print(f"Document info retrieved successfully")
        add_password_options = gm.domain.options.AddPasswordOptions("SomePasswordString")
        merger.add_password(add_password_options)
        merger.save(constants.output_pptx)
        print(f"Source document password was added successfully")
        print(f"Check output: {constants.output_pptx}")
    
    print(f"----------------------------------------------------------------------------")