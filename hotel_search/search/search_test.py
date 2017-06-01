from search import SearchApiHandler
import json
from mock import Mock
import unittest


class SearchApiHandlerTest(unittest.TestCase):
    def test_merge_responses(self):
        resp_one = {'results': [{'ecstasy': 6}, {'ecstasy': 4}, {'ecstasy': 2}]}
        resp_two = {'results': [{'ecstasy': 5}, {'ecstasy': 3}, {'ecstasy': 1}]}

        http_resp_one = Mock()
        http_resp_one.body = json.dumps(resp_one)
        http_resp_two = Mock()
        http_resp_two.body = json.dumps(resp_two)

        result = SearchApiHandler.merge_responses([http_resp_one, http_resp_two])
        expected = {'results': [{'ecstasy': 6}, {'ecstasy': 5}, {'ecstasy': 4},
                                {'ecstasy': 3}, {'ecstasy': 2}, {'ecstasy': 1}]}

        assert result == expected, 'Results not merged properly'
