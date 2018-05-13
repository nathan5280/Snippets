import argparse_, sys, json
from requests import get, put, post

def main(argv):
    '''
    Process the request specified on the command line
    Args:
        argv: Command line arguments.

    Returns: None
    '''
    parser = argparse_.ArgumentParser(description='Business Predictor')

    # IP:port of the business predictor server.
    parser.add_argument('-i', dest='ip', required=True,
                        help='IP:Port of the business predictor server.')
    # Address to add.
    parser.add_argument('-a', '--address', dest='address', default=None,
                        help='Address (double quoted) to add to the repository.')

    # Flag request a list known of addresses.
    parser.add_argument('-l', '--list', dest='list_addresses', action='store_true', default=False,
                        help='Request a list of known all addresses.')

    # Predict on all addresses
    parser.add_argument('-P', '--predict_all', dest='predict_all', action='store_true', default=False,
                        help='Request predictions for all addresses.')

    # Predict one address
    parser.add_argument('-p', '--predict_one', dest='id', default=None,
                        help='Address ID to predict.')

    args = parser.parse_args(argv)
    # Get the parsed command line arguments as a dictionary
    args = vars(args)

    if args['address']:
        response = post("http://{ip}/addresses".format(ip=args['ip']),
             {"address": args['address']}).json()
        print(json.dumps(response, indent=4))

    if args['list_addresses']:
        response = get("http://{ip}/addresses".format(ip=args['ip'])).json()
        print(json.dumps(response, indent=4))

    if args['predict_all']:
        response = get("http://{ip}/predictAll".format(ip=args['ip'])).json()
        print(json.dumps(response, indent=4))

    if args['id']:
        response = get("http://{ip}/predict/{id}".format(ip=args['ip'], id=args['id'])).json()
        print(json.dumps(response, indent=4))


if __name__ == '__main__':
    main(sys.argv[1:])