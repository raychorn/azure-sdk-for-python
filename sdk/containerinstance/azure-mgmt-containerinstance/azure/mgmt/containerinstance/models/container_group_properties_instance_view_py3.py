# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerGroupPropertiesInstanceView(Model):
    """The instance view of the container group. Only valid in response.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar events: The events of this container group.
    :vartype events: list[~azure.mgmt.containerinstance.models.Event]
    :ivar state: The state of the container group. Only valid in response.
    :vartype state: str
    """

    _validation = {
        'events': {'readonly': True},
        'state': {'readonly': True},
    }

    _attribute_map = {
        'events': {'key': 'events', 'type': '[Event]'},
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(ContainerGroupPropertiesInstanceView, self).__init__(**kwargs)
        self.events = None
        self.state = None