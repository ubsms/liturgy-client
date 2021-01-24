import liturgyclient
import logging
import argparse

parser = argparse.ArgumentParser(description='CasparCG client for Liturgy')
parser.add_argument('host', nargs="?", default="localhost", help='the host to which to connect')
parser.add_argument('--port', '-p', nargs="?", dest='port', default=5250, help='the port on which to connect')
parser.add_argument('-d', dest='debug', action='store_true', help='enable debugging')

args = parser.parse_args()

print(args.port)

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)

liturgyclient.run(ip=args.host)