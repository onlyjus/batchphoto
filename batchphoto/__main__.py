

# Import from the future for Python 2 and 3 compatability!
from __future__ import print_function, absolute_import, unicode_literals

import sys
import argparse
import os
import glob

import batchphoto

def main():
    # parser
    parser = argparse.ArgumentParser(description='batchphoto')
    ARG = parser.add_argument

    ARG('action', action='store', nargs='?', default=None,
        help='action to perform')
    ARG('-i', '--input', metavar='GLOB', action='store', default=None,
        required=True, help='input glob pattern')
    ARG('-o', '--output', metavar='DIR', action='store', default=None,
        help='directory to save processed images')
    ARG('-r', '--ratios', metavar='R', nargs='*', action='store', default=[],
        help='list of aspect ratios or dimensions')
    ARG('-w', '--overwrite', action='store_true', default=False,
        help='overwrite output files')
    ARG('-v', '--version', action='version', version=batchphoto.__version__)

    args, unknown = parser.parse_known_args()

    # process input
    input_ = args.input
    images = []
    if input_ is not None:
        images = glob.glob(input_)
        if not images:
            print('Could not find any images to process with glob '
                  'pattern: {}'.format(input_))
            sys.exit()
    else:
        print('Please provide a glob pattern to find images.')
        sys.exit()

    # process output
    output = args.output
    if output is not None:
        output = os.path.abspath(output)
        # check to see if the path exists
        if not os.path.exists(output):
            os.mkdir(output)
    else:
        output = './'

    # process ratios
    ratios = args.ratios
    print(ratios)

    kwargs={
        'input': images,
        'output': output,
        'overwrite': args.overwrite,
    }

    if args.action in batchphoto.__all__:
        __import__('.'.join(['batchphoto', args.action, '__main__']))
        getattr(batchphoto, args.action).__main__.main(kwargs)
    else:
        print('Please provide a valid action to perform. Must be one of:\n',
              '\n'.join(batchphoto.__all__))
    sys.exit()

if __name__ == '__main__':
    main()
