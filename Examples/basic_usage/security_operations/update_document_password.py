from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SecurityOperations # UpdateDocumentPassword")

    load_options = gm.domain.options.LoadOptions("SomePasswordString")
    with gm.Merger(constants.sample_xlsx_protected, load_options) as merger:
        print(f"Document info retrieved successfully")
        update_password_options = gm.domain.options.UpdatePasswordOptions("OtherPasswordString")
        merger.update_password(update_password_options)
        merger.save(constants.output_xlsx)
        print(f"Source document password was updated successfully")
        print(f"Check output: {constants.output_xlsx}")
    
    print(f"----------------------------------------------------------------------------")