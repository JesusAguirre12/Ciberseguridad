import json
from os import environ
from uuid import uuid4
from textwrap import dedent
from http import HTTPStatus
from flask import Flask, request, Response


app = Flask(__name__)


@app.route("/", methods=("GET", "HEAD", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"))
def root():
    method = request.headers.get("X-Method", "GET")
    print(method)
    if method not in ("GET", "HEAD", "OPTIONS"):
        response = Response("Internal server error", mimetype="text/plain", status=HTTPStatus.INTERNAL_SERVER_ERROR)
        response.headers["X-Flag"] = environ["FLAG"]
        return response
    if method == "GET":
        return Response("Unauthorized", mimetype="text/plain", status=HTTPStatus.UNAUTHORIZED)
    response = Response("", status=HTTPStatus.UNAUTHORIZED)
    if method == "OPTIONS":
        response.headers["Allow"] = "HEAD, OPTIONS, GET"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
