from tornado import gen, ioloop, web, httpclient
import json
import itertools
from config import SCRAPERS, SCRAPER_BASE_URL


class SearchApiHandler(web.RequestHandler):
    @web.asynchronous
    @gen.coroutine
    def get(self):
        http = httpclient.AsyncHTTPClient()
        for scraper in SCRAPERS:
            url = SCRAPER_BASE_URL + scraper
            http.fetch(httpclient.HTTPRequest(url, method='GET'),
                       callback=(yield gen.Callback(scraper)))
        responses = yield gen.WaitAll(SCRAPERS)

        response = self.merge_responses(responses)
        self.set_header('Content-Type', 'application/json')
        self.write(response)
        self.finish()

    @staticmethod
    def merge_responses(responses):
        all_results = [json.loads(x.body)['results'] for x in responses]
        merged_results = sorted(itertools.chain(*all_results),
                                key=lambda x: -x['ecstasy'])
        return {'results': merged_results}


ROUTES = [
    (r"/hotels/search+", SearchApiHandler),
]


def run():
    app = web.Application(
        ROUTES,
        debug=True,
    )

    app.listen(8000)
    print "Server (re)started. Listening on port 8000"

    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
