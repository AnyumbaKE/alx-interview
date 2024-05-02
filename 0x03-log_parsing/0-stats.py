#!/usr/bin/python3
"""A script for parsing HTTP request logs."""
import re

def extract_input(input_line):
    """Extracts sections from a line of an HTTP request log."""
    pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {'status_code': 0, 'file_size': 0}
    log_format = '{}-{}{}{}{}\\s*'.format(*pattern)
    match = re.fullmatch(log_format, input_line)
    if match:
        info['status_code'] = match.group('status_code')
        info['file_size'] = int(match.group('file_size'))
    return info

def print_statistics(total_file_size, status_codes_stats):
    """Prints the accumulated statistics of the HTTP request log."""
    print(f'File size: {total_file_size}', flush=True)
    for status_code, count in sorted(status_codes_stats.items()):
        if count:
            print(f'{status_code}: {count}', flush=True)

def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the metrics from a given HTTP request log line."""
    info = extract_input(line)
    status_code = info.get('status_code', '0')
    status_codes_stats[status_code] = status_codes_stats.get(status_code, 0) + 1
    return total_file_size + info['file_size']

def run():
    """Starts the log parser."""
    total_file_size = 0
    status_codes_stats = {str(code): 0 for code in range(200, 404)}
