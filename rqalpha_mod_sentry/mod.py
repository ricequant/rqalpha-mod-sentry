# -*- coding: utf-8 -*-
#
# Copyright 2017 Ricequant, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logbook
from raven.base import Client
from raven.handlers.logbook import SentryHandler

from rqalpha.interface import AbstractMod


class ErrorSentryHandler(SentryHandler):
    def emit(self, record):
        if record.level >= logbook.base.WARNING:
            super(ErrorSentryHandler, self).emit(record)


class SentryLogMod(AbstractMod):
    def start_up(self, env, mod_config):
        try:
            tags = dict()
            config = env.config
            for tag in mod_config.tags:
                split_t = tag.split("__")
                split_t.reverse()
                tag_name = None
                tag_value = config
                while True:
                    tag_name = split_t.pop()
                    tag_value = getattr(tag_value, tag_name)
                    if len(split_t) == 0:
                        break
                tags[tag_name] = tag_value
            client = client(mod_config.url, tags=tags)
            handler = ErrorSentryHandler(client, bubble=True)
            env.user_detail_log.handlers.append(handler)
            env.system_log.handlers.append(handler)
        except Exception as e:
            env.system_log.exception(e)

    def tear_down(self, success, exception=None):
        pass
