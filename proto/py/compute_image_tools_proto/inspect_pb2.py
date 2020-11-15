# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inspect.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='inspect.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rinspect.proto\"\xa1\x01\n\tOsRelease\x12\x15\n\rcli_formatted\x18\x01 \x01(\t\x12\x0e\n\x06\x64istro\x18\x02 \x01(\t\x12\x15\n\rmajor_version\x18\x03 \x01(\t\x12\x15\n\rminor_version\x18\x04 \x01(\t\x12#\n\x0c\x61rchitecture\x18\x05 \x01(\x0e\x32\r.Architecture\x12\x1a\n\tdistro_id\x18\x06 \x01(\x0e\x32\x07.Distro\"\x9e\x03\n\x11InspectionResults\x12\x1e\n\nos_release\x18\x01 \x01(\x0b\x32\n.OsRelease\x12\x15\n\rbios_bootable\x18\x02 \x01(\x08\x12\x15\n\ruefi_bootable\x18\x03 \x01(\x08\x12\x0f\n\x07root_fs\x18\x04 \x01(\t\x12\x30\n\nerror_when\x18\x05 \x01(\x0e\x32\x1c.InspectionResults.ErrorWhen\x12\x17\n\x0f\x65lapsed_time_ms\x18\x06 \x01(\x03\x12\x10\n\x08os_count\x18\x07 \x01(\x05\"\xcc\x01\n\tErrorWhen\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x13\n\x0fSTARTING_WORKER\x10\x64\x12\x12\n\x0eRUNNING_WORKER\x10\x65\x12\x13\n\x0eMOUNTING_GUEST\x10\xc8\x01\x12\x12\n\rINSPECTING_OS\x10\xc9\x01\x12\x1a\n\x15INSPECTING_BOOTLOADER\x10\xca\x01\x12\x1d\n\x18\x44\x45\x43ODING_WORKER_RESPONSE\x10\xac\x02\x12$\n\x1fINTERPRETING_INSPECTION_RESULTS\x10\xad\x02*\xb7\x01\n\x06\x44istro\x12\x12\n\x0e\x44ISTRO_UNKNOWN\x10\x00\x12\x0c\n\x07WINDOWS\x10\xe8\x07\x12\x0b\n\x06\x44\x45\x42IAN\x10\xd0\x0f\x12\x0b\n\x06UBUNTU\x10\xd1\x0f\x12\t\n\x04KALI\x10\xd2\x0f\x12\r\n\x08OPENSUSE\x10\xb8\x17\x12\t\n\x04SLES\x10\xb9\x17\x12\r\n\x08SLES_SAP\x10\xba\x17\x12\x0b\n\x06\x46\x45\x44ORA\x10\xa0\x1f\x12\t\n\x04RHEL\x10\xa1\x1f\x12\x0b\n\x06\x43\x45NTOS\x10\xa2\x1f\x12\x0b\n\x06\x41MAZON\x10\xa3\x1f\x12\x0b\n\x06ORACLE\x10\xa4\x1f*:\n\x0c\x41rchitecture\x12\x18\n\x14\x41RCHITECTURE_UNKNOWN\x10\x00\x12\x07\n\x03X86\x10\x01\x12\x07\n\x03X64\x10\x02\x42\x06Z\x04.;pbb\x06proto3'
)

_DISTRO = _descriptor.EnumDescriptor(
  name='Distro',
  full_name='Distro',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISTRO_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WINDOWS', index=1, number=1000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEBIAN', index=2, number=2000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UBUNTU', index=3, number=2001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KALI', index=4, number=2002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPENSUSE', index=5, number=3000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SLES', index=6, number=3001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SLES_SAP', index=7, number=3002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEDORA', index=8, number=4000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RHEL', index=9, number=4001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CENTOS', index=10, number=4002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AMAZON', index=11, number=4003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORACLE', index=12, number=4004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=599,
  serialized_end=782,
)
_sym_db.RegisterEnumDescriptor(_DISTRO)

Distro = enum_type_wrapper.EnumTypeWrapper(_DISTRO)
_ARCHITECTURE = _descriptor.EnumDescriptor(
  name='Architecture',
  full_name='Architecture',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARCHITECTURE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='X86', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='X64', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=784,
  serialized_end=842,
)
_sym_db.RegisterEnumDescriptor(_ARCHITECTURE)

Architecture = enum_type_wrapper.EnumTypeWrapper(_ARCHITECTURE)
DISTRO_UNKNOWN = 0
WINDOWS = 1000
DEBIAN = 2000
UBUNTU = 2001
KALI = 2002
OPENSUSE = 3000
SLES = 3001
SLES_SAP = 3002
FEDORA = 4000
RHEL = 4001
CENTOS = 4002
AMAZON = 4003
ORACLE = 4004
ARCHITECTURE_UNKNOWN = 0
X86 = 1
X64 = 2


_INSPECTIONRESULTS_ERRORWHEN = _descriptor.EnumDescriptor(
  name='ErrorWhen',
  full_name='InspectionResults.ErrorWhen',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STARTING_WORKER', index=1, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING_WORKER', index=2, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOUNTING_GUEST', index=3, number=200,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSPECTING_OS', index=4, number=201,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INSPECTING_BOOTLOADER', index=5, number=202,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DECODING_WORKER_RESPONSE', index=6, number=300,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERPRETING_INSPECTION_RESULTS', index=7, number=301,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=392,
  serialized_end=596,
)
_sym_db.RegisterEnumDescriptor(_INSPECTIONRESULTS_ERRORWHEN)


_OSRELEASE = _descriptor.Descriptor(
  name='OsRelease',
  full_name='OsRelease',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cli_formatted', full_name='OsRelease.cli_formatted', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distro', full_name='OsRelease.distro', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='major_version', full_name='OsRelease.major_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minor_version', full_name='OsRelease.minor_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='architecture', full_name='OsRelease.architecture', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distro_id', full_name='OsRelease.distro_id', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=179,
)


_INSPECTIONRESULTS = _descriptor.Descriptor(
  name='InspectionResults',
  full_name='InspectionResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='os_release', full_name='InspectionResults.os_release', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bios_bootable', full_name='InspectionResults.bios_bootable', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uefi_bootable', full_name='InspectionResults.uefi_bootable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root_fs', full_name='InspectionResults.root_fs', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_when', full_name='InspectionResults.error_when', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='elapsed_time_ms', full_name='InspectionResults.elapsed_time_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='os_count', full_name='InspectionResults.os_count', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INSPECTIONRESULTS_ERRORWHEN,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=596,
)

_OSRELEASE.fields_by_name['architecture'].enum_type = _ARCHITECTURE
_OSRELEASE.fields_by_name['distro_id'].enum_type = _DISTRO
_INSPECTIONRESULTS.fields_by_name['os_release'].message_type = _OSRELEASE
_INSPECTIONRESULTS.fields_by_name['error_when'].enum_type = _INSPECTIONRESULTS_ERRORWHEN
_INSPECTIONRESULTS_ERRORWHEN.containing_type = _INSPECTIONRESULTS
DESCRIPTOR.message_types_by_name['OsRelease'] = _OSRELEASE
DESCRIPTOR.message_types_by_name['InspectionResults'] = _INSPECTIONRESULTS
DESCRIPTOR.enum_types_by_name['Distro'] = _DISTRO
DESCRIPTOR.enum_types_by_name['Architecture'] = _ARCHITECTURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OsRelease = _reflection.GeneratedProtocolMessageType('OsRelease', (_message.Message,), {
  'DESCRIPTOR' : _OSRELEASE,
  '__module__' : 'inspect_pb2'
  # @@protoc_insertion_point(class_scope:OsRelease)
  })
_sym_db.RegisterMessage(OsRelease)

InspectionResults = _reflection.GeneratedProtocolMessageType('InspectionResults', (_message.Message,), {
  'DESCRIPTOR' : _INSPECTIONRESULTS,
  '__module__' : 'inspect_pb2'
  # @@protoc_insertion_point(class_scope:InspectionResults)
  })
_sym_db.RegisterMessage(InspectionResults)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
# Don't run flake8 on gnerated Python files.
# flake8: noqa