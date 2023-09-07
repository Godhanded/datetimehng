from flask import Flask, jsonify, request
from datetime import datetime


app = Flask(__name__)
app.json.sort_keys = False # stop default sorting of json responses



@app.route("/api", methods=["GET"])
def get_details():
    data = request.args  # get query params
    # collect required params(slack_name,track) if exist else none
    slack_name, track = data.get("slack_name", None), data.get("track", None)
    if not slack_name or not track:  # error if required params missing
        return (
            jsonify(
                {
                    "status_code": str(400),
                    "error": "Bad Request",
                    "message": "request args slack_name or track missing",
                }
            ),
            400,
        )
    return (
        # serialize as json and prepare response body
        jsonify(
            {
                "slack_name": slack_name,
                "current_day": datetime.utcnow().strftime("%A"),# give full weekday name from utc date
                "utc_time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "track": track,
                "github_file_url": "https://github.com/Godhanded/datetimehng/blob/main/app.py",
                "github_repo_url": "https://github.com/Godhanded/datetimehng",
                "status_code": str(200),
            }
        ),
        200,
    )
