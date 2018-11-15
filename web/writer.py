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
        instr_id = request.form['instr_id']
        traj = request.form['traj']
        split = request.form['split']
        instr = request.form['instr']

        assert traj[:2] == ",(", "the traj is {}".format(traj)
        traj = "["+traj[1:]+"]"

        print("stream, path, traj, split, instr is .. ", stream_id, instr_id, traj, split, instr)

        fname = "hits/{}_{}_{}.hit".format(split, stream_id, instr_id)

        with open(fname, "a") as f:
            f.write("\n\n")
            f.write(traj + "\n")
            f.write(instr + "\n")

        return "Success: Saved the traj!"
    except Exception as e:
        error = "Error: while saving the traj into file: '{}'".format(str(e))
        raise Exception(error)


if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=True)
