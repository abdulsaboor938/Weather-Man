# this file will accept multiple arguments in an api call and call specific functions based on given argument

from flask import Flask, request, jsonify
from commands.a_command import handle_a_command
from commands.c_command import handle_c_command
from commands.e_command import handle_e_command

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    # check if the arguments are provided
    if not request.args:
        return {
            "error": "No arguments provided",
            "usage": [
                {"a": "Execute the 'a' command with the given date (YYYY/M)"},
                {"c": "Execute the 'c' command with the given date (YYYY/MM)"},
                {"e": "Execute the 'e' command with the given year (YYYY)"},
            ],
        }

    response = {}
    if "a" in request.args:
        response["a"] = handle_a_command(request.args["a"])
    if "c" in request.args:
        response["c"] = handle_c_command(request.args["c"])
    if "e" in request.args:
        response["e"] = handle_e_command(request.args["e"])
    return jsonify(response)


if __name__ == "__main__":
    app.run()
