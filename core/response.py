import core.messages
import json



def mk_resp(json_str):
    try:
        json_resp = json.loads(json_str)
        cap = -1
        if 'response' in json_resp:
            cap = json_resp['response']['count']
        return((cap, json_resp))
    except Exception as e:
        print(e)
        exit(core.messages.ERR_JSON_PARSE)
