import psutil, random, aiohttp, socket, orjson
from typing import Optional

class NoInterface(Exception):
    def __init__(self):
        return super().__init__(f"Please provide an interface to pull addresses from using the interface= argument")

def get_local_addresses(interface:str):
    interfaces=psutil.net_if_addrs()
    return [(str(i.address),0) for i in interfaces[interface] if '.' in i.address]

def get_all_interface_addresses():
    addresses=[]
    interfaces=psutil.net_if_addrs()
    interface_keys=list(interfaces.keys())
    for interface in interface_keys:
        for i in interfaces[interface]:
            if i.address:
                if "." in i.address and not i.address.startswith('127.') and not i.address.startswith('192'):
                    addresses.append((str(i.address),0))
    return addresses

class ProxyPool(object):
    def __init__(self,proxies:Optional[list],use_local:bool=False,interface: Optional[str]=None):
        if proxies:
            self.proxies = proxies
            self.local = False
        else:
            if use_local == True:
                self.local=True
                if not interface: self.proxies = get_all_interface_addresses()
                else: self.proxies = get_local_addresses(interface)
        self.proxies=iter(self.proxies)

    async def session(self):
        if self.local == True:
            return aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=socket.AF_INET,limit=0,local_addr=(next(self.proxies),0)),json_serialize=lambda x: orjson.dumps(x).decode(),resolver=aiohttp.AsyncResolver())
        else:
            return aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=socket.AF_INET,limit=0),proxy=next(self.proxies),resolver=aiohttp.AsyncResolver(),json_serialize=lambda x: orjson.dumps(x).decode(),)
