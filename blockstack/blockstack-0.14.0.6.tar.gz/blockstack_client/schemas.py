#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
    Blockstack-client
    ~~~~~
    copyright: (c) 2014-2015 by Halfmoon Labs, Inc.
    copyright: (c) 2016 by Blockstack.org

    This file is part of Blockstack-client.

    Blockstack-client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Blockstack-client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with Blockstack-client. If not, see <http://www.gnu.org/licenses/>.
"""

import jsonschema
from .constants import *

OP_CONSENSUS_HASH_PATTERN = r'^([0-9a-fA-F]{{{}}})$'.format(LENGTH_CONSENSUS_HASH * 2)
OP_BASE58CHECK_PATTERN = r'^([123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+)$'
OP_ADDRESS_PATTERN = OP_BASE58CHECK_PATTERN
OP_PRIVKEY_PATTERN = OP_BASE58CHECK_PATTERN
OP_P2PKH_PATTERN = r'^76[aA]914[0-9a-fA-F]{40}88[aA][cC]$'
OP_SCRIPT_PATTERN = r'^[0-9a-fA-F]+$'
OP_CODE_PATTERN = r'^([{}]{{1}}|{}{}|{}{}|{}{})$'.format(
    ''.join(NAME_OPCODES.values()),
    NAME_TRANSFER, TRANSFER_KEEP_DATA,
    NAME_TRANSFER, TRANSFER_REMOVE_DATA,
    NAME_REGISTRATION, NAME_REGISTRATION
)
OP_CODE_NAME_PATTERN = '|'.join(NAME_OPCODES.keys())
OP_HEX_PATTERN = r'^([0-9a-fA-F]+)$'
OP_UUID_PATTERN = r'^([0-9a-fA-F\-]+)$'
OP_PUBKEY_PATTERN = OP_HEX_PATTERN
OP_SCRIPT_PATTERN = OP_HEX_PATTERN
OP_TXID_PATTERN = OP_HEX_PATTERN
OP_ZONEFILE_HASH_PATTERN = r'^([0-9a-fA-F]{{{}}})$'.format(LENGTH_VALUE_HASH * 2)
OP_NAME_PATTERN = r'^([a-z0-9\-_.+]{{{},{}}})$'.format(3, LENGTH_MAX_NAME)
OP_NAMESPACE_PATTERN = r'^([a-z0-9\-_+]{{{},{}}})$'.format(1, LENGTH_MAX_NAMESPACE_ID)
OP_NAMESPACE_HASH_PATTERN = r'^([0-9a-fA-F]{16})$'
OP_BASE64_PATTERN_SECTION = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})'
OP_BASE64_PATTERN = r'^({})$'.format(OP_BASE64_PATTERN_SECTION)
OP_URLENCODED_PATTERN = r'^([a-zA-Z0-9\-_.~%]+)$'
OP_URI_TARGET_PATTERN = r'^([a-z0-9+]+)://([a-zA-Z0-9\-_.~%#?&\:/]+)$'
OP_MUTABLE_DATA_MD_PATTERN = r'^(mutable:{}:[0-9]+)$'.format(OP_BASE64_PATTERN_SECTION)

PRIVKEY_SINGLESIG_SCHEMA_WIF = {
    'type': 'string',
    'pattern': OP_PRIVKEY_PATTERN
}

PRIVKEY_SINGLESIG_SCHEMA_HEX = {
    'type': 'string',
    'pattern': OP_HEX_PATTERN
}

PRIVKEY_SINGLESIG_SCHEMA = {
    'anyOf': [
        PRIVKEY_SINGLESIG_SCHEMA_WIF,
        PRIVKEY_SINGLESIG_SCHEMA_HEX
    ],
}

PRIVKEY_MULTISIG_SCHEMA = {
    'type': 'object',
    'properties': {
        'address': {
            'type': 'string',
            'pattern': OP_ADDRESS_PATTERN,
        },
        'redeem_script': {
            'type': 'string',
            'pattern': OP_SCRIPT_PATTERN,
        },
        'private_keys': {
            'type': 'array',
            'items': PRIVKEY_SINGLESIG_SCHEMA
        },
    },
    'required': [
        'address',
        'redeem_script',
        'private_keys'
    ],
}

PRIVKEY_INFO_SCHEMA = {
    'anyOf': [
        PRIVKEY_SINGLESIG_SCHEMA,
        PRIVKEY_MULTISIG_SCHEMA
    ],
}

ENCRYPTED_PRIVKEY_SINGLESIG_SCHEMA = {
    'type': 'string',
    'pattern': OP_BASE64_PATTERN
}

ENCRYPTED_PRIVKEY_MULTISIG_SCHEMA = {
    'type': 'object',
    'properties': {
        'address': {
            'type': 'string',
            'pattern': OP_ADDRESS_PATTERN,
        },
        'encrypted_redeem_script': {
            'type': 'string',
            'pattern': OP_BASE64_PATTERN,
        },
        'encrypted_private_keys': {
            'type': 'array',
            'items': {
                'type': 'string',
                'pattern': OP_BASE64_PATTERN
            },
        },
    },
    'required': [
        'address',
        'encrypted_redeem_script',
        'encrypted_private_keys',
    ],
}

ENCRYPTED_PRIVKEY_INFO_SCHEMA = {
    'anyOf': [
        ENCRYPTED_PRIVKEY_SINGLESIG_SCHEMA,
        ENCRYPTED_PRIVKEY_MULTISIG_SCHEMA
    ],
}

ENCRYPTED_WALLET_SCHEMA_PROPERTIES = {
    'data_pubkey': {
        'type': 'string',
        'pattern': OP_PUBKEY_PATTERN
    },
    'data_pubkeys': {
        'type': 'array',
        'items': {
            'type': 'string',
            'pattern': OP_PUBKEY_PATTERN,
            'minItems': 1,
            'maxItems': 1
        },
    },
    'encrypted_data_privkey': {
        'type': 'string',
        'pattern': OP_BASE64_PATTERN,
    },
    'encrypted_master_private_key': {
        'type': 'string',
        'pattern': OP_BASE64_PATTERN,
    },
    'encrypted_owner_privkey': ENCRYPTED_PRIVKEY_INFO_SCHEMA,
    'encrypted_payment_privkey': ENCRYPTED_PRIVKEY_INFO_SCHEMA,
    'owner_addresses': {
        'type': 'array',
        'items': {
            'type': 'string',
            'pattern': OP_ADDRESS_PATTERN,
            'minItems': 1,
            'maxItems': 1
        },
    },
    'payment_addresses': {
        'type': 'array',
        'items': {
            'type': 'string',
            'pattern': OP_ADDRESS_PATTERN,
            'minItems': 1,
            'maxItems': 1
        },
    },
}

ENCRYPTED_WALLET_SCHEMA_CURRENT = {
    'type': 'object',
    'properties': ENCRYPTED_WALLET_SCHEMA_PROPERTIES,
    'required': [
        'data_pubkey',
        'data_pubkeys',
        'encrypted_data_privkey',
        'encrypted_owner_privkey',
        'encrypted_payment_privkey',
        'owner_addresses',
        'payment_addresses',
    ],
}

ENCRYPTED_WALLET_SCHEMA_LEGACY = {
    'type': 'object',
    'properties': ENCRYPTED_WALLET_SCHEMA_PROPERTIES,
    'required': [
        'encrypted_master_private_key'
    ],
}


WALLET_SCHEMA_PROPERTIES = {
    'data_pubkey': {
        'type': 'string',
        'pattern': OP_PUBKEY_PATTERN,
    },
    'data_pubkeys': {
        'type': 'array',
        'items': {
            'type': 'string',
            'pattern': OP_PUBKEY_PATTERN,
            'minItems': 1,
            'maxItems': 1,
        },
    },
    'data_privkey': {
        'type': 'string',
        'pattern': OP_PRIVKEY_PATTERN,
    },
    'owner_privkey': PRIVKEY_INFO_SCHEMA,
    'payment_privkey': PRIVKEY_INFO_SCHEMA,
    'owner_addresses': {
        'type': 'array',
        'items': {
            'type': 'string',
            'pattern': OP_ADDRESS_PATTERN,
            'minItems': 1,
            'maxItems': 1,
        },
    },
    'payment_addresses': {
        'type': 'array',
        'items': {
            'type': 'string',
            'pattern': OP_ADDRESS_PATTERN,
            'minItems': 1,
            'maxItems': 1,
        },
    },
}

WALLET_SCHEMA_CURRENT = {
    'type': 'object',
    'properties': WALLET_SCHEMA_PROPERTIES,
    'required': [
        'data_pubkey',
        'data_pubkeys',
        'data_privkey',
        'owner_privkey',
        'payment_privkey',
        'owner_addresses',
        'payment_addresses'
    ],
}

URI_RECORD_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string'
        },
        'priority': {
            'type': 'integer'
        },
        'weight': {
            'type': 'integer'
        },
        'target': {
            'type': 'string',
            'pattern': OP_URI_TARGET_PATTERN
        },
    },
    'required': [
        'name',
        'priority',
        'weight',
        'target'
    ],
}       

TXT_RECORD_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
            'pattern': OP_URLENCODED_PATTERN,
        },
        'txt': {
            'type': 'string',
        },
    },
    'required': [
        'name',
        'txt'
    ],
}        

USER_ZONEFILE_SCHEMA = {
    'type': 'object',
    'properties': {
        'txt': {
            'type': 'array',
            'items': TXT_RECORD_SCHEMA,
        },
        'uri': {
            'type': 'array',
            'items': URI_RECORD_SCHEMA,
        },
        '$origin': {
            'type': 'string',
            'pattern': OP_NAME_PATTERN,
        },
        '$ttl': {
            'type': 'integer'
        },
    },
    'required': [
        'txt',
        'uri',
        '$origin',
        '$ttl'
    ],
}


MUTABLE_DATUM_PERMISSIONS = {
    'type': 'object',
    'properties': {
        'owner': {
            'read': 'bool',
            'write': 'bool',
        },
        'group': {
            'read': 'bool',
            'write': 'bool',
        },
        'world': {
            'read': 'bool',
            'write': 'bool',
        },
    },
    'required': [
        'owner',
        'group',
        'world'
    ],
    'additionalProperties': False
}


MUTABLE_DATUM_FILE_TYPE = 1
MUTABLE_DATUM_DIR_TYPE = 2

MUTABLE_DATUM_SCHEMA_BASE_PROPERTIES = {
    'type': {
        # file, directory
        'type': 'integer',
        'minimum': MUTABLE_DATUM_FILE_TYPE,
        'maximum': MUTABLE_DATUM_DIR_TYPE,
    },
    'owner': {
        # hash of public key
        'type': 'string',
        'pattern': OP_ADDRESS_PATTERN
    },
    'group': {
        # group ID
        'type': 'integer'
    },
    'version': {
        # version 
        'type': 'integer'
    },
    'permissions': MUTABLE_DATUM_PERMISSIONS
}

MUTABLE_DATUM_FILE_SCHEMA_PROPERTIES = MUTABLE_DATUM_SCHEMA_BASE_PROPERTIES.copy()
MUTABLE_DATUM_DIR_SCHEMA_PROPERTIES = MUTABLE_DATUM_SCHEMA_BASE_PROPERTIES.copy()

MUTABLE_DATUM_FILE_SCHEMA_PROPERTIES.update({
    'data': {
        # raw data
        'type': 'string',
    },
})

MUTABLE_DATUM_DIRENT_SCHEMA = {
    'type': 'object',
    'properties': {
        'type': {
            'type': 'integer',
            'minimum': MUTABLE_DATUM_FILE_TYPE,
            'maximum': MUTABLE_DATUM_DIR_TYPE,
        },
        'uuid': {
            'type': 'string',
            'pattern': OP_UUID_PATTERN
        },
        'links': {
            'type': 'array',
            'items': URI_RECORD_SCHEMA
        },
    },
    'additionalProperties': False,
    'required': [
        'name',
        'links'
    ],
}

MUTABLE_DATUM_DIR_SCHEMA_PROPERTIES.update({
    'data': {
        # pointers to other files and directories
        'type': 'object',
        'patternProperties': {
            # maps name to uuid, links
            OP_URLENCODED_PATTERN: MUTABLE_DATUM_DIRENT_SCHEMA
        },
        'additionalProperties': False,
    },
})

MUTABLE_DATUM_FILE_SCHEMA = {
    'type': 'object',
    'properties': MUTABLE_DATUM_FILE_SCHEMA_PROPERTIES,
    'additionalProperties': False,
    'required': MUTABLE_DATUM_FILE_SCHEMA_PROPERTIES.keys()
}

MUTABLE_DATUM_DIR_SCHEMA = {
    'type': 'object',
    'properties': MUTABLE_DATUM_DIR_SCHEMA_PROPERTIES,
    'additionalProperties': False,
    'required': MUTABLE_DATUM_DIR_SCHEMA_PROPERTIES.keys()
}

MUTABLE_DATUM_SCHEMA = {
    'anyOf': [
        MUTABLE_DATUM_FILE_SCHEMA,
        MUTABLE_DATUM_DIR_SCHEMA
    ],
}

MUTABLE_DATA_STORE_GROUP_SCHEMA = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string',
        },
        'id': {
            'type': 'string',
            'pattern': OP_UUID_PATTERN,
        },
        'addresses': {
            'type': 'array',
            'items': {
                'type': 'string',
                'pattern': OP_ADDRESS_PATTERN
            },
        },
    },
    'additionalProperties': False,
    'required': [
        'name',
        'id',
        'addresses'
    ],
}

MUTABLE_DATA_STORE = {
    'type': 'object',
    'properties': {
        'owner': {
            'type': 'string',
            'pattern': OP_ADDRESS_PATTERN
        },
        'groups': {
            'type': 'array',
            'items': MUTABLE_DATA_STORE_GROUP_SCHEMA
        },
        'drivers': {
            'type': 'array',
            'items': 'string'
        },
        'root_uuid': {
            'type': 'string',
            'pattern': OP_UUID_PATTERN,
        },
    },
    'additionalProperties': False,
    'required': [
        'owner',
        'groups',
        'root_uuid',
        'drivers'
    ]
}


# for a profile's mutable data
PROFILE_MUTABLE_DATA_SCHEMA = {
    'type': 'object',
    'properties': {
        'data': {
            'type': 'object',
            'patternProperties': {
                OP_MUTABLE_DATA_MD_PATTERN: {
                    'type': 'object',
                    'properties'
                    'type': 'array',
                    'items': URI_RECORD_SCHEMA
                },
            },
        },
    },
    'required': [
        'data'
    ],
}


OP_HISTORY_SCHEMA = {
    'type': 'object',
    'properties': {
        'address': {
            'type': 'string',
            'pattern': OP_ADDRESS_PATTERN,
        },
        'base': {
            'type': 'integer',
        },
        'buckets': {
            'anyOf': [
                {
                    'type': 'array',
                    'items': {
                        'type': 'integer',
                        'minItems': 16,
                        'maxItems': 16,
                    },
                },
                {
                    'type': 'null',
                },
            ],
        },
        'block_number': {
            'type': 'integer',
        },
        'coeff': {
            'anyOf': [
                {
                    'type': 'integer',
                },
                {
                    'type': 'null'
                },
            ],
        },
        'consensus_hash': {
            'anyOf': [
                {
                    'type': 'string',
                    'pattern': OP_CONSENSUS_HASH_PATTERN,
                },
                {
                    'type': 'null'
                },
            ],
        },
        'fee': {
            'type': 'integer',
        },
        'first_registered': {
            'type': 'integer',
        },
        'history_snapshot': {
            'type': 'boolean',
        },
        'importer': {
            'anyOf': [
                {
                    'type': 'string',
                    'pattern': OP_P2PKH_PATTERN,
                },
                {
                    'type': 'null',
                },
            ],
        },
        'importer_address': {
            'anyOf': [
                {
                    'type': 'string',
                    'pattern': OP_ADDRESS_PATTERN,
                },
                {
                    'type': 'null',
                },
            ],
        },
        'last_renewed': {
            'type': 'integer',
        },
        'op': {
            'type': 'string',
            'pattern': OP_CODE_PATTERN,
        },
        'op_fee': {
            'type': 'number',
        },
        'opcode': {
            'type': 'string',
            'pattern': OP_CODE_NAME_PATTERN,
        },
        'revoked': {
            'type': 'boolean',
        },
        'sender': {
            'type': 'string',
            'pattern': OP_SCRIPT_PATTERN,
        },
        'sender_pubkey': {
            'anyOf': [
                {
                    'type': 'string',
                    'pattern': OP_PUBKEY_PATTERN,
                },
                {
                    'type': 'null'
                },
            ],
        },
        'recipient': {
            'anyOf': [
                {
                    'type': 'string',
                    'pattern': OP_SCRIPT_PATTERN,
                },
                {
                    'type': 'null'
                },
            ],
        },
        'recipient_address': {
            'anyOf': [
                {
                    'type': 'string',
                    'pattern': OP_ADDRESS_PATTERN,
                },
                {
                    'type': 'null'
                },
            ],
        },
        'recipient_pubkey': {
            'anyOf': [
                {
                    'type': 'string',
                    'pattern': OP_PUBKEY_PATTERN,
                },
                {
                    'type': 'null'
                },
            ],
        },
        'txid': {
            'type': 'string',
            'pattern': OP_TXID_PATTERN,
        },
        'value_hash': {
            'anyOf': [
                {
                    'type': 'string',
                    'pattern': OP_ZONEFILE_HASH_PATTERN,
                },
                {
                    'type': 'null',
                },
            ],
        },
        'vtxindex': {
            'type': 'integer',
        },
    },
    'required': [
        'op',
        'opcode',
        'txid',
        'vtxindex'
    ],
}

NAMEOP_SCHEMA_PROPERTIES = {
    'address': OP_HISTORY_SCHEMA['properties']['address'],
    'block_number': OP_HISTORY_SCHEMA['properties']['block_number'],
    'consensus_hash': OP_HISTORY_SCHEMA['properties']['consensus_hash'],
    'expire_block': {
        'type': 'integer',
    },
    'first_registered': OP_HISTORY_SCHEMA['properties']['first_registered'],
    'history': {
        'type': 'object',
        'patternProperties': {
            '^([0-9]+)$': {
                'type': 'array',
                'items': OP_HISTORY_SCHEMA,
            },
        },
    },
    'history_snapshot': {
        'type': 'boolean',
    },
    'importer': OP_HISTORY_SCHEMA['properties']['importer'],
    'importer_address': OP_HISTORY_SCHEMA['properties']['importer_address'],
    'last_renewed': OP_HISTORY_SCHEMA['properties']['last_renewed'],
    'name': {
        'type': 'string',
        'pattern': OP_NAME_PATTERN,
    },
    'op': OP_HISTORY_SCHEMA['properties']['op'],
    'op_fee': OP_HISTORY_SCHEMA['properties']['op_fee'],
    'opcode': OP_HISTORY_SCHEMA['properties']['opcode'],
    'revoked': OP_HISTORY_SCHEMA['properties']['revoked'],
    'sender': OP_HISTORY_SCHEMA['properties']['sender'],
    'sender_pubkey': OP_HISTORY_SCHEMA['properties']['sender_pubkey'],
    'recipient': OP_HISTORY_SCHEMA['properties']['recipient'],
    'recipient_address': OP_HISTORY_SCHEMA['properties']['recipient_address'],
    'txid': OP_HISTORY_SCHEMA['properties']['txid'],
    'value_hash': OP_HISTORY_SCHEMA['properties']['value_hash'],
    'vtxindex': OP_HISTORY_SCHEMA['properties']['vtxindex'],
}

NAMESPACE_SCHEMA_PROPERTIES = {
    'address': OP_HISTORY_SCHEMA['properties']['address'],
    'base': OP_HISTORY_SCHEMA['properties']['base'],
    'block_number': OP_HISTORY_SCHEMA['properties']['block_number'],
    'buckets': OP_HISTORY_SCHEMA['properties']['buckets'],
    'coeff': OP_HISTORY_SCHEMA['properties']['coeff'],
    'fee': OP_HISTORY_SCHEMA['properties']['fee'],
    'history': {
        'type': 'object',
        'patternProperties': {
            '^([0-9]+)$': {
                'type': 'array',
                'items': OP_HISTORY_SCHEMA,
            },
        },
    },
    'lifetime': {
        'type': 'integer'
    },
    'namespace_id': {
        'type': 'string',
        'pattern': OP_NAMESPACE_PATTERN,
    },
    'namespace_id_hash': {
        'type': 'string',
        'pattern': OP_NAMESPACE_HASH_PATTERN,
    },
    'no_vowel_discount': {
        'type': 'integer',
    },
    'nonalpha_discount': {
        'type': 'integer',
    },
    'op': OP_HISTORY_SCHEMA['properties']['op'],
    'ready': {
        'type': 'boolean',
    },
    'ready_block': {
        'type': 'integer',
    },
    'recipient': OP_HISTORY_SCHEMA['properties']['recipient'],
    'recipient_address': OP_HISTORY_SCHEMA['properties']['recipient_address'],
    'reveal_block': {
        'type': 'integer',
    },
    'sender': OP_HISTORY_SCHEMA['properties']['sender'],
    'sender_pubkey': OP_HISTORY_SCHEMA['properties']['sender_pubkey'],
    'txid': OP_HISTORY_SCHEMA['properties']['txid'],
    'version': {
        'type': 'integer',
    },
    'vtxindex': OP_HISTORY_SCHEMA['properties']['vtxindex'],
}

NAMEOP_SCHEMA_REQUIRED = [
    'address',
    'block_number',
    'op',
    'op_fee',
    'opcode',
    'sender',
    'txid',
    'vtxindex'
]

NAMESPACE_SCHEMA_REQUIRED = [
    'address',
    'base',
    'block_number',
    'buckets',
    'coeff',
    'lifetime',
    'namespace_id',
    'no_vowel_discount',
    'nonalpha_discount',
    'op',
    'ready',
    'recipient',
    'recipient_address',
    'reveal_block',
    'sender',
    'sender_pubkey',
    'txid',
    'version',
    'vtxindex'
]

