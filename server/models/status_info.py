# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server import util


class StatusInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, number: str=None, state: str=None, type: str=None, cert: str=None, npx: str=None, po: str=None, part_number: str=None, quantity: str=None, needs: str=None, status: str=None, ship_date: str=None, notes: str=None):  # noqa: E501
        """StatusInfo - a model defined in Swagger

        :param number: The number of this StatusInfo.  # noqa: E501
        :type number: str
        :param state: The state of this StatusInfo.  # noqa: E501
        :type state: str
        :param type: The type of this StatusInfo.  # noqa: E501
        :type type: str
        :param cert: The cert of this StatusInfo.  # noqa: E501
        :type cert: str
        :param npx: The npx of this StatusInfo.  # noqa: E501
        :type npx: str
        :param po: The po of this StatusInfo.  # noqa: E501
        :type po: str
        :param part_number: The part_number of this StatusInfo.  # noqa: E501
        :type part_number: str
        :param quantity: The quantity of this StatusInfo.  # noqa: E501
        :type quantity: str
        :param needs: The needs of this StatusInfo.  # noqa: E501
        :type needs: str
        :param status: The status of this StatusInfo.  # noqa: E501
        :type status: str
        :param ship_date: The ship_date of this StatusInfo.  # noqa: E501
        :type ship_date: str
        :param notes: The notes of this StatusInfo.  # noqa: E501
        :type notes: str
        """
        self.swagger_types = {
            'number': str,
            'state': str,
            'type': str,
            'cert': str,
            'npx': str,
            'po': str,
            'part_number': str,
            'quantity': str,
            'needs': str,
            'status': str,
            'ship_date': str,
            'notes': str
        }

        self.attribute_map = {
            'number': 'number',
            'state': 'state',
            'type': 'type',
            'cert': 'cert',
            'npx': 'npx',
            'po': 'po',
            'part_number': 'part_number',
            'quantity': 'quantity',
            'needs': 'needs',
            'status': 'status',
            'ship_date': 'ship_date',
            'notes': 'notes'
        }
        self._number = number
        self._state = state
        self._type = type
        self._cert = cert
        self._npx = npx
        self._po = po
        self._part_number = part_number
        self._quantity = quantity
        self._needs = needs
        self._status = status
        self._ship_date = ship_date
        self._notes = notes

    @classmethod
    def from_dict(cls, dikt) -> 'StatusInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The statusInfo of this StatusInfo.  # noqa: E501
        :rtype: StatusInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number(self) -> str:
        """Gets the number of this StatusInfo.


        :return: The number of this StatusInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number: str):
        """Sets the number of this StatusInfo.


        :param number: The number of this StatusInfo.
        :type number: str
        """

        self._number = number

    @property
    def state(self) -> str:
        """Gets the state of this StatusInfo.


        :return: The state of this StatusInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this StatusInfo.


        :param state: The state of this StatusInfo.
        :type state: str
        """

        self._state = state

    @property
    def type(self) -> str:
        """Gets the type of this StatusInfo.


        :return: The type of this StatusInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this StatusInfo.


        :param type: The type of this StatusInfo.
        :type type: str
        """

        self._type = type

    @property
    def cert(self) -> str:
        """Gets the cert of this StatusInfo.


        :return: The cert of this StatusInfo.
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert: str):
        """Sets the cert of this StatusInfo.


        :param cert: The cert of this StatusInfo.
        :type cert: str
        """

        self._cert = cert

    @property
    def npx(self) -> str:
        """Gets the npx of this StatusInfo.


        :return: The npx of this StatusInfo.
        :rtype: str
        """
        return self._npx

    @npx.setter
    def npx(self, npx: str):
        """Sets the npx of this StatusInfo.


        :param npx: The npx of this StatusInfo.
        :type npx: str
        """

        self._npx = npx

    @property
    def po(self) -> str:
        """Gets the po of this StatusInfo.


        :return: The po of this StatusInfo.
        :rtype: str
        """
        return self._po

    @po.setter
    def po(self, po: str):
        """Sets the po of this StatusInfo.


        :param po: The po of this StatusInfo.
        :type po: str
        """

        self._po = po

    @property
    def part_number(self) -> str:
        """Gets the part_number of this StatusInfo.


        :return: The part_number of this StatusInfo.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number: str):
        """Sets the part_number of this StatusInfo.


        :param part_number: The part_number of this StatusInfo.
        :type part_number: str
        """

        self._part_number = part_number

    @property
    def quantity(self) -> str:
        """Gets the quantity of this StatusInfo.


        :return: The quantity of this StatusInfo.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: str):
        """Sets the quantity of this StatusInfo.


        :param quantity: The quantity of this StatusInfo.
        :type quantity: str
        """

        self._quantity = quantity

    @property
    def needs(self) -> str:
        """Gets the needs of this StatusInfo.


        :return: The needs of this StatusInfo.
        :rtype: str
        """
        return self._needs

    @needs.setter
    def needs(self, needs: str):
        """Sets the needs of this StatusInfo.


        :param needs: The needs of this StatusInfo.
        :type needs: str
        """

        self._needs = needs

    @property
    def status(self) -> str:
        """Gets the status of this StatusInfo.


        :return: The status of this StatusInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this StatusInfo.


        :param status: The status of this StatusInfo.
        :type status: str
        """

        self._status = status

    @property
    def ship_date(self) -> str:
        """Gets the ship_date of this StatusInfo.


        :return: The ship_date of this StatusInfo.
        :rtype: str
        """
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date: str):
        """Sets the ship_date of this StatusInfo.


        :param ship_date: The ship_date of this StatusInfo.
        :type ship_date: str
        """

        self._ship_date = ship_date

    @property
    def notes(self) -> str:
        """Gets the notes of this StatusInfo.


        :return: The notes of this StatusInfo.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """Sets the notes of this StatusInfo.


        :param notes: The notes of this StatusInfo.
        :type notes: str
        """

        self._notes = notes
