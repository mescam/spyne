
#
# rpclib - Copyright (C) Rpclib contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

import logging
logger = logging.getLogger(__name__)

from rpclib.protocol import Base

# this is not exactly rest, because it ignores http verbs.
class HttpRpc(Base):
    def create_document_structure(self, ctx, in_string, in_string_encoding=None):
        print ctx
        print in_string

    def decompose_incoming_envelope(self, ctx, envelope_doc, xmlids=None):
        print ctx

    def deserialize(self, ctx, doc_struct):
        print ctx

    def serialize(self, ctx, out_object):
        print ctx
    
    def create_document_string(self, ctx, out_doc):
        print ctx