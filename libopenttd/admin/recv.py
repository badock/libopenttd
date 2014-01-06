from libopenttd import packets
from .base import AdminPacket

class AdminRecvPacket(AdminPacket):
    class Meta:
        direction = packets.Direction.RECV
        abstract = True
Packet = AdminRecvPacket

class Full(Packet):
    pid = 100

class Banned(Packet):
    pid = 101

class Error(Packet):
    pid = 102
    errorcode   = packets.UInt8Field(ordering=1)

class Protocol(Packet):
    pid = 103
    version     = packets.UInt8Field(ordering=1, is_version_identifier = True)
    settings    = packets.DictField(ordering=2, key=packets.UInt16Field(ordering=1),
                                    value=packets.UInt16Field(ordering=2),
                                    is_next=packets.BooleanField(ordering=3, is_next=True))

class Welcome(Packet):
    pid = 104
    name        = packets.StringField(ordering=1)
    version     = packets.StringField(ordering=2)
    dedicated   = packets.BooleanField(ordering=3)
    map_name    = packets.StringField(ordering=4)
    seed        = packets.UInt32Field(ordering=5)
    landscape   = packets.UInt8Field(ordering=6)
    startyear   = packets.DateField(ordering=7)
    size_x      = packets.UInt16Field(ordering=8)
    size_y      = packets.UInt16Field(ordering=9)

class NewGame(Packet):
    pid = 105

class Shutdown(Packet):
    pid = 106

class Date(Packet):
    pid = 107
    date        = packets.DateField(ordering=1)

class ClientJoin(Packet):
    pid = 108
    client_id   = packets.UInt32Field(ordering=1)

class ClientInfo(Packet):
    pid = 109
    client_id   = packets.UInt32Field(ordering=1)
    hostname    = packets.StringField(ordering=2)
    name        = packets.StringField(ordering=3)
    language    = packets.UInt8Field(ordering=4)
    joindate    = packets.DateField(ordering=5)
    play_as     = packets.UInt8Field(ordering=6)

class ClientUpdate(Packet):
    pid = 110
    client_id   = packets.UInt32Field(ordering=1)
    name        = packets.StringField(ordering=2)
    play_as     = packets.UInt8Field(ordering=3)

class ClientQuit(Packet):
    pid = 111
    client_id   = packets.UInt32Field(ordering=1)

class ClientError(Packet):
    pid = 112
    client_id   = packets.UInt32Field(ordering=1)
    errorcode   = packets.UInt8Field(ordering=2)

class CompanyNew(Packet):
    pid = 113
    company_id  = packets.UInt8Field(ordering=1)

class CompanyInfo(Packet):
    pid = 114
    company_id  = packets.UInt8Field(ordering=1)
    name        = packets.StringField(ordering=2)
    manager_name = packets.StringField(ordering=3)
    colour      = packets.UInt8Field(ordering=4)
    passworded  = packets.BooleanField(ordering=5)
    startyear   = packets.UInt32Field(ordering=6)
    is_ai       = packets.BooleanField(ordering=7)
    bankrupcy_counter = packets.UInt8Field(ordering=8)
    shareholder = packets.UInt8Field(ordering=9, count=4)

class CompanyUpdate(Packet):
    pid = 115
    company_id  = packets.UInt8Field(ordering=1)
    name        = packets.StringField(ordering=2)
    manager_name = packets.StringField(ordering=3)
    colour      = packets.UInt8Field(ordering=4)
    passworded  = packets.BooleanField(ordering=5)
    bankrupcy_counter = packets.UInt8Field(ordering=8)
    shareholder = packets.UInt8Field(ordering=9, count=4)

class CompanyRemove(Packet):
    pid = 116
    company_id  = packets.UInt8Field(ordering=1)
    reason      = packets.UInt8Field(ordering=2)

class CompanyEconomy(Packet):
    pid = 117
    company_id  = packets.UInt8Field(ordering=1)
    money       = packets.Int64Field(ordering=2)
    current_loan = packets.Int64Field(ordering=3)
    income      = packets.Int64Field(ordering=4)
    delivered   = packets.UInt16Field(ordering=5)
    history     = packets.RepeatingField(ordering=6, count=2, fields = {
        'value':        packets.Int64Field(ordering=1),
        'performance':  packets.UInt16Field(ordering=2),
        'delivered':    packets.UInt16Field(ordering=3),
        })

class CompanyStats(Packet):
    pid = 118
    company_id  = packets.UInt8Field(ordering=1)
    vehicles    = packets.GroupedField(ordering=2, fields = {
        'train':    packets.UInt16Field(ordering=1),
        'lorry':    packets.UInt16Field(ordering=2),
        'bus':      packets.UInt16Field(ordering=3),
        'plane':    packets.UInt16Field(ordering=4),
        'ship':     packets.UInt16Field(ordering=5),
        })
    stations    = packets.GroupedField(ordering=3, fields = {
        'train':    packets.UInt16Field(ordering=1),
        'lorry':    packets.UInt16Field(ordering=2),
        'bus':      packets.UInt16Field(ordering=3),
        'plane':    packets.UInt16Field(ordering=4),
        'ship':     packets.UInt16Field(ordering=5),
        })

class Chat(Packet):
    pid = 119
    action      = packets.UInt8Field(ordering=1)
    dest_type   = packets.UInt8Field(ordering=2)
    client_id   = packets.UInt32Field(ordering=3)
    message     = packets.StringField(ordering=4)
    data        = packets.UInt64Field(ordering=5)

class Rcon(Packet):
    pid = 120
    colour      = packets.UInt16Field(ordering=1)
    result      = packets.StringField(ordering=2)

class Console(Packet):
    pid = 121
    origin      = packets.StringField(ordering=1)
    message     = packets.StringField(ordering=2)

class CmdNames(Packet):
    pid = 122
    commands    = packets.DictField(ordering=1, key=packets.UInt16Field(ordering=1),
                                    value=packets.StringField(ordering=2),
                                    is_next=packets.BooleanField(ordering=3, is_next=True))

class CmdLogging(Packet):
    pid = 123
    client_id   = packets.UInt32Field(ordering=1)
    company_id  = packets.UInt8Field(ordering=2)
    command_id  = packets.UInt16Field(ordering=3)
    params      = packets.UInt32Field(ordering=4, count=2)
    tile        = packets.UInt32Field(ordering=5)
    text        = packets.StringField(ordering=6)
    frame       = packets.UInt32Field(ordering=7)

class Gamescript(Packet):
    pid = 124
    data        = packets.JsonField(ordering=1)

class RconEnd(Packet):
    pid = 125
    command     = packets.StringField(ordering=1)

class Pong(Packet):
    pid = 126
    payload     = packets.UInt32Field(ordering=1)
