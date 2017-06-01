# Design
- Asynchronously calls all api endpoints to get all results. Then merges results into one list.
- Thought about implementing some fancy merge function with a heap to take advantage of presorted data, but the built in sort function is already optimized for this situation (https://stackoverflow.com/questions/38340588/python-heapq-vs-sorted-speed-for-pre-sorted-lists)
- Added unit test for merge function in addition to the integration test already given


# How to use
- To run tests, make sure the pytest, unittest, and mock packages are installed (setup.py was updated)
- `python -m hotel_search.scraperapi` to get scrapers running on port 9000
- `python -m hotel_search.search.search` to get search running on port 8000
- `python -m pytest hotel_search` will run the given scaperapi_test as well as unit tests.
