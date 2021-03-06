# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='bithorde.proto',
  package='bithorde',
  serialized_pb='\n\x0e\x62ithorde.proto\x12\x08\x62ithorde\":\n\nIdentifier\x12 \n\x04type\x18\x01 \x02(\x0e\x32\x12.bithorde.HashType\x12\n\n\x02id\x18\x02 \x02(\x0c\"E\n\tHandShake\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x17\n\x0cprotoversion\x18\x02 \x02(\r:\x01\x32\x12\x11\n\tchallenge\x18\x03 \x01(\x0c\"d\n\x12HandShakeConfirmed\x12$\n\x06\x63ipher\x18\x01 \x01(\x0e\x32\x14.bithorde.CipherType\x12\x10\n\x08\x63ipheriv\x18\x02 \x01(\x0c\x12\x16\n\x0e\x61uthentication\x18\x03 \x02(\x0c\"b\n\x08\x42indRead\x12\x0e\n\x06handle\x18\x01 \x02(\r\x12!\n\x03ids\x18\x02 \x03(\x0b\x32\x14.bithorde.Identifier\x12\x12\n\nrequesters\x18\x03 \x03(\x04\x12\x0f\n\x07timeout\x18\x04 \x02(\r\";\n\tBindWrite\x12\x0e\n\x06handle\x18\x01 \x02(\r\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x10\n\x08linkpath\x18\x03 \x01(\t\"\x97\x01\n\x0b\x41ssetStatus\x12\x0e\n\x06handle\x18\x01 \x02(\r\x12 \n\x06status\x18\x02 \x02(\x0e\x32\x10.bithorde.Status\x12!\n\x03ids\x18\x03 \x03(\x0b\x32\x14.bithorde.Identifier\x12\x0c\n\x04size\x18\x04 \x01(\x04\x12\x14\n\x0c\x61vailability\x18\x05 \x01(\r\x12\x0f\n\x07servers\x18\x06 \x03(\x04\"\xbd\x01\n\x04Read\x1aW\n\x07Request\x12\r\n\x05reqId\x18\x01 \x02(\r\x12\x0e\n\x06handle\x18\x02 \x02(\r\x12\x0e\n\x06offset\x18\x03 \x02(\x04\x12\x0c\n\x04size\x18\x04 \x02(\r\x12\x0f\n\x07timeout\x18\x05 \x02(\r\x1a\\\n\x08Response\x12\r\n\x05reqId\x18\x01 \x02(\r\x12 \n\x06status\x18\x02 \x02(\x0e\x32\x10.bithorde.Status\x12\x0e\n\x06offset\x18\x03 \x01(\x04\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\x0c\">\n\x0b\x44\x61taSegment\x12\x0e\n\x06handle\x18\x01 \x02(\r\x12\x0e\n\x06offset\x18\x02 \x02(\x04\x12\x0f\n\x07\x63ontent\x18\x03 \x02(\x0c\"\x17\n\x04Ping\x12\x0f\n\x07timeout\x18\x01 \x01(\r\"\xfb\x02\n\x06Stream\x12&\n\thandshake\x18\x01 \x02(\x0b\x32\x13.bithorde.HandShake\x12$\n\x08\x62indRead\x18\x02 \x03(\x0b\x32\x12.bithorde.BindRead\x12*\n\x0b\x61ssetStatus\x18\x03 \x03(\x0b\x32\x15.bithorde.AssetStatus\x12\'\n\x07readReq\x18\x05 \x03(\x0b\x32\x16.bithorde.Read.Request\x12(\n\x07readRes\x18\x06 \x03(\x0b\x32\x17.bithorde.Read.Response\x12&\n\tbindWrite\x18\x07 \x03(\x0b\x32\x13.bithorde.BindWrite\x12&\n\x07\x64\x61taSeg\x18\x08 \x03(\x0b\x32\x15.bithorde.DataSegment\x12\x36\n\x10handShakeConfirm\x18\t \x03(\x0b\x32\x1c.bithorde.HandShakeConfirmed\x12\x1c\n\x04ping\x18\n \x03(\x0b\x32\x0e.bithorde.Ping*:\n\x08HashType\x12\x08\n\x04SHA1\x10\x01\x12\n\n\x06SHA256\x10\x02\x12\x0e\n\nTREE_TIGER\x10\x03\x12\x08\n\x04\x45\x44\x32K\x10\x04*:\n\nCipherType\x12\r\n\tCLEARTEXT\x10\x00\x12\x07\n\x03XOR\x10\x01\x12\x07\n\x03RC4\x10\x02\x12\x0b\n\x07\x41\x45S_CTR\x10\x03*\x8c\x01\n\x06Status\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0c\n\x08NOTFOUND\x10\x02\x12\x12\n\x0eINVALID_HANDLE\x10\x03\x12\x0e\n\nWOULD_LOOP\x10\x04\x12\x10\n\x0c\x44ISCONNECTED\x10\x05\x12\x0b\n\x07TIMEOUT\x10\x06\x12\x0f\n\x0bNORESOURCES\x10\x07\x12\t\n\x05\x45RROR\x10\x08')

_HASHTYPE = descriptor.EnumDescriptor(
  name='HashType',
  full_name='bithorde.HashType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='SHA1', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SHA256', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TREE_TIGER', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ED2K', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1239,
  serialized_end=1297,
)


_CIPHERTYPE = descriptor.EnumDescriptor(
  name='CipherType',
  full_name='bithorde.CipherType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CLEARTEXT', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='XOR', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RC4', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='AES_CTR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1299,
  serialized_end=1357,
)


_STATUS = descriptor.EnumDescriptor(
  name='Status',
  full_name='bithorde.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='NOTFOUND', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='INVALID_HANDLE', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='WOULD_LOOP', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DISCONNECTED', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='NORESOURCES', index=7, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERROR', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1360,
  serialized_end=1500,
)


SHA1 = 1
SHA256 = 2
TREE_TIGER = 3
ED2K = 4
CLEARTEXT = 0
XOR = 1
RC4 = 2
AES_CTR = 3
NONE = 0
SUCCESS = 1
NOTFOUND = 2
INVALID_HANDLE = 3
WOULD_LOOP = 4
DISCONNECTED = 5
TIMEOUT = 6
NORESOURCES = 7
ERROR = 8



_IDENTIFIER = descriptor.Descriptor(
  name='Identifier',
  full_name='bithorde.Identifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='bithorde.Identifier.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='bithorde.Identifier.id', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=28,
  serialized_end=86,
)


_HANDSHAKE = descriptor.Descriptor(
  name='HandShake',
  full_name='bithorde.HandShake',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='bithorde.HandShake.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='protoversion', full_name='bithorde.HandShake.protoversion', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='challenge', full_name='bithorde.HandShake.challenge', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=88,
  serialized_end=157,
)


_HANDSHAKECONFIRMED = descriptor.Descriptor(
  name='HandShakeConfirmed',
  full_name='bithorde.HandShakeConfirmed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cipher', full_name='bithorde.HandShakeConfirmed.cipher', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cipheriv', full_name='bithorde.HandShakeConfirmed.cipheriv', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='authentication', full_name='bithorde.HandShakeConfirmed.authentication', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=159,
  serialized_end=259,
)


_BINDREAD = descriptor.Descriptor(
  name='BindRead',
  full_name='bithorde.BindRead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='handle', full_name='bithorde.BindRead.handle', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ids', full_name='bithorde.BindRead.ids', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requesters', full_name='bithorde.BindRead.requesters', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeout', full_name='bithorde.BindRead.timeout', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=261,
  serialized_end=359,
)


_BINDWRITE = descriptor.Descriptor(
  name='BindWrite',
  full_name='bithorde.BindWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='handle', full_name='bithorde.BindWrite.handle', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='bithorde.BindWrite.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='linkpath', full_name='bithorde.BindWrite.linkpath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=361,
  serialized_end=420,
)


_ASSETSTATUS = descriptor.Descriptor(
  name='AssetStatus',
  full_name='bithorde.AssetStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='handle', full_name='bithorde.AssetStatus.handle', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='bithorde.AssetStatus.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ids', full_name='bithorde.AssetStatus.ids', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='bithorde.AssetStatus.size', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='availability', full_name='bithorde.AssetStatus.availability', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='servers', full_name='bithorde.AssetStatus.servers', index=5,
      number=6, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=423,
  serialized_end=574,
)


_READ_REQUEST = descriptor.Descriptor(
  name='Request',
  full_name='bithorde.Read.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reqId', full_name='bithorde.Read.Request.reqId', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='handle', full_name='bithorde.Read.Request.handle', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='bithorde.Read.Request.offset', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='bithorde.Read.Request.size', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeout', full_name='bithorde.Read.Request.timeout', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=585,
  serialized_end=672,
)

_READ_RESPONSE = descriptor.Descriptor(
  name='Response',
  full_name='bithorde.Read.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reqId', full_name='bithorde.Read.Response.reqId', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='bithorde.Read.Response.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='bithorde.Read.Response.offset', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='bithorde.Read.Response.content', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=674,
  serialized_end=766,
)

_READ = descriptor.Descriptor(
  name='Read',
  full_name='bithorde.Read',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_READ_REQUEST, _READ_RESPONSE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=577,
  serialized_end=766,
)


_DATASEGMENT = descriptor.Descriptor(
  name='DataSegment',
  full_name='bithorde.DataSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='handle', full_name='bithorde.DataSegment.handle', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='bithorde.DataSegment.offset', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='content', full_name='bithorde.DataSegment.content', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=768,
  serialized_end=830,
)


_PING = descriptor.Descriptor(
  name='Ping',
  full_name='bithorde.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='timeout', full_name='bithorde.Ping.timeout', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=832,
  serialized_end=855,
)


_STREAM = descriptor.Descriptor(
  name='Stream',
  full_name='bithorde.Stream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='handshake', full_name='bithorde.Stream.handshake', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bindRead', full_name='bithorde.Stream.bindRead', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='assetStatus', full_name='bithorde.Stream.assetStatus', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='readReq', full_name='bithorde.Stream.readReq', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='readRes', full_name='bithorde.Stream.readRes', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bindWrite', full_name='bithorde.Stream.bindWrite', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dataSeg', full_name='bithorde.Stream.dataSeg', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='handShakeConfirm', full_name='bithorde.Stream.handShakeConfirm', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ping', full_name='bithorde.Stream.ping', index=8,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=858,
  serialized_end=1237,
)

_IDENTIFIER.fields_by_name['type'].enum_type = _HASHTYPE
_HANDSHAKECONFIRMED.fields_by_name['cipher'].enum_type = _CIPHERTYPE
_BINDREAD.fields_by_name['ids'].message_type = _IDENTIFIER
_ASSETSTATUS.fields_by_name['status'].enum_type = _STATUS
_ASSETSTATUS.fields_by_name['ids'].message_type = _IDENTIFIER
_READ_REQUEST.containing_type = _READ;
_READ_RESPONSE.fields_by_name['status'].enum_type = _STATUS
_READ_RESPONSE.containing_type = _READ;
_STREAM.fields_by_name['handshake'].message_type = _HANDSHAKE
_STREAM.fields_by_name['bindRead'].message_type = _BINDREAD
_STREAM.fields_by_name['assetStatus'].message_type = _ASSETSTATUS
_STREAM.fields_by_name['readReq'].message_type = _READ_REQUEST
_STREAM.fields_by_name['readRes'].message_type = _READ_RESPONSE
_STREAM.fields_by_name['bindWrite'].message_type = _BINDWRITE
_STREAM.fields_by_name['dataSeg'].message_type = _DATASEGMENT
_STREAM.fields_by_name['handShakeConfirm'].message_type = _HANDSHAKECONFIRMED
_STREAM.fields_by_name['ping'].message_type = _PING
DESCRIPTOR.message_types_by_name['Identifier'] = _IDENTIFIER
DESCRIPTOR.message_types_by_name['HandShake'] = _HANDSHAKE
DESCRIPTOR.message_types_by_name['HandShakeConfirmed'] = _HANDSHAKECONFIRMED
DESCRIPTOR.message_types_by_name['BindRead'] = _BINDREAD
DESCRIPTOR.message_types_by_name['BindWrite'] = _BINDWRITE
DESCRIPTOR.message_types_by_name['AssetStatus'] = _ASSETSTATUS
DESCRIPTOR.message_types_by_name['Read'] = _READ
DESCRIPTOR.message_types_by_name['DataSegment'] = _DATASEGMENT
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Stream'] = _STREAM

class Identifier(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IDENTIFIER
  
  # @@protoc_insertion_point(class_scope:bithorde.Identifier)

class HandShake(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANDSHAKE
  
  # @@protoc_insertion_point(class_scope:bithorde.HandShake)

class HandShakeConfirmed(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HANDSHAKECONFIRMED
  
  # @@protoc_insertion_point(class_scope:bithorde.HandShakeConfirmed)

class BindRead(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BINDREAD
  
  # @@protoc_insertion_point(class_scope:bithorde.BindRead)

class BindWrite(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BINDWRITE
  
  # @@protoc_insertion_point(class_scope:bithorde.BindWrite)

class AssetStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ASSETSTATUS
  
  # @@protoc_insertion_point(class_scope:bithorde.AssetStatus)

class Read(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Request(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _READ_REQUEST
    
    # @@protoc_insertion_point(class_scope:bithorde.Read.Request)
  
  class Response(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _READ_RESPONSE
    
    # @@protoc_insertion_point(class_scope:bithorde.Read.Response)
  DESCRIPTOR = _READ
  
  # @@protoc_insertion_point(class_scope:bithorde.Read)

class DataSegment(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATASEGMENT
  
  # @@protoc_insertion_point(class_scope:bithorde.DataSegment)

class Ping(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PING
  
  # @@protoc_insertion_point(class_scope:bithorde.Ping)

class Stream(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STREAM
  
  # @@protoc_insertion_point(class_scope:bithorde.Stream)

# @@protoc_insertion_point(module_scope)
