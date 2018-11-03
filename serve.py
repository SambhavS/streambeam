from flask import Flask, send_file, render_template
app = Flask(__name__)
mime_d = {"m3u8" : "vnd.apple.mpegURL", "ts" : "video/MP2T", "mp4": "video/mp4"}

@app.route('/index/')
def main():
    return render_template("index.html")

@app.route('/index/<fname>')
def stuffy(fname):
	return send_file(fname, mimetype=mime_d[fname.split(".")[-1]])


#ffmpeg -i in.mkv -c:v h264 -flags +cgop -g 30 -hls_time 1 output.m3u8 -hls_list_size 0