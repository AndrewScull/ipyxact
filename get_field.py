import argparse

from ipyxact.ipyxact import Component

parser = argparse.ArgumentParser(
        description='Get the base addresses of the first value of the '
                    'specified field.')
parser.add_argument('ipxact_file', help='IP-XACT file to parse')
parser.add_argument('field', choices=['base','range'])
args = parser.parse_args();

with open(args.ipxact_file) as f:
    component = Component()
    component.load(f)
    ab = component.memoryMaps.memoryMap[0].addressBlock[0]
    print '0x{:X}'.format(ab.baseAddress if args.field == 'base' else ab.range)
