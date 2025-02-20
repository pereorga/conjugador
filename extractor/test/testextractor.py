# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from extract import extract_from_dictfile
import unittest
import sys
import hashlib

class TestExtractor(unittest.TestCase):

    def _hash_file(self, filename):
        BUF_SIZE = 65536
        sha1 = hashlib.sha1()

        with open(filename, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)

        return sha1.hexdigest()

    def test_extractor(self):
        executed = 0
        output_dir = "test/output/"
        with open('test/data/signatures.txt') as f:
            lines = f.readlines()

        for line in lines:
            line = line.rstrip('\n')
            filename, output_file, signature = line.split(',')
            filename = "test/data/" + filename

            extract_from_dictfile(filename, 'test/data/definitions.json', output_dir)
            signature_file = self._hash_file(output_dir + output_file)
            self.assertEquals(signature, signature_file)
            executed = executed + 1

        self.assertEquals(2, executed)


if __name__ == '__main__':
    unittest.main()
