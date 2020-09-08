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


class MediaJobOutputStateChangeEventData(Model):
    """Schema of the Data property of an EventGridEvent for a
    Microsoft.Media.JobOutputStateChange event.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar previous_state: The previous state of the Job. Possible values
     include: 'Canceled', 'Canceling', 'Error', 'Finished', 'Processing',
     'Queued', 'Scheduled'
    :vartype previous_state: str or ~azure.eventgrid.models.MediaJobState
    :param output: Gets the output.
    :type output: ~azure.eventgrid.models.MediaJobOutput
    :param job_correlation_data: Gets the Job correlation data.
    :type job_correlation_data: dict[str, str]
    """

    _validation = {
        'previous_state': {'readonly': True},
    }

    _attribute_map = {
        'previous_state': {'key': 'previousState', 'type': 'MediaJobState'},
        'output': {'key': 'output', 'type': 'MediaJobOutput'},
        'job_correlation_data': {'key': 'jobCorrelationData', 'type': '{str}'},
    }

    def __init__(self, *, output=None, job_correlation_data=None, **kwargs) -> None:
        super(MediaJobOutputStateChangeEventData, self).__init__(**kwargs)
        self.previous_state = None
        self.output = output
        self.job_correlation_data = job_correlation_data