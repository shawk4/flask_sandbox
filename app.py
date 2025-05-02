from flask import Flask, render_template, request, url_for
import subprocess


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Hardcoded states: 'active', 'stopped', or None
    checkbox_states = {
        "Check0": "bg-success",
        "Check1": "bg-danger",
        "Check2": None,
        "Check3": "bg-success"
    }

    timesync = subprocess.check_output(['timedatectl'], text=True)
    textboxes = [
        {'text': f"{timesync}", 'bg_class': 'bg-success'},
        {'text': 'Error in Beta module', 'bg_class': 'bg-danger'},
        {'text': 'Waiting for Gamma input...', 'bg_class': 'bg-warning'},
        {'text': 'Delta is idle', 'bg_class': 'bg-secondary'},
    ]

    return render_template('index.html', checkbox_states=checkbox_states, textboxes=textboxes)

@app.route("/launch_selected", methods=["POST"])
def launch_selected():
    selected = request.form.getlist("selected_checks")
    # app.logger.info(f"Selected checkboxes: {selected}")
    # Do something with the list of selected checkbox IDs
    return "Received: " + ", ".join(selected)

@app.route("/stop_selected", methods=["POST"])
def stop_selected():
    selected = request.form.getlist("selected_checks")
    # app.logger.info(f"Selected checkboxes: {selected}")
    # Do something with the list of selected checkbox IDs
    return "Stopping: " + ", ".join(selected)

if __name__ == '__main__':
    app.run(debug=True)

    