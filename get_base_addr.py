import argparse

from ipyxact.ipyxact import Component

def parse_args():
    parser = argparse.ArgumentParser(
            description='Get the base addresses of the first address block')
    parser.add_argument('ipxact_file', help='IP-XACT file to parse')
    return parser.parse_args();

if __name__ == '__main__':
    args = parse_args()
    with open(args.ipxact_file) as f:
        component = Component()
        component.load(f)
        print '0x{:X}'.format(
                component.memoryMaps.memoryMap[0].addressBlock[0].baseAddress)
