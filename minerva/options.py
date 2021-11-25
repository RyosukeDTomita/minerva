# coding: utf-8
import argparse


def parse_args() -> dict:
    """parse_args.
    set datetime ex:19901010
    Args:

    Returns:
        dict:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test",
                        help="test", type=str)
    p = parser.parse_args()
    args = {"test": p.test}
    return args
