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

import click
from rqalpha import cli

__config__ = {
    "url": None,
    "tags": [
        "base__start_date",
        "base__end_date",
        "base__stock_starting_cash",
        "base__future_starting_cash",
        "base__securities",
        "base__run_type",
        "base__frequency",
        "base__benchmark",
    ]
}


def load_mod():
    from .mod import SentryLogMod
    return SentryLogMod()


cli.commands['run'].params.append(
    click.Option(
        ('--sentry', 'mod__sentry__url'),
        default=None,
        type=click.STRING,
        help="[sentry] sentry host url"
    )
)
