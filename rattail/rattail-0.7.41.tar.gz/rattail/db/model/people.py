# -*- coding: utf-8 -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2016 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU Affero General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for
#  more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Data Models for People
"""

from __future__ import unicode_literals, absolute_import

import datetime

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.orderinglist import ordering_list

from .core import Base, uuid_column
from .contact import PhoneNumber, EmailAddress, MailingAddress
from rattail.db.util import normalize_full_name


# TODO: deprecate/remove this
def get_person_display_name(first_name, last_name):
    return normalize_full_name(first_name, last_name)

# TODO: rename this?
def get_person_display_name_from_context(context):
    first_name = context.current_parameters.get('first_name')
    last_name = context.current_parameters.get('last_name')
    return normalize_full_name(first_name, last_name)


class Person(Base):
    """
    Represents a real, living and breathing person.

    (Or, at least was previously living and breathing, in the case of the
    deceased.)
    """
    __tablename__ = 'person'
    __versioned__ = {}

    uuid = uuid_column()
    first_name = sa.Column(sa.String(length=50), nullable=True)
    middle_name = sa.Column(sa.String(length=50), nullable=True)
    last_name = sa.Column(sa.String(length=50), nullable=True)
    display_name = sa.Column(sa.String(length=100), default=get_person_display_name_from_context)
    modified = sa.Column(sa.DateTime(), nullable=True, onupdate=datetime.datetime.utcnow)

    def __unicode__(self):
        return unicode(self.display_name or '')

    def add_email_address(self, address, type='Home'):
        email = PersonEmailAddress(address=address, type=type)
        self.emails.append(email)
        return email

    def add_phone_number(self, number, type='Home'):
        phone = PersonPhoneNumber(number=number, type=type)
        self.phones.append(phone)
        return phone


class PersonPhoneNumber(PhoneNumber):
    """
    Represents a phone (or fax) number associated with a person.
    """

    __mapper_args__ = {'polymorphic_identity': 'Person'}


Person.phones = orm.relationship(
    PersonPhoneNumber,
    primaryjoin=PersonPhoneNumber.parent_uuid == Person.uuid,
    foreign_keys=[PersonPhoneNumber.parent_uuid],
    collection_class=ordering_list('preference', count_from=1),
    order_by=PersonPhoneNumber.preference,
    cascade='save-update, merge, delete, delete-orphan',
    doc="""
    Sequence of :class:`PersonPhoneNUmber` instances which belong to the
    person.
    """,
    backref=orm.backref(
        'person',
        doc="""
        Reference to the :class:`Person` instance to which the phone number
        belongs.
        """),
)

Person.phone = orm.relationship(
    PersonPhoneNumber,
    primaryjoin=sa.and_(
        PersonPhoneNumber.parent_uuid == Person.uuid,
        PersonPhoneNumber.preference == 1,
        ),
    foreign_keys=[PersonPhoneNumber.parent_uuid],
    uselist=False,
    viewonly=True)


class PersonEmailAddress(EmailAddress):
    """
    Represents an email address associated with a person.
    """

    __mapper_args__ = {'polymorphic_identity': 'Person'}


Person.emails = orm.relationship(
    PersonEmailAddress,
    primaryjoin=PersonEmailAddress.parent_uuid == Person.uuid,
    foreign_keys=[PersonEmailAddress.parent_uuid],
    collection_class=ordering_list('preference', count_from=1),
    order_by=PersonEmailAddress.preference,
    cascade='save-update, merge, delete, delete-orphan',
    doc="""
    Sequence of :class:`PersonEmailAddress` instances which belong to the
    person.
    """,
    backref=orm.backref(
        'person',
        doc="""
        Reference to the :class:`Person` instance to which the email address
        belongs.
        """),
)

Person.email = orm.relationship(
    PersonEmailAddress,
    primaryjoin=sa.and_(
        PersonEmailAddress.parent_uuid == Person.uuid,
        PersonEmailAddress.preference == 1,
        ),
    foreign_keys=[PersonEmailAddress.parent_uuid],
    uselist=False,
    viewonly=True)


class PersonMailingAddress(MailingAddress):
    """
    Represents a physical / mailing address associated with a person.
    """

    __mapper_args__ = {'polymorphic_identity': 'Person'}


Person.addresses = orm.relationship(
    PersonMailingAddress,
    backref='person',
    primaryjoin=PersonMailingAddress.parent_uuid == Person.uuid,
    foreign_keys=[PersonMailingAddress.parent_uuid],
    collection_class=ordering_list('preference', count_from=1),
    order_by=PersonMailingAddress.preference,
    cascade='save-update, merge, delete, delete-orphan')

Person.address = orm.relationship(
    PersonMailingAddress,
    primaryjoin=sa.and_(
        PersonMailingAddress.parent_uuid == Person.uuid,
        PersonMailingAddress.preference == 1,
        ),
    foreign_keys=[PersonMailingAddress.parent_uuid],
    uselist=False,
    viewonly=True)
