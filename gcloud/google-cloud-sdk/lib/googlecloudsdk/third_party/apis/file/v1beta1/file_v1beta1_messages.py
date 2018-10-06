"""Generated message classes for file version v1beta1.

The Cloud Filestore API is used for creating and managing cloud file servers.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'file'


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class ClientList(_messages.Message):
  r"""The sets of network addresses and DNS names for hosts to which a given
  export or share should be allowed or denied.

  Fields:
    hostNames: DNS names of hosts, with optional wildcards.
    ipAddresses: IPv4 addresses in the format {octet 1}.{octet 2}.{octet
      3}.{octet 4}.
  """

  hostNames = _messages.StringField(1, repeated=True)
  ipAddresses = _messages.StringField(2, repeated=True)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class Export(_messages.Message):
  r"""File share export specification.

  Fields:
    allowedClients: The clients which may connect.
    async: Writes may be completed when not yet on stable storage.
    deniedClients: The clients which may not connect.
    networks: Networks on which the export should appear. If none are
      specified, the default is all networks to which the instance is
      connected to.
    nfsExport: Export rule for NFS
    path: Path to export (either "" or of the form /file_share_name[/subdir]).
    readOnly: Whether the file share should be exported as read-only.
    smbExport: Export rule for SMB
  """

  allowedClients = _messages.MessageField('ClientList', 1)
  async = _messages.BooleanField(2)
  deniedClients = _messages.MessageField('ClientList', 3)
  networks = _messages.MessageField('NetworkConfig', 4, repeated=True)
  nfsExport = _messages.MessageField('NfsExport', 5)
  path = _messages.StringField(6)
  readOnly = _messages.BooleanField(7)
  smbExport = _messages.MessageField('SmbExport', 8)


class FileProjectsLocationsGetRequest(_messages.Message):
  r"""A FileProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class FileProjectsLocationsInstancesCreateRequest(_messages.Message):
  r"""A FileProjectsLocationsInstancesCreateRequest object.

  Fields:
    instance: A Instance resource to be passed as the request body.
    instanceId: The name of the instance to create. The name must be unique
      for the specified project and location.
    parent: The instance's project and location, in the format
      projects/{project_id}/locations/{location}. In Cloud Filestore,
      locations map to GCP zones, for example **us-west1-b**.
  """

  instance = _messages.MessageField('Instance', 1)
  instanceId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class FileProjectsLocationsInstancesDeleteRequest(_messages.Message):
  r"""A FileProjectsLocationsInstancesDeleteRequest object.

  Fields:
    name: The instance resource name, in the format
      projects/{project_id}/locations/{location}/instances/{instance_id}
  """

  name = _messages.StringField(1, required=True)


class FileProjectsLocationsInstancesGetRequest(_messages.Message):
  r"""A FileProjectsLocationsInstancesGetRequest object.

  Fields:
    name: The instance resource name, in the format
      projects/{project_id}/locations/{location}/instances/{instance_id}.
  """

  name = _messages.StringField(1, required=True)


class FileProjectsLocationsInstancesListRequest(_messages.Message):
  r"""A FileProjectsLocationsInstancesListRequest object.

  Fields:
    filter: List filter.
    orderBy: Sort results. Supported values are "name", "name desc" or ""
      (unsorted).
    pageSize: The maximum number of items to return.
    pageToken: The next_page_token value to use if there are additional
      results to retrieve for this list request.
    parent: The project and location for which to retrieve instance
      information, in the format projects/{project_id}/locations/{location}.
      In Cloud Filestore, locations map to GCP zones, for example **us-
      west1-b**. To retrieve instance information for all locations, use "-"
      for the {location} value.
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class FileProjectsLocationsInstancesPatchRequest(_messages.Message):
  r"""A FileProjectsLocationsInstancesPatchRequest object.

  Fields:
    instance: A Instance resource to be passed as the request body.
    name: Output only. The resource name of the instance, in the format
      projects/{project_id}/locations/{location_id}/instances/{instance_id}.
    updateMask: Mask of fields to update.  At least one path must be supplied
      in this field.  The elements of the repeated paths field may only
      include these fields: "description"
  """

  instance = _messages.MessageField('Instance', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class FileProjectsLocationsListRequest(_messages.Message):
  r"""A FileProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class FileProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A FileProjectsLocationsOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class FileProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A FileProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class FileProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A FileProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class FileProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A FileProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class FileShareConfig(_messages.Message):
  r"""File share configuration for the instance.

  Enums:
    ProtocolsValueListEntryValuesEnum:

  Fields:
    capacityGb: File share capacity in gigabytes (GB). Cloud Filestore defines
      1 GB as 1024^3 bytes.
    deleted: Delete requested. The file share will be deleted.
    enabled: Service enabled.  When enabled, the instance exposes the exports
      to the user for mounting.
    exports: Exports. If protocols and exports are both zero-length, a default
      protocol of NFSV3 and a default export of "*" are provided, and enabled
      is set to true.
    name: The name of the file share (must be 16 characters or less).
    protocols: Protocols supported.
  """

  class ProtocolsValueListEntryValuesEnum(_messages.Enum):
    r"""ProtocolsValueListEntryValuesEnum enum type.

    Values:
      FILE_SHARE_PROTOCOL_UNSPECIFIED: <no description>
      NFS_V3: <no description>
      NFS_V4_0: <no description>
      NFS_V4_1: <no description>
      SMB_V2_0: <no description>
      SMB_V2_1: <no description>
      SMB_V3: <no description>
    """
    FILE_SHARE_PROTOCOL_UNSPECIFIED = 0
    NFS_V3 = 1
    NFS_V4_0 = 2
    NFS_V4_1 = 3
    SMB_V2_0 = 4
    SMB_V2_1 = 5
    SMB_V3 = 6

  capacityGb = _messages.IntegerField(1)
  deleted = _messages.BooleanField(2)
  enabled = _messages.BooleanField(3)
  exports = _messages.MessageField('Export', 4, repeated=True)
  name = _messages.StringField(5)
  protocols = _messages.EnumField('ProtocolsValueListEntryValuesEnum', 6, repeated=True)


class Instance(_messages.Message):
  r"""A Cloud Filestore instance.

  Enums:
    StateValueValuesEnum: Output only. The instance state.
    TierValueValuesEnum: The service tier of the instance.

  Messages:
    LabelsValue: Resource labels to represent user provided metadata.

  Fields:
    createTime: Output only. The time when the instance was created.
    description: Optional. A description of the instance (2048 characters or
      less).
    etag: Server-specified ETag for the instance resource to prevent
      simultaneous updates from overwriting each other.
    fileShares: File system shares on the instance. For this version, only a
      single file share is supported.
    labels: Resource labels to represent user provided metadata.
    loggingService: The logging service the instance should use to write logs.
      Currently available options:  * `logging.googleapis.com` - the Google
      Cloud Logging service. * `none` - no logs will be exported from the
      instance. * if left as an empty string,`logging.googleapis.com` will be
      used.
    monitoringService: The monitoring service the instance should use to write
      metrics. Currently available options:  * `monitoring.googleapis.com` -
      the Google Cloud Monitoring service. * `none` - no metrics will be
      exported from the instance. * if left as an empty string,
      `monitoring.googleapis.com` will be used.
    name: Output only. The resource name of the instance, in the format
      projects/{project_id}/locations/{location_id}/instances/{instance_id}.
    networks: VPC networks to which the instance is connected. For this
      version, only a single network is supported.
    state: Output only. The instance state.
    statusMessage: Output only. Additional information about the instance
      state, if available.
    tier: The service tier of the instance.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. The instance state.

    Values:
      STATE_UNSPECIFIED: State not set.
      CREATING: The instance is being created.
      READY: The instance is available for use.
      REPAIRING: Work is being done on the instance. You can get further
        details from the `statusMessage` field of the `Instance` resource.
      DELETING: The instance is shutting down.
      ERROR: The instance is experiencing an issue and might be unusable. You
        can get further details from the `statusMessage` field of the
        `Instance` resource.
    """
    STATE_UNSPECIFIED = 0
    CREATING = 1
    READY = 2
    REPAIRING = 3
    DELETING = 4
    ERROR = 5

  class TierValueValuesEnum(_messages.Enum):
    r"""The service tier of the instance.

    Values:
      TIER_UNSPECIFIED: Not set.
      STANDARD: STANDARD tier.
      PREMIUM: PREMIUM tier.
    """
    TIER_UNSPECIFIED = 0
    STANDARD = 1
    PREMIUM = 2

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Resource labels to represent user provided metadata.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  description = _messages.StringField(2)
  etag = _messages.StringField(3)
  fileShares = _messages.MessageField('FileShareConfig', 4, repeated=True)
  labels = _messages.MessageField('LabelsValue', 5)
  loggingService = _messages.StringField(6)
  monitoringService = _messages.StringField(7)
  name = _messages.StringField(8)
  networks = _messages.MessageField('NetworkConfig', 9, repeated=True)
  state = _messages.EnumField('StateValueValuesEnum', 10)
  statusMessage = _messages.StringField(11)
  tier = _messages.EnumField('TierValueValuesEnum', 12)


class ListInstancesResponse(_messages.Message):
  r"""ListInstancesResponse is the result of ListInstancesRequest.

  Fields:
    instances: A list of instances in the project for the specified location.
      If the {location} value in the request is "-", the response contains a
      list of instances from all locations. If any location is unreachable,
      the response will only return instances in reachable locations and the
      "unreachable" field will be populated with a list of unreachable
      locations.
    nextPageToken: The token you can use to retrieve the next page of results.
      Not returned if there are no more results in the list.
    unreachable: Locations that could not be reached.
  """

  instances = _messages.MessageField('Instance', 1, repeated=True)
  nextPageToken = _messages.StringField(2)
  unreachable = _messages.StringField(3, repeated=True)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class NetworkConfig(_messages.Message):
  r"""Network configuration for the instance.

  Enums:
    ModesValueListEntryValuesEnum:

  Fields:
    ipAddresses: Output only. IPv4 addresses in the format {octet 1}.{octet
      2}.{octet 3}.{octet 4} or IPv6 addresses in the format {block 1}:{block
      2}:{block 3}:{block 4}:{block 5}:{block 6}:{block 7}:{block 8}.
    modes: Internet protocol versions for which the instance has IP addresses
      assigned. For this version, only MODE_IPV4 is supported.
    network: The name of the Google Compute Engine [VPC network](/compute/docs
      /networks-and-firewalls#networks) to which the instance is connected.
    reservedIpRange: A /29 CIDR block in one of the [internal IP address
      ranges](https://www.arin.net/knowledge/address_filters.html) that
      identifies the range of IP addresses reserved for this instance. For
      example, 10.0.0.0/29 or 192.168.0.0/29. The range you specify can't
      overlap with either existing subnets or assigned IP address ranges for
      other Cloud Filestore instances in the selected VPC network.
    subnetwork: Output only. The name of the Google Compute Engine
      [subnetwork](/compute/docs/subnetworks) to which the instance is
      connected.
  """

  class ModesValueListEntryValuesEnum(_messages.Enum):
    r"""ModesValueListEntryValuesEnum enum type.

    Values:
      ADDRESS_MODE_UNSPECIFIED: <no description>
      MODE_IPV4: <no description>
      MODE_IPV6: <no description>
    """
    ADDRESS_MODE_UNSPECIFIED = 0
    MODE_IPV4 = 1
    MODE_IPV6 = 2

  ipAddresses = _messages.StringField(1, repeated=True)
  modes = _messages.EnumField('ModesValueListEntryValuesEnum', 2, repeated=True)
  network = _messages.StringField(3)
  reservedIpRange = _messages.StringField(4)
  subnetwork = _messages.StringField(5)


class NfsExport(_messages.Message):
  r"""NfsExport specifies attributes of a given NFS export rule.

  Enums:
    ProtocolsValueListEntryValuesEnum:
    SquashValueValuesEnum: The mode of mapping of UIDs and GIDs (if any).

  Fields:
    anonymousGid: GID for anonymous or squashed GIDs.
    anonymousUid: UID for anonymous or squashed UIDs.
    protocols: Network transport protocols to be enabled. The default is TCP.
    squash: The mode of mapping of UIDs and GIDs (if any).
    unauthenticatedLocksAllowed: If unauthenticated_locks_allowed is true,
      locking requests do not require authentication.
    userPortsAllowed: If user_ports_allowed is true, client ports greater than
      or equal to 1024 are allowed.
  """

  class ProtocolsValueListEntryValuesEnum(_messages.Enum):
    r"""ProtocolsValueListEntryValuesEnum enum type.

    Values:
      NETWORK_PROTOCOLS_UNSPECIFIED: <no description>
      TCP: <no description>
      UDP: <no description>
    """
    NETWORK_PROTOCOLS_UNSPECIFIED = 0
    TCP = 1
    UDP = 2

  class SquashValueValuesEnum(_messages.Enum):
    r"""The mode of mapping of UIDs and GIDs (if any).

    Values:
      SQUASH_MODE_UNSPECIFIED: No mapping.
      ROOT: UID 0 maps to anon_uid and GID 0 maps to anon_gid.
      ALL: All UIDs map to anon_uid and all GIDs map to anon_gid.
    """
    SQUASH_MODE_UNSPECIFIED = 0
    ROOT = 1
    ALL = 2

  anonymousGid = _messages.IntegerField(1)
  anonymousUid = _messages.IntegerField(2)
  protocols = _messages.EnumField('ProtocolsValueListEntryValuesEnum', 3, repeated=True)
  squash = _messages.EnumField('SquashValueValuesEnum', 4)
  unauthenticatedLocksAllowed = _messages.BooleanField(5)
  userPortsAllowed = _messages.BooleanField(6)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  r"""Represents the metadata of the long-running operation.

  Fields:
    apiVersion: [Output only] API version used to start the operation.
    cancelRequested: [Output only] Identifies whether the user has requested
      cancellation of the operation. Operations that have successfully been
      cancelled have Operation.error value with a google.rpc.Status.code of 1,
      corresponding to `Code.CANCELLED`.
    createTime: [Output only] The time the operation was created.
    endTime: [Output only] The time the operation finished running.
    statusDetail: [Output only] Human-readable status of the operation, if
      any.
    target: [Output only] Server-defined resource path for the target of the
      operation.
    verb: [Output only] Name of the verb executed by the operation.
  """

  apiVersion = _messages.StringField(1)
  cancelRequested = _messages.BooleanField(2)
  createTime = _messages.StringField(3)
  endTime = _messages.StringField(4)
  statusDetail = _messages.StringField(5)
  target = _messages.StringField(6)
  verb = _messages.StringField(7)


class SmbExport(_messages.Message):
  r"""SmbExport defines attributes of a given SMB sharing rule.

  Fields:
    browsable: If true, allow clients to see this share when browsing the
      instance for shares.
    fileShare: The published name of the share (if different from name).
  """

  browsable = _messages.BooleanField(1)
  fileShare = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
