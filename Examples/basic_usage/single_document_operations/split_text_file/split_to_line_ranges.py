from turtle import update
import groupdocs.merger as gm
import constants

def run():
    print(f"----------------------------------------------------------------------------")
    print(f"[Example Basic Usage] # SingleDocumentOperations # SplitToLineRanges")

    with gm.Merger(constants.sample_txt) as merger:
        print(f"Document info retrieved successfully")
        filePathOut = "./Output/text_{0}.{1}"
        textSplitMode = gm.domain.options.TextSplitMode.INTERVAL
        textSplitOptions = gm.domain.options.TextSplitOptions(filePathOut, textSplitMode, [3, 6])
        merger.split(textSplitOptions)
        print(f"Source document was splitted successfully")
        print(f"Check output: {filePathOut}")
    
    print(f"----------------------------------------------------------------------------")