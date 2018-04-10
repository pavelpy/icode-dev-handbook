# Python 3
"""
Assuming your filesystem is case sensitive, you use Python 3 and your files in UTF-8

"""


# ==== Imports ===
import re
import glob
import os

# === Constants ===
SUMMARRY_FILENAME = "SUMMARY.md"
IGNORE_FILES = (SUMMARRY_FILENAME, "to-append.md", )  # Case sensitive


# === Functions ==


def get_recursive_file_list(file_ext='.md', basedir='./'):
    for root, dirs, files in os.walk(basedir):
        for file in files:
            if file.endswith(file_ext):
                yield os.path.join(root, file).lstrip(basedir)  # Delete basedir from result filepath(relative path)


def get_book_files_without_ignored(basedir='./', file_ext='.md'):
    """ get book files without ignored files """
    result = []
    for filename in get_recursive_file_list(basedir=basedir, file_ext=".md"):
        if filename not in IGNORE_FILES:
            result.append(filename)
    return result


def get_summary_list_files():
    """ get summary list files"""
    result = []
    with open("SUMMARY.md", 'r') as summary_file:
        summary_text = summary_file.read()#.decode('utf8')
        # Anything that isn't a square closing bracket
        name_regex = "[^]]+"
        # http:// or https:// followed by anything but a closing paren
        url_regex = "[^)]+"

        markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)

        for match in re.findall(markup_regex, summary_text):
            title, filename = match
            result.append(filename)
    return result


def get_file_header(filename):
    with open(filename) as f:
        first_line = f.readline().rstrip().lstrip('#').lstrip()
    return first_line


def main():
    summary_files_checked = []
    summary_list_files = get_summary_list_files()

    # Check files existence
    for fname in summary_list_files:
        if os.path.isfile(fname):
            summary_files_checked.append(fname)
        else:
            print('{} not found'.format(fname))

    result_delta = list(set(get_book_files_without_ignored(basedir='./', file_ext='.md')) - set(summary_files_checked))
    result_delta.sort()
    with open(SUMMARRY_FILENAME,'a') as summary_file:
        for fname in result_delta:
            line_to_add = "* [{1}]({0})".format(fname, get_file_header(fname))
            summary_file.write("\n{}".format(line_to_add))
            print(line_to_add)



if __name__ == "__main__":
    main()
