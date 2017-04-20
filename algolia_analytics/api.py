import requests
import json
from datetime import datetime, timedelta
from util import exception_handler

class AlgoliaAnalytics(object):

    endpoint = 'https://analytics.algolia.com/1'

    def __init__(self, api_key, application_id):
        """ Initialize the instance and create the API headers """
        self.headers = { 'X-Algolia-API-Key': api_key,
                         'X-Algolia-Application-Id': application_id }

    def popular_searches(self, indices, **kwargs):
        end_point_type = 'searches'
        metric = 'popular'
        url = self._construct_url(end_point_type, indices, metric)
        result = self._call_algolia(url, params = kwargs)

        return result

    def no_results(self, indices, **kwargs):
        end_point_type = 'searches'
        metric = 'noresults'
        url = self._construct_url(end_point_type, indices, metric)
        result = self._call_algolia(url, params = kwargs)

        return result

    def countries(self, indices, **kwargs):
        end_point_type = 'searches'
        metric = 'countries'
        url = self._construct_url(end_point_type, indices, metric)
        result = self._call_algolia(url, params = kwargs)

        return result

    def hits(self, indices, **kwargs):
        end_point_type = 'searches'
        metric = 'hits'
        url = self._construct_url(end_point_type, indices, metric)
        result = self._call_algolia(url, params = kwargs)

        return result

    def hitswithtypo(self, indices, **kwargs):
        end_point_type = 'searches'
        metric = 'hitswithtypo'
        url = self._construct_url(end_point_type, indices, metric)
        result = self._call_algolia(url, params = kwargs)

        return result

    def top_ips(self, indices, **kwargs):
        end_point_type = 'searches'
        metric = 'ips'
        url = self._construct_url(end_point_type, indices, metric)
        result = self._call_algolia(url, params = kwargs)

        return result

    def top_ips_ratelimits(self, indices, **kwargs):
        end_point_type = 'ratelimits'
        metric = 'ips'
        url = self._construct_url(end_point_type, indices, metric)
        result = self._call_algolia(url, params = kwargs)

        return result

    def _construct_url(self, end_point_type, indices, metric):
        """ Utility function for creating the api url """
        if type(indices) is str:
            url = [self.endpoint, end_point_type, indices, metric]
        else:
            url = [self.endpoint, end_point_type, ",".join(indices), metric]

        return '/'.join(url)

    def _call_algolia(self, url, **kwargs):
        """ Utility method for creating HTTP request to Algolia """
        result = requests.get(url, headers=self.headers, **kwargs)

        if result.status_code >= 300:
            exception_handler(result)

        return result

