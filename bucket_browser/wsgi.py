from flask import Flask, request, render_template, Response
from requests import Session
from xmltodict import parse
from json import dumps, loads

app = Flask(__name__, static_url_path='/static')

BUCKET = "public-j5-org"
SIZES = ["Bytes", "KB", "MB", "GB", "TB", "PB"]

@app.route("/")
@app.route("/<path:path>", methods=["GET"], defaults={"path": ""})
def root(path=None):

    path = request.path

    session = Session()

    try:
        Url = f"https://{BUCKET}.storage.googleapis.com"
        response = session.get(Url)
        decoded_response = response.content.decode("utf-8")
        response_json = loads(dumps(parse(decoded_response)))
        print(Url, response_json.get('ListBucketResult').get('Contents'))
        contents = response_json.get('ListBucketResult').get('Contents')
    except Exception as e:
        return Response(e, 500, content_type="text/plain")

    try:
        files = []
        for obj in contents:
            key = obj.get('Key') if path else f"{path}{obj.get('Key')}"
            name = key if key.endswith("/") else key.split('/')[-1]
            if size := None if key.endswith("/") else int(obj.get('Size')):
                for i, v in enumerate(SIZES):
                    if size < 1000 ** i+1:
                        size = f"{size} {v}"
                        break
                    else:
                        size = round(size / 1000, 3)
                        continue
            _ = {
                'key': f"{Url}{key}" if size else key,
                'name': name,
                'size': size,
                'last_modified': obj.get('LastModified'),
            }
            if path:
                if path in key:
                    files.append(_)
            if not '/' in key or not size:
                if path:
                    if path in key:
                        files.append(_)
                else:
                    files.append(_)
        return render_template('bucket_browser.html', files=files)
    except Exception as e:
        return Response(e, 500, content_type="text/plain")


if __name__ == '__main__':
    app.run()
