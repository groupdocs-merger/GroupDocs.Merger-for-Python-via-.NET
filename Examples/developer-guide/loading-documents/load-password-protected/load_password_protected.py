from groupdocs.merger import Merger
from groupdocs.merger.domain.options import LoadOptions
from groupdocs.merger.exceptions import IncorrectPasswordException, PasswordRequiredException

def load_password_protected():
    # Provide the document's open password via LoadOptions
    load_options = LoadOptions(password="secret")
    try:
        # Load the password-protected document
        with Merger("./protected.pdf", load_options) as merger:
            # The document is now open — perform any supported operation
            info = merger.get_document_info()
            print("Format:", info.type.file_format)
            print("Pages:", info.page_count)
    except PasswordRequiredException:
        print("Error: the document requires a password but none was provided.")
    except IncorrectPasswordException:
        print("Error: the supplied password is incorrect.")

if __name__ == "__main__":
    load_password_protected()