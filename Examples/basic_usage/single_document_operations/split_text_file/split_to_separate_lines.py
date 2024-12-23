from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # SplitToSeparateLines")

    with gm.Merger(constants.sample_txt) as merger:
        print(f"Document info retrieved successfully")
        filePathOut = "./Output/line_{0}.{1}"
        textSplitOptions = gm.domain.options.TextSplitOptions(filePathOut, [3, 6])
        merger.split(textSplitOptions)
        print(f"Source document was splitted successfully")
        print(f"Check output: {filePathOut}")
    
    print(f"----------------------------------------------------------------------------")