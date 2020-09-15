import argparse

parser = argparse.ArgumentParser(description='Add two numbers')
parser.add_argument('--a', type = int ,metavar = '',required=True, help = 'First Number')
parser.add_argument('--b', type = int ,metavar = '',required=True, help = 'Second Number')
args = parser.parse_args()

def myAdd(a,b):
    return a+b

if __name__ == "__main__":
    print(myAdd(args.a,args.b))    