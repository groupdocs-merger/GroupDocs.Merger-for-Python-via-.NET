from groupdocs.merger import Merger
from groupdocs.merger.domain.options import LoadOptions

def check_document_password_protection():
    # Provide the current password so the protected document can be opened
    load_options = LoadOptions(password="p@ss")
    # Load the password-protected document
    with Merger("./protected.pdf", load_options) as merger:
        # Returns True if the document has an open password set
        protected = merger.is_password_set()
        print("Is password set:", protected)

if __name__ == "__main__":
    check_document_password_protection()