from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # SplitToMultiPageDocuments")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        filePathOut = "./Output/document_{0}.{1}"
        splitMode = gm.domain.options.SplitMode.INTERVAL
        splitOptions = gm.domain.options.SplitOptions(filePathOut, [3, 6], splitMode)
        merger.split(splitOptions)
        print(f"Source document was splitted successfully")
        print(f"Check output: {filePathOut}")
    
    print(f"----------------------------------------------------------------------------")