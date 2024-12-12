from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # SplitToSinglePagesByRange")

    with gm.Merger(constants.sample_docx) as merger:
        print(f"Document info retrieved successfully")
        filePathOut = "./Examples/Output/document_{0}.{1}"
        splitOptions = gm.domain.options.SplitOptions(filePathOut, 3, 6)
        merger.split(splitOptions)
        print(f"Source document was splitted successfully")
        print(f"Check output: {filePathOut}")
    
    print(f"----------------------------------------------------------------------------")