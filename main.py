import os
from flask import Flask, Response

server = Flask(__name__)

host = os.environ.get("BACKEND_SERVICE_HOST", "0.0.0.0")
port = int(os.environ.get("BACKEND_SERVICE_PORT", 8080))

pod = os.environ.get("HOSTNAME", "hello-world-backend")

name = os.environ.get("NAME", "STRANGER")


@server.errorhandler(Exception)
def error(e):
    server.logger.error(e)
    return Response(f"Trouble! {e}\n", status=500, mimetype="text/plain")

@server.route("/api/hello")
def hello():
    return Response(f"Hello {name}", mimetype="text/plain")

@server.route("/")
def root():
    return Response("Welcome to the Hello Project", mimetype="text/plain")

if __name__ == "__main__":
    server.run(host=host, port=port)