import json


def load_bare():
    try:
        return json.load(open("data.json"))
    except:
        pass


def load_bare_log():
    try:
        return json.load(open("data.json"))
    except:
        print("failed to load")


def load_broad():
    try:
        return json.load(open("data.json"))
    except Exception:
        pass


def load_broad_named_log():
    try:
        return json.load(open("data.json"))
    except BaseException as e:
        log(e)
