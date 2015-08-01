from http import app


@app.route('/_ping', methods=['OPTIONS'])
def _heath_check():
    return "OK"
