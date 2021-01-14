import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    return parser


def main(args):
    parser = create_parser()
    args = parser.parse_args(args)


if __name__ == '__main__':
    main(sys.argv[1:])
