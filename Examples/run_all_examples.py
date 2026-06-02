import os
import sys
import traceback

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# converted Markdown that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Set license path (update this path to your license file location)
# os.environ["GROUPDOCS_LIC_PATH"] = "./GroupDocs.Merger.lic"

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Merger for Python via .NET Examples!
=================================================================

This script runs a series of examples showcasing how to merge, split, and reorganize documents with GroupDocs.Merger for Python via .NET.
Each example demonstrates different use cases and functionalities such as:

- Merging and joining documents, page subsets, and images.
- Splitting documents by page list or interval, and splitting text by lines.
- Extracting, removing, swapping, moving, and rotating pages; changing orientation.
- Adding, changing, and removing document passwords.
- Reading document info: format, page count, size, and per-page dimensions.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)

def set_license():
    """Set the GroupDocs license from environment variable or license file."""
    from groupdocs.merger import License

    # First, check for license path in environment variable
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")

    # Set license if found
    if license_path and os.path.exists(license_path):
        license = License()
        license.set_license(license_path)
        print(f"{GREEN}License set from: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")

def run_example(base_dir, example_path):
    """Run a single example by executing its script in-process."""
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)

    # Change to the example directory so relative paths work
    saved_cwd = os.getcwd()
    os.chdir(example_dir)
    try:
        code = open(full_path, "r", encoding="utf-8").read()
        exec(compile(code, full_path, "exec"), {"__name__": "__main__", "__file__": full_path})
    finally:
        os.chdir(saved_cwd)

examples = [
    "getting-started/quick-start-guide/merge_two_documents.py",
    "getting-started/quick-start-guide/extract_pages_from_pdf.py",
    "getting-started/quick-start-guide/split_document_pages.py",
    "developer-guide/get-supported-file-types/list_supported_file_types.py",
    "developer-guide/merge/html/merge_html_documents.py",
    "developer-guide/merge/pdf/merge_pdf_documents.py",
    "developer-guide/merge/pdf/merge_pdf_with_bookmarks.py",
    "developer-guide/get-document-information/read_document_info.py",
    "developer-guide/merge/word/merge_word_documents.py",
    "developer-guide/merge/word/merge_word_documents_continuous.py",
    "developer-guide/merge/powerpoint/merge_powerpoint_documents.py",
    "developer-guide/page-preview/generate_page_previews.py",
    "developer-guide/merge/excel/merge_excel_documents.py",
    "developer-guide/merge/text/merge_text_documents.py",
    "developer-guide/merge/archives/merge_archive_documents.py",
    "developer-guide/merge/epub/merge_epub_documents.py",
    "developer-guide/single-document-operations/move-page/move_document_page.py",
    "developer-guide/single-document-operations/remove-pages/remove_document_pages.py",
    "developer-guide/single-document-operations/split-document/split_document.py",
    "developer-guide/single-document-operations/split-text-file/split_text_file_by_lines.py",
    "developer-guide/single-document-operations/swap-pages/swap_document_pages.py",
    "developer-guide/single-document-operations/extract-pages/extract_pages_by_numbers.py",
    "developer-guide/single-document-operations/change-page-orientation/change_page_orientation.py",
    "developer-guide/single-document-operations/rotate-pages/rotate_document_pages.py",
    "developer-guide/security-operations/add-document-password/add_document_password.py",
    "developer-guide/security-operations/add-password-to-pdf-with-permissions/add_password_to_pdf_with_permissions.py",
    "developer-guide/security-operations/check-document-password-protection/check_document_password_protection.py",
    "developer-guide/security-operations/remove-document-password/remove_document_password.py",
    "developer-guide/security-operations/update-document-password/update_document_password.py",
    "developer-guide/loading-documents/load-from-local-disk/load_from_local_disk.py",
    "developer-guide/loading-documents/load-from-stream/load_from_stream.py",
    "developer-guide/loading-documents/load-password-protected/load_password_protected.py",
]

print_intro()
set_license()

base_dir = os.path.dirname(__file__)
passed = 0
failed = 0

for example in examples:
    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        run_example(base_dir, example)
        print(f"{GREEN}Completed {example}{RESET}\n")
        passed += 1
    except Exception as e:
        print(f"{RED}Error in {example}: {type(e).__name__}: {e}{RESET}\n")
        failed += 1

print(f"\n{GREEN}Passed: {passed}{RESET}  {RED}Failed: {failed}{RESET}  Total: {passed + failed}")

sys.exit(1 if failed else 0)
