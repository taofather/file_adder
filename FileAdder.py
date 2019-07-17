import argparse
import os.path

parser = argparse.ArgumentParser(description='Parse a file.')
parser.add_argument('path', metavar='path', nargs=1, help='the path of the file')
args = parser.parse_args()
params = {"total": 0, "folder": "resources"}


def file_sum(path):
    file_o = open(params['folder'] + '/' + path, 'r')
    for line in file_o.readlines():
        # sanitize
        text = str.strip(line)

        if text.isdigit():
            params['total'] += int(text)
        elif os.path.isfile(params['folder'] + '/' + text):
            file_sum(text)


file_sum(args.path[0])
print 'Total is ' + str(params['total'])
