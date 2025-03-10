from quick_start import *
from basic_usage import *
from basic_usage.multiple_document_operations import *
from basic_usage.multiple_document_operations.merge import *
from basic_usage.multiple_document_operations.merge.pdf import *
from basic_usage.multiple_document_operations.merge.word import *
from basic_usage.security_operations import *
from basic_usage.single_document_operations import *
from basic_usage.single_document_operations.extract_pages import *
from basic_usage.single_document_operations.import_document import *
from basic_usage.single_document_operations.split_document import *
from basic_usage.single_document_operations.split_text_file import *
from advanced_usage.loading import *
from advanced_usage.loading.loading_documents_from_different_sources import *

if __name__ == '__main__':
    ## Quick Start
    set_license_from_file.run()  
    # set_license_from_stream.run()
    # set_metered_license.run()

    ## Basic usage
    get_document_info.run()
    get_supported_file_types.run()
    ### Multiple document operations
    cross_join_family_documents.run()
    cross_join_images_to_pdf.run()
    cross_join_multiple_archives.run()
    cross_join_multiple_documents.run()
    cross_join_multiple_images.run()
    cross_join_pages_from_various_documents.run()
    join_multiple_documents.run()
    join_pages_from_various_documents.run()
    join_pages_using_page_builder.run()
    ### Merge
    merge_word_documents_without_section_breaks.run()
    merge_word_documents_without_starting_from_new_page.run()
    merge_word_documents_with_predefined_compliance_mode.run()
    merge_docx.run()
    # merge_epub.run()
    merge_html.run()
    # merge_one.run()
    merge_pdf.run()
    merge_pdf_use_bookmarks.run()
    merge_tiff.run()
    merge_pptx.run()
    merge_pptm.run()
    merge_txt.run()
    merge_vsdx.run()
    # merge_xlsx.run()
    merge_zip.run()
    merge_png.run()
    ### Security operations
    add_document_password.run()
    add_pdf_document_password_with_permissions.run()
    check_document_password_protection.run()
    remove_document_password.run()
    update_document_password.run()
    ### Single document operations
    change_page_orientation.run()
    move_page.run()
    remove_pages.run()
    rotate_pages.run()
    swap_pages.run()
    ### Extract pages
    extract_pages_by_numbers.run()
    extract_pages_by_range.run()
    ### Import document
    import_document_to_diagram.run()
    import_document_to_pdf.run()
    import_document_to_presentation.run()
    import_document_to_spreadsheet.run()
    import_document_to_word_processing.run()
    ### Split document
    split_to_multi_page_documents.run()
    split_to_single_pages.run()
    split_to_single_pages_by_range.run()
    split_to_single_pages_by_range_with_filter.run()
    ### Split text file
    split_to_line_ranges.run()
    split_to_separate_lines.run()
    ## Advanced usage
    ## Loading
    load_password_protected_document.run()
    ### Loading documents from different sources
    load_documents_from_local_disk.run()
    load_documents_from_stream.run()
    load_documents_from_url.run()