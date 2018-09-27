from sys import exit
import urllib.request
import core.messages
import core.api.page
import core.api.count
import core.api.token
import core.api.offset
import core.api.version
from core.response import mk_resp
from core.bandwidth import run_limited



base_url = 'https://api.vk.com/method/wall.get'



def mk_req(token, page, count, offset = 0, v = '5.85'):
    return(
        base_url +
        '?' +
        core.api.page.url(page) +
        '&' +
        core.api.token.url(token) +
        '&' +
        core.api.count.url(count) +
        '&' +
        core.api.offset.url(offset) +
        '&' +
        core.api.version.url(v)
    )



def run_req(url):
    try:
        return(urllib.request.urlopen(url).read().decode('utf-8'))
    except Exception as e:
        print(e)
        exit(core.messages.ERR_NETWORK)
