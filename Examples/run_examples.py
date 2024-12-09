from quick_start import *
from basic_usage import *
from basic_usage.multiple_document_operations import *
from basic_usage.multiple_document_operations.merge import *
from basic_usage.security_operations import *
from advanced_usage.loading import *
from advanced_usage.loading.loading_documents_from_different_sources import *

#from advanced_usage import *


if __name__ == '__main__':
    ## Quick Start
    set_license_from_file.run()  
    # set_license_from_stream.run()
    # set_metered_license.run()

    ## Basic usage
    get_document_info.run()
    get_supported_file_types.run()
    ## Multiple document operations
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
    merge_docx.run()
    merge_epub.run()
    merge_html.run()
    merge_one.run()
    merge_pdf.run()
    merge_tiff.run()
    merge_pptx.run()
    merge_txt.run()
    merge_vsdx.run()
    merge_xlsx.run()
    merge_zip.run()
    merge_png.run()
    ### Security operations
    add_document_password.run()
    check_document_password_protection.run()
    remove_document_password.run()
    update_document_password.run()
    ## Advanced usage
    ## Loading
    load_password_protected_document.run()
    ### Loading documents from different sources
    load_documents_from_local_disk.run()
    load_documents_from_stream.run()
    load_documents_from_url.run()