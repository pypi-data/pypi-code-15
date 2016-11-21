"""
    Slixmpp: The Slick XMPP Library
    Copyright (C) 2010 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of Slixmpp.

    See the file LICENSE for copying permission.
"""

import logging
from slixmpp.plugins import BasePlugin
from .. xmlstream.handler.callback import Callback
from .. xmlstream.matcher.xpath import MatchXPath
from .. xmlstream.stanzabase import register_stanza_plugin, ElementBase, ET, JID
from .. stanza.iq import Iq


log = logging.getLogger(__name__)


class GmailQuery(ElementBase):
    namespace = 'google:mail:notify'
    name = 'query'
    plugin_attrib = 'gmail'
    interfaces = {'newer-than-time', 'newer-than-tid', 'q', 'search'}

    def get_search(self):
        return self['q']

    def set_search(self, search):
        self['q'] = search

    def del_search(self):
        del self['q']


class MailBox(ElementBase):
    namespace = 'google:mail:notify'
    name = 'mailbox'
    plugin_attrib = 'mailbox'
    interfaces = {'result-time', 'total-matched', 'total-estimate',
                  'url', 'threads', 'matched', 'estimate'}

    def get_threads(self):
        threads = []
        for threadXML in self.xml.findall('{%s}%s' % (MailThread.namespace,
                                                      MailThread.name)):
            threads.append(MailThread(xml=threadXML, parent=None))
        return threads

    def get_matched(self):
        return self['total-matched']

    def get_estimate(self):
        return self['total-estimate'] == '1'


class MailThread(ElementBase):
    namespace = 'google:mail:notify'
    name = 'mail-thread-info'
    plugin_attrib = 'thread'
    interfaces = {'tid', 'participation', 'messages', 'date',
                  'senders', 'url', 'labels', 'subject', 'snippet'}
    sub_interfaces = {'labels', 'subject', 'snippet'}

    def get_senders(self):
        senders = []
        sendersXML = self.xml.find('{%s}senders' % self.namespace)
        if sendersXML is not None:
            for senderXML in sendersXML.findall('{%s}sender' % self.namespace):
                senders.append(MailSender(xml=senderXML, parent=None))
        return senders


class MailSender(ElementBase):
    namespace = 'google:mail:notify'
    name = 'sender'
    plugin_attrib = 'sender'
    interfaces = {'address', 'name', 'originator', 'unread'}

    def get_originator(self):
        return self.xml.attrib.get('originator', '0') == '1'

    def get_unread(self):
        return self.xml.attrib.get('unread', '0') == '1'


class NewMail(ElementBase):
    namespace = 'google:mail:notify'
    name = 'new-mail'
    plugin_attrib = 'new-mail'


class gmail_notify(BasePlugin):
    """
    Google Talk: Gmail Notifications
    """

    def plugin_init(self):
        self.description = 'Google Talk: Gmail Notifications'

        self.xmpp.registerHandler(
            Callback('Gmail Result',
                     MatchXPath('{%s}iq/{%s}%s' % (self.xmpp.default_ns,
                                                   MailBox.namespace,
                                                   MailBox.name)),
                     self.handle_gmail))

        self.xmpp.registerHandler(
            Callback('Gmail New Mail',
                     MatchXPath('{%s}iq/{%s}%s' % (self.xmpp.default_ns,
                                                   NewMail.namespace,
                                                   NewMail.name)),
                     self.handle_new_mail))

        register_stanza_plugin(Iq, GmailQuery)
        register_stanza_plugin(Iq, MailBox)
        register_stanza_plugin(Iq, NewMail)

        self.last_result_time = None

    def handle_gmail(self, iq):
        mailbox = iq['mailbox']
        approx = ' approximately' if mailbox['estimated'] else ''
        log.info('Gmail: Received%s %s emails', approx, mailbox['total-matched'])
        self.last_result_time = mailbox['result-time']
        self.xmpp.event('gmail_messages', iq)

    def handle_new_mail(self, iq):
        log.info("Gmail: New emails received!")
        self.xmpp.event('gmail_notify')
        self.checkEmail()

    def getEmail(self, query=None):
        return self.search(query)

    def checkEmail(self):
        return self.search(newer=self.last_result_time)

    def search(self, query=None, newer=None):
        if query is None:
            log.info("Gmail: Checking for new emails")
        else:
            log.info('Gmail: Searching for emails matching: "%s"', query)
        iq = self.xmpp.Iq()
        iq['type'] = 'get'
        iq['to'] = self.xmpp.boundjid.bare
        iq['gmail']['q'] = query
        iq['gmail']['newer-than-time'] = newer
        return iq.send()
