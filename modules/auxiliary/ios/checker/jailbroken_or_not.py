#!/usr/bin/env python3

#
# MIT License
#
# Copyright (c) 2020 EntySec
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import os
import sys

import socket

from core.badges import badges

class ZetaSploitModule:
    def __init__(self):
        self.badges = badges()

        self.details = {
            'Name': "ios/checker/jailbroken_or_not",
            'Authors': [
                'enty8080'
            ],
            'Description': "Check if remote iPhone jailbroken.",
            'Comments': [
                'Remote iPhone jailbroken if 22 port opened on it.',
                'Cydia.app opens this port by default for SSH connections.'
            ]
        }

        self.options = {
            'RHOST': {
                'Description': "Remote host.",
                'Value': "",
                'Required': True
            }
        }

    def run(self):
        self.badges.output_process("Checking...")
        remote_host = self.options['RHOST']['Value']
        checker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if checker.connect_ex((remote_host, 22)) == 0:
            self.badges.output_success("Target device jailbroken!")
        else:
            self.badges.output_error("Target device is not jailbroken!")
        checker.close()
