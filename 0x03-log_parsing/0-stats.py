#!/usr/bin/python3
'''Log Parsing
'''
import sys
import signal


def calculate_statistics(total_size, status_codes):
    '''calculate_statistics
    '''
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes):
        print("{}: {}".format(status_code, status_codes[status_code]))


def main():
    '''main function
    '''
    line_count = 0
    total_size = 0
    status_codes = {}

    def signal_handler(sig, frame):
        '''signal_handler
        '''
        calculate_statistics(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = int(parts[-2])

            total_size += size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if line_count % 10 == 0:
                calculate_statistics(total_size, status_codes)

        except (ValueError, IndexError):
            # Skip lines with invalid format
            pass


if __name__ == "__main__":
    main()
