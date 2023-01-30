from flask import Flask
import subprocess
import string
import getpass

#flask
app = Flask(__name__)
@app.route("/")
def index():
    #return "THINKSOFT111"
    cmd = subprocess.Popen("system_profiler SPHardwareDataType SPStorageDataType SPDisplaysDataType", stdout=subprocess.PIPE, universal_newlines=True, shell=True)
    cmd_out, cmd_err = cmd.communicate()
    #filter out attributes
    for myLine in cmd_out.split('\n'):
        if "Capacity" in myLine:
            cap =  myLine.strip()
        if "Memory" in myLine:
            mem =  myLine.strip()
        if "Chip" in myLine:
            chip =  myLine.strip()
        if "Serial" in myLine:
            serial =  myLine.strip()
        if "Model Identifier" in myLine:
            model_id =  myLine.strip()
        if "Resolution" in myLine:
            resolution = myLine.strip()
    return cap + '</br>' + mem + '</br>' + chip + '</br>' + serial + '</br>' + model_id + '</br>' + resolution

#send data from client to server########




exit
