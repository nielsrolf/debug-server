import argparse
from flask import Flask, request, Response
import pprint as pp


app = Flask(__name__)


def request_params():
    if request.method == 'GET':
        return request.args.to_dict()
    else:
        return request.get_json(force=True)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def log_request(path="/"):
    print("----- NEW REQUEST ------")
    print(request.method, path)
    print(">> HEADERS: ")
    pp.pprint(request.headers)
    print(">> BODY: ")
    pp.pprint(request_params())
    return Response(status=204)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", help="which port to check", type=int)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)


if __name__ == '__main__':
    main()
    
