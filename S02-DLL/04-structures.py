import ctypes

from ctypes import Structure, Union
from ctypes import c_char_p, c_ushort, c_ulong, POINTER

from socket import htonl
from ipaddress import ip_address

# https://docs.microsoft.com/en-us/windows/win32/api/windns/ns-windns-dns_recorda
# https://docs.microsoft.com/en-us/windows/win32/api/windns/nf-windns-dnsquery_a
IP4_ADDRESS = c_ulong


class DNS_MX_DATAA(Structure):
    _fields_ = [
        ("pNameExchange", c_char_p),
        ("wPreference", c_ushort),
        ("Pad", c_ushort),
    ]
PDNS_MX_DATAA = POINTER(DNS_MX_DATAA)


class DNS_A_DATA(Structure):
    _fields_ = [
        ("IpAddress", IP4_ADDRESS),
    ]
PDNS_A_DATA = POINTER(DNS_A_DATA)


class DnsData(Union):
    _fields_ = [
        ("A", DNS_A_DATA),
        ("MX", DNS_MX_DATAA),
    ]


class DNS_RECORDA(Structure):
    pass

PDNS_RECORDA = POINTER(DNS_RECORDA)
DNS_RECORDA._fields_ = [
    ("pNext", PDNS_RECORDA),
    ("pName", c_char_p),
    ("wType", c_ushort),
    ("wDataLength", c_ushort),
    ("Flags", c_ushort),
    ("dwTtl", c_ulong),
    ("dwReserved", c_ulong),
    ("Data", DnsData),
]


def print_dns_records(p: PDNS_RECORDA):
    dns_types = {
        0x0001: 'A',
        0x000f: 'MX',
    }
    while bool(p):
        record = p.contents
        pName = record.pName.decode()
        ttl = record.dwTtl
        wType = dns_types.get(record.wType, f'UNKNOWN({hex(record.wType)})')

        if wType == 'A':
            address = ip_address(htonl(record.Data.A.IpAddress))
        elif wType == 'MX':
            address = record.Data.MX.pNameExchange
        else:
            address = '-'
        print(f'{pName}    {ttl}    {wType}    {address}')

        p = record.pNext
        

DnsQuery_A = ctypes.windll.dnsapi.DnsQuery_A
DnsRecordListFree = ctypes.windll.dnsapi.DnsFree


results = PDNS_RECORDA()
ret = DnsQuery_A(
    b'baidu.com.',
    0x01, # A Data
    0x0, # DNS_QUERY_STANDARD
    None,
    ctypes.byref(results),
    None
)
print(f'{ret=}, {results=}')
print_dns_records(results)
DnsRecordListFree(results, 1)
print()

ret = DnsQuery_A(
    b'baidu.com.',
    0x0f, # MX Data
    0x0, # DNS_QUERY_STANDARD
    None,
    ctypes.byref(results),
    None
)
print(f'{ret=}, {results=}')
print_dns_records(results)
DnsRecordListFree(results, 1)
print()

ret = DnsQuery_A(
    b'baidu.com.',
    0x02, # NS Data
    0x0, # DNS_QUERY_STANDARD
    None,
    ctypes.byref(results),
    None
)
print(f'{ret=}, {results=}')
print_dns_records(results)
DnsRecordListFree(results, 1)
print()
