#!/usr/bin/env python3
"""An Python command line tool that reads and splits tagging data."""

from itertools import islice
import argparse
import random


def main(args: argparse.Namespace) -> None:

    with open(args.input, 'r') as text:
        lines = text.readlines()
    random.seed(args.seed)
    random.shuffle(lines)
    train_size = round(len(lines) * 0.8)
    dev_size = round(len(lines) * 0.1)
    test_size = round(len(lines) - train_size - dev_size)
    write_tags(lines, args.train, 0, train_size)
    write_tags(lines, args.dev, train_size, dev_size)
    write_tags(lines, args.test, train_size + dev_size, test_size)

def write_tags(text, path, start, size):
    with open(path, 'a') as outfile:
        for line in text[start:start + size]:
            outfile.write(line)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("input")
    parser.add_argument("train")
    parser.add_argument("dev")
    parser.add_argument("test")
    main(parser.parse_args())
