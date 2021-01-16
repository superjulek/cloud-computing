"""Main program"""

import sys
import argparse
import config

from run import run

TempL=300
TempR=900
size=1
elem_num=200
max_iter=int(5e04)
time_delta=0.1

def main():
    print ("Witaj w świecie klałd kopjutingu")
    parser = argparse.ArgumentParser(description='Get simulation values.')
    parser.add_argument('--temp_left', type=int, dest='temp_left', required=False)
    parser.add_argument('--temp_right', type=int, dest='temp_right', required=False)
    parser.add_argument('--expected_diff', type=int, dest='expected_diff', required=False)
    parser.add_argument('--time_delta', type=int, dest='time_delta', required=False)
    parser.add_argument('--space_delta', type=int, dest='space_delta', required=False)
    parser.add_argument('--run_check', action='store_true', required=False)
    args = parser.parse_args()
    
    if args.temp_left is not None:
        config.initials.temp_left = args.temp_left
    if args.temp_right is not None:
        config.initials.temp_right = args.temp_right
    if args.expected_diff is not None:
        config.simulation.expected_diff = args.expected_diff
    if args.time_delta is not None:
        config.stepping.time_delta = args.time_delta
    if args.space_delta is not None:
        config.stepping.space_delta = args.space_delta
    if args.run_check:
        config.simulation.run_check = True

    run()



if __name__ == "__main__":
    main()
