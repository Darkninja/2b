from flask import Flask, make_response, request
import os
from convert import convert
app = Flask(__name__)

app.debug = True

mydir = os.path.dirname(__file__)

@app.route('/')
def main():
    return open(mydir+'/content/index.html','r').read()

@app.route('/watch/<vidname>')
def get_vid(vidname):
    vid = open(mydir+'/content/vid/'+vidname,'r').read()
    resp = make_response(vid)
    resp.content_type = "video/ogg"
    return resp
    
@app.route('/download/<vidname>', methods=["POST"])    
def download_vid(vidname):
    c = convert(mydir+'/content/vid/'+vidname, request.form['format'])
    if c.status == 0:
        vid = open(c.path+c.filename,'r').read()
        resp = make_response(vid)
        resp.headers['Content-Disposition'] = 'attachment; filename="' + c.filename + '"'
        resp.headers['Content-Length'] = len(vid)
        resp.content_type = "application/octet-stream"
        return resp
    else:
        return "500: Server Error"

if __name__ == '__main__':
    app.run()