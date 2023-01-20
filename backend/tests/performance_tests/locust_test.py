# locust_test.py

import logging
import random
import time

from locust import HttpUser, task, between
from locust.exception import RescheduleTask

test_email_host = 'test.local'


def unique_str():
    return '{:.10f}.{}'.format(time.time(), random.randint(1000, 9999))


def unique_email():
    return 'e.' + unique_str() + '@' + test_email_host


def unique_joke_title():
    return 'j.' + unique_str()


def unique_joke_content():
    return 'c.' + unique_str()


def get_cookie(headers):
    for header in headers:
        if header.lower() == 'set-cookie':
            return headers[header]
    return None


class WebsiteTestUser(HttpUser):
    network_timeout = 30.0
    connection_timeout = 30.0

    # wait_time = between(0.5, 3.0)

    def on_start(self):

        base_url = 'http://127.0.0.1:5000/api/v1'

        # set up urls
        register_url = base_url + '/register'
        get_token_url = base_url + '/login'
        # urls used in task
        self.jokes_create_url = base_url + '/jokes'
        self.jokes_get_by_id_url = base_url + '/jokes/'

        # get unique email
        email = unique_email()
        password = 'abcdefghi'

        # register
        response = self.client.post(
            register_url,
            json={'username': email, 'password': password},
        )
        if response.status_code != 201:
            error_msg = 'register: response.status_code = {}, expected 201'.format(response.status_code)
            logging.error(error_msg)

        # get_token
        # - username instead of email
        # - x-www-form-urlencoded (instead of json)
        response = self.client.post(
            get_token_url,
            data={'username': email, 'password': password},
        )
        access_token = response.headers['set-cookie']
        logging.debug('get_token: for email = {}, access_token = {}'.format(email, access_token))

        # set headers with access token
        self.headers = {'Authorization': 'Bearer ' + access_token, 'content-type': 'application/json'}

    def on_stop(self):
        pass

    # enable this dummy task to develop 'on_start'
    # @task
    def dummy(self):
        pass

    @task
    def jokes_write_read_check(self):
        # add joke to api
        joke_title = unique_joke_title()
        joke_content = unique_joke_content()
        logging.debug('jokes_create: joke_name = {}'.format(joke_title))
        with self.client.post(
                self.jokes_create_url,
                json={'title': joke_title, 'content': joke_content},
                headers=self.headers,
                catch_response=True,
        ) as response:

            if response.status_code != 200:
                error_msg = 'jokes_create: response.status_code = {}, expected 201, joke_title = {}'.format(
                    response.status_code, joke_title)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()

            response_dict = response.json()
            if 'id' not in response_dict:
                error_msg = 'jokes_create: data not in response_dict, joke_title = {}'.format(joke_title)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()

            joke_id = response_dict['id']
            logging.debug('jokes_create: for joke_name = {}, joke_id = {}'.format(joke_title, joke_id))

        # get joke from api and check
        with self.client.get(
                self.jokes_get_by_id_url + joke_id,
                headers=self.headers,
                name=self.jokes_get_by_id_url + 'id',
                catch_response=True,
        ) as response:

            if response.status_code != 200:
                error_msg = 'jokes_get_by_id: response.status_code = {}, expected 200, jokes_title = {}'.format(
                    response.status_code, joke_title)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()

            if 'id' not in response_dict:
                error_msg = 'jokes_get_by_id: data not in response_dict, jokes_name = {}'.format(joke_title)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()

            joke_name_returned = response_dict['title']
            logging.debug(
                'jokes_get_by_id: for joke_id = {}, joke_name_returned = {}'.format(joke_id, joke_name_returned))

            if joke_name_returned != joke_title:
                error_msg = 'jokes_get_by_id: joke_name_returned = {} not equal joke_name = {}'.format(
                    joke_name_returned, joke_title)
                logging.error(error_msg)
                response.failure(error_msg)
                raise RescheduleTask()
