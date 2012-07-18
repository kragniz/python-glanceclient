# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class Controller(object):
    def __init__(self, http_client, model):
        self.http_client = http_client
        self.model = model

    def list(self):
        """Retrieve a listing of Image objects

        :returns generator over list of Images
        """
        resp, body = self.http_client.json_request('GET', '/v2/images')
        for image in body['images']:
            #NOTE(bcwaldon): remove 'self' for now until we have an elegant
            # way to pass it into the model constructor without conflict
            image.pop('self', None)
            yield self.model(**image)

    def get(self, image_id):
        url = '/v2/images/%s' % image_id
        resp, body = self.http_client.json_request('GET', url)
        #NOTE(bcwaldon): remove 'self' for now until we have an elegant
        # way to pass it into the model constructor without conflict
        body['image'].pop('self', None)
        return self.model(**body['image'])
