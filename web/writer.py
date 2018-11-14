from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/traj_dump/', methods=["GET", "POST"])
@cross_origin()
def login_page():

    try:
        # raise Exception("arrey bhai wait")
        stream_id = request.form['stream_id']
        path_id = request.form['path_id']
        traj = request.form['traj']

        assert traj[:2] == ",("
        traj = "["+traj[1:]+"]"

        print("stream, path, traj is .. ", stream_id, path_id, traj)
        return "Success: Saved the traj!"
    except Exception as e:
        error = "Error: while saving the traj into file: '{}'".format(str(e))
        raise
        return error


if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=True)
