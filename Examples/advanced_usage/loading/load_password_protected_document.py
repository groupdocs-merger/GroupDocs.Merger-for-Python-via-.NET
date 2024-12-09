from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Advanced Usage] # Loading # LoadPasswordProtectedDocument")

    load_options = gm.domain.options.LoadOptions("SomePasswordString")
    with gm.Merger(constants.sample_docx_protected, load_options) as merger:
        print(f"Document loaded successfully")
    
    print(f"----------------------------------------------------------------------------")