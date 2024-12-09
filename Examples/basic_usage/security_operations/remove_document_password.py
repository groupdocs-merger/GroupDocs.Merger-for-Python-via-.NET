import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SecurityOperations # RemoveDocumentPassword")

    load_options = gm.domain.options.LoadOptions("SomePasswordString")
    with gm.Merger(constants.sample_docx_protected, load_options) as merger:
        print(f"Document info retrieved successfully")
        merger.remove_password()
        merger.save(constants.output_docx)
        print(f"Source document password was removed successfully")
        print(f"Check output: {constants.output_docx}")
    
    print(f"----------------------------------------------------------------------------")