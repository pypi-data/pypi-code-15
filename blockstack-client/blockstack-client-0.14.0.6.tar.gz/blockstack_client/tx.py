#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

import os
import sys
import pybitcoin
from .operations import *
from .config import CONFIG_PATH, get_utxo_provider_client, get_tx_broadcaster, get_logger
from pybitcoin import serialize_transaction, sign_all_unsigned_inputs, broadcast_transaction

from .scripts import tx_sign_all_unsigned_inputs 

log = get_logger("blockstack-client")

def preorder_tx( *args, **kw ):
    """
    Make an unsigned preorder transaction
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_preorder( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def register_tx( *args, **kw ):
    """
    Make an unsigned register transaction
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_register( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def update_tx( *args, **kw ):
    """
    Make an unsigned update transaction
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_update( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def transfer_tx( *args, **kw ):
    """
    Make an unsigned transfer transaction
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_transfer( *args, **kw ) 
    return pybitcoin.serialize_transaction( inputs, outputs )


def revoke_tx( *args, **kw ):
    """
    Make an unsigned revoke transaction
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_revoke( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def namespace_preorder_tx( *args, **kw ):
    """
    Make an unsigned namespace preorder transaction
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_namespace_preorder( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def namespace_reveal_tx( *args, **kw ):
    """
    Make an unsigned namespace reveal transaction 
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_namespace_reveal( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def namespace_ready_tx( *args, **kw ):
    """
    Make an unsigned namespace ready transaction 
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_namespace_ready( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def name_import_tx( *args, **kw ):
    """
    Make an unsigned name import transaction
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_name_import( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def announce_tx( *args, **kw ):
    """
    Make an unsigned announce transaction
    Raise ValueError if there are not enough inputs to make the transaction
    """
    inputs, outputs = tx_announce( *args, **kw )
    return pybitcoin.serialize_transaction( inputs, outputs )


def sign_tx( tx_hex, private_key_info ):
    """
    Sign a transaction
    """
    return tx_sign_all_unsigned_inputs( private_key_info, tx_hex )


def broadcast_tx( tx_hex, config_path=CONFIG_PATH, tx_broadcaster=None ):
    """
    Send a signed transaction to the blockchain
    """
    if tx_broadcaster is None:
        tx_broadcaster = get_tx_broadcaster( config_path=config_path )

    if os.environ.get("BLOCKSTACK_TEST") == "1":
        log.debug("Send %s" % tx_hex)

    resp = {}
    try:
        resp = broadcast_transaction( tx_hex, tx_broadcaster )
        if 'tx_hash' not in resp or 'error' in resp:
            log.error("Failed to send %s" % tx_hex)
            resp['error'] = 'Failed to broadcast transaction: %s' % tx_hex
            return resp

    except Exception, e:
        log.exception(e)
        resp['error'] = 'Failed to broadcast transaction: %s' % tx_hex

        if os.environ.get("BLOCKSTACK_TEST") == "1":
            # should NEVER happen in test mode
            log.error("FATAL: failed to send transaction:\n%s" % simplejson.dumps(resp, indent=4, sort_keys=True))
            sys.exit(1)

    # for compatibility
    resp['transaction_hash'] = resp['tx_hash']
    del resp['tx_hash']
    return resp


def sign_and_broadcast_tx( tx_hex, private_key_info, config_path=CONFIG_PATH, tx_broadcaster=None ):
    """
    Sign and send a transaction
    """
    signed_tx = sign_tx( tx_hex, private_key_info )
    try:
        resp = broadcast_tx( signed_tx, config_path=config_path, tx_broadcaster=tx_broadcaster )
    except Exception, e:
        log.exception(e)
        log.error("Failed to broadcast transaction %s" % signed_tx)
        return {'error': 'Failed to broadcast transaction (caught exception)'}

    if 'error' in resp:
        log.error("Failed to broadcast transaction: %s" % resp['error'])

    return resp

