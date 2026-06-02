from groupdocs.merger import Merger
from groupdocs.merger.domain.options import TextSplitOptions, TextSplitMode

def split_text_file_by_lines():
    # Load the source text file
    with Merger("./input.txt") as merger:
        # Split at lines 2 and 4 — each listed line becomes a separate output file
        # Output files: lines_0.txt (line 2), lines_1.txt (line 4)
        # IMPORTANT: use keyword arguments — positional arguments will fail
        merger.split(TextSplitOptions(
            file_path_format="./lines_{0}.txt",
            line_numbers=[2, 4],
            mode=TextSplitMode.LINES,
        ))

def split_text_file_by_interval():
    # Load the source text file
    with Merger("./input.txt") as merger:
        # Split at line boundaries [2, 4] using INTERVAL mode
        # lines_0.txt → line 1, lines_1.txt → lines 2-3, lines_2.txt → lines 4+
        merger.split(TextSplitOptions(
            file_path_format="./lines_{0}.txt",
            line_numbers=[2, 4],
            mode=TextSplitMode.INTERVAL,
        ))

if __name__ == "__main__":
    split_text_file_by_lines()
    split_text_file_by_interval()