
from core.request import mk_req, run_req
from core.response import mk_resp
from core.bandwidth import run_limited
from core.poroshok import Poroshok
from core.parse import parse



class Fetcher:

    reqs = None
    freq = None

    def __init__(self, token, page, count, offset = 0, freq = 3):

        self.reqs = []
        self.freq = freq
        for i in range(offset, offset + count, 100):
            self.reqs.append(mk_req(token, page, min([count, 100]), i))
            count -= 100

    def __execute__(self, request):
        poroshki = []
        (cap, json) = mk_resp(
            run_req(
                request
            )
        )

        if cap != -1:
            for post in json['response']['items']:
                prs = parse(post['text'])
                for p in prs:
                    poroshki.append(
                        Poroshok(p, post['date'], post['from_id'], post['id'])
                    )
        return(poroshki)

    def run(self):
        poroshki = []
        for request in self.reqs:
            poroshki.append(
                run_limited(
                    lambda: self.__execute__(request),
                    self.freq
                )
            )
        return(
            sum(
                poroshki,
                []
            )
        )



class CFetcher:

    page = None
    token = None
    freq = None

    def __init__(self, token, page, freq = 3):
        self.token = token
        self.page = page
        self.freq = freq

    def run(self):

        request = mk_req(self.token, self.page, 1)

        (cap, _) = run_limited(
            lambda: mk_resp(
                run_req(
                    request
                )
            ),
            self.freq
        )

        return(Fetcher(self.token, self.page, cap).run())
