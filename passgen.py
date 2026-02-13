#!/usr/bin/env python3
"""Simple password generator CLI tool."""

import random
import string
import argparse
import sys


def generate_password(length: int, use_special: bool = True) -> str:
    """Generate a random password."""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(
        description="Generate random passwords",
        prog="passgen"
    )
    parser.add_argument(
        "-l", "--length", 
        type=int, 
        default=16, 
        help="Password length (default: 16)"
    )
    parser.add_argument(
        "-n", "--no-special", 
        action="store_true", 
        help="Exclude special characters"
    )
    parser.add_argument(
        "-c", "--count", 
        type=int, 
        default=1, 
        help="Number of passwords to generate (default: 1)"
    )
    parser.add_argument(
        "-s", "--seed", 
        type=int, 
        help="Random seed for reproducibility"
    )
    
    args = parser.parse_args()
    
    if args.seed is not None:
        random.seed(args.seed)
    
    for i in range(args.count):
        pwd = generate_password(args.length, not args.no_special)
        print(pwd)


if __name__ == "__main__":
    main()
