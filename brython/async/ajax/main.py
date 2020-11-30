from browser import ajax, document


def show_text(req):
    if req.status == 200:
        log(f"Text received: '{req.text}'")
    else:
        log(f"Error: {req.status} - {req.text}")


def log(message):
    document["log"].value += f"{message} \n"


def ajax_get(evt):
    log("Before async get")
    ajax.get("/api.txt", oncomplete=show_text)
    log("After async get")


def ajax_get_blocking(evt):
    log("Before blocking get")
    try:
        ajax.get("/api.txt", blocking=True, oncomplete=show_text)
    except Exception as exc:
        log(f"Error: {exc.__name__}")
        log("Did you start a web server (ex: 'python3 -m http.server')?")
    else:
        log("After blocking get")


document["get-btn"].bind("click", ajax_get)
document["get-blocking-btn"].bind("click", ajax_get_blocking)
