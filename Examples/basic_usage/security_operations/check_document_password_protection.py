import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SecurityOperations # CheckDocumentPasswordProtection")

    with gm.Merger(constants.sample_xlsx_protected) as merger:
        print(f"Document info retrieved successfully")
        is_password_set = merger.is_password_set()
        print(f"Source document password has password: {is_password_set}.")
    
    print(f"----------------------------------------------------------------------------")