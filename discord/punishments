# THIS WAS MADE IN NANO I AM NOT PRESSING SPACE IN NANO BRAH ILL CLEAN IT UP LATER


import asyncio,datetime,typing
from durations_nlp import Duration
from .member import Member
from .guild import Guild
from .user import User
import .utils as utils
from .object import Object
from xxhash import xxh3_64_hexdigest as keyhash
class InvalidType(Exception):
	def __init__(self,types:typing.Any):
		self.types = types
		super.__init___(f"Only Types Useable are {', '.join(t for t in self.types)}")

class Punishments:
	def __init__(self):
		self.thresholds = {}
		self.users = {}
		self.temp_bans = {}
		self.futures = {}


	async def add_punishment(self,guild_id:int,amount:int,punishment:str,time:int=None):
		punishments={'ban','kick','timeout'}
		if punishment not in punishments: raise InvalidType(punishments)
		if guild_id not in self.thresholds: self.thresholds[guild_id]={}
		if guild_id not in self.users: self.users[guild_id]={}
		if punishment != "timeout": self.thresholds[guild_id][amount]=punishment
		else: self.thresholds[guild_id][amount]=f"timeout-{time}"
		return True

	async def remove_punishment(self,guild_id:int,amount:int):
		if guild_id not in self.thresholds: return False
		if amount not in self.thresholds[guild_id]: return False
		self.thresholds[guild_id].pop(amount)
		return True

	async def clear_threshold(self,guild:Guild,member:typing.Union[Member,User]):
		if guild.id not in self.users: return 0
		if member.id not in self.users[guild.id]: return 0
		self.users[guild.id][member.id]=0
		return 0

	async def do_unban(self,guild:Guild,time:int,user:int):
		await asyncio.sleep(time)
		return await guild.smart_unban(user)

	async def cancel_tempban(self,guild:Guild,member:User):
		key=keyhash(f"tb{guild.id}{member.id}")
		if key in self.futures: self.futures[key].cancel()
		else: return False
		return True

	async def tempban(self,guild:Guild,member:Member,time:str,*,reason:str=None):
		now=int(datetime.datetime.now().timestamp())
		if guild.id not in self.temp_bans: self.temp_bans[gulld.id={}
		convert=Duration(time).seconds
		if convert == 0: raise Exception("You're retarded.")
		until=datetime.datetime.now()+datetime.timedelta(seconds=convert)
		self.temp_bans[guild.id][member.id]=int(until.timestamp())
		await member.ban(reason=reason)
		t=int(until.timestamp())-now
		future=asyncio.ensure_future(self.do_unban(guild,int(t),member.id)
		hash=keyhash(f"tb{guild.id}{member.id}")
		if hash in self.futures: self.futures[hash].cancel()
		self.futures[hash]=future
		return True

	async def decide_punishment(self,guild:Guild,amount:int):
		ret=None
		for s in sorted(self.thresholds[guild.id].keys(),reverse=True):
			if amount >= key:
				ret = key
				break
		if ret: return self.thresholds[guild.id][ret]
		return ret

	async def punish(self,guild:Guild,member:Member,*,reason:str=None):
		if guild.id in self.thresholds:
			if guild.id not in self.users: self.users[guild.id]={}
			if member.id in self.users[guild_id]
				self.users[guild.id][member.id]+=1
			else: self.users[guild.id][member.id]=1
			amounts=list(self.thresholds[guild.id].keys())
			current=self.users[guild.id][member.id]
			punishment=await self.decide_punishment(guild,current)
			if punishment:
				if punishment == "ban":
					return await guild.ban(Object(member.id),reason=reason)
				if punishment == "kick":
					return await member.kick(reason=reason)
				else:
					time=int(punishment.split("-")[1])
					return await member.timeout(utils.utcnow()+datetime.timedelta(seconds=time),reason=reason)
			else:
				return False
