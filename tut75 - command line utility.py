import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    elif args.o == 'rdiv':
        return args.x // args.y
    elif args.o == 'rem':
        return args.x % args.y
    elif args.o == 'pow':
        return args.x ** args.y
    else:
        return 'Please use a valid operator'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--x', type=float, default=1.0, help='Please contact the owner')
    parser.add_argument('--y', type=float, default=1.0, help='Please contact the owner')
    parser.add_argument('--o', type=str, default='add', help='Please contact the owner')

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))