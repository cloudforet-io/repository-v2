from google.protobuf.empty_pb2 import Empty
from spaceone.core.pygrpc.message_type import *


def EmptyInfo():
    return Empty()


def StatisticsInfo(result):
    return change_struct_type(result)


def AnalyzeInfo(result):
    return change_struct_type(result)