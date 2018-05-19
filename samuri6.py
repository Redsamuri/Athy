# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia, goslate
import timeit
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

import six

if (six.PY2):
    import urllib2
    import urllib
else:
    import urllib.request
    import urllib.parse

cl = LINETCR.LINE()
cl.login(token="")
cl.loginResult()

    
print "=====[Login Success]====="
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""╔═════════════════
╠   Selft Command
╠➩〘$,Me〙
╠➩〘เปลี่ยนชื่อ: 〙
╠➩〘เปลี่ยนตัส: 〙
╠➩〘ชื่อ〙
╠➩〘ตัส〙
╠➩〘รูปโปร〙
╠➩〘รูปปก〙
╠➩〘เช็คบอท〙
╠➩〘Sp/Speed〙
╠➩〘แนะนำตัว〙
╠➩〘ไอดี @〙
╠➩〘รูปโปร @〙
╠➩〘คท @〙
╠➩〘ข้อมูล @〙
╠➩〘ชื่อ @〙
╠➩〘ตัส @〙
╠➩〘รูปโปร @〙
╠➩〘รูปปก @〙
╠➩〘ใครแทค/แจ๊ะ〙
╠➩〘เปิด/ปิดสแกน〙
╠➩〘จับ/อ่าน〙
╠➩〘หวด @〙
╠➩〘ปลิว:〙
╠➩〘เช็ค:〙
╠➩〘Bot on/off〙
╠➩〘จับ〙
╠➩〘อ่าน〙
╠➩〘กันรัน〙
╠➩〘ลบรัน〙
╠➩〘ลบแชท〙
╠➩〘Mimic on/off〙
╠➩〘Micadd @〙
╠➩〘Micdel @〙
╠ 
╠    〘Help1-3〙
╚════════════════════════════════
"""

helpset ="""╔═════════════════
╠   Setting Command
╠➩〘My simisimi on/off〙
╠➩〘เปิด/ปิดกัน〙
╠➩〘เปิด/ปิดกันลิ้ง〙
╠➩〘เปิด/ปิดกันเชิญ〙
╠➩〘เปิด/ปิดกันยก〙
╠➩〘เปิด/ปิดแทคเจ็บ〙
╠➩〘เปิด/ปิดคท〙
╠➩〘เปิด/ปิดเข้า〙
╠➩〘เปิด/ปิดออก〙
╠➩〘เปิด/ปิดแอด〙
╠➩〘Like me〙
╠➩〘Like friend〙
╠➩〘เปิด/ปิดไลค์〙
╠➩〘เปิด/ปิดเม้น〙
╠➩〘เปิด/ปิดแทค〙
╠➩〘เปิด/ปิดอ่าน〙
╠➩〘เปิด/ปิดแทครูป〙
╠➩〘รับแขก On/off〙
╠➩〘ส่งแขก On/off〙
╠➩〘ใครเตะ On/off〙
╠➩〘เปิด/ปิดแสกน〙
╠➩〘เปิด/ปิดSambutan〙
╚═════════════════
"""

helpgrup ="""╔═════════════════
╠   Group Command
╠➩〘เปิด/ปิดลิ้ง〙
╠➩〘ลอคชื่อ/ปิดลอค〙
╠➩〘ลิ้ง〙
╠➩〘แซว〙
╠➩〘แอด〙
╠➩〘แอด.ทั้งห้อง〙
╠➩〘รายชื่อสมาชิก〙
╠➩〘หวด @〙
╠➩〘ทดสอบ @〙
╠➩〘ข้อมูล @〙
╠➩〘เปลี่ยนชื่อกลุ่ม: 〙
╠➩〘ข้อมูลกลุ่ม〙
╠➩〘รูปกลุ่ม〙
╠➩〘ลิ้งรูปกลุ่ม〙
╠➩〘ไอดีกลุ่ม〙
╠➩〘รายชื่อกลุ่ม〙
╠➩〘รายชื่อเพื่อน〙
╠➩〘บัญชีดำ〙
╠➩〘แบน @〙
╠➩〘ล้างแบน @〙
╠➩〘เครีย์แบน〙
╠➩〘เช็คดำ〙
╠➩〘เช็คบล็อค〙
╠➩〘คทแบน〙
╠➩〘ไอดีแบน〙
╠➩〘#BanAll〙
╠➩〘#UnbanAll〙
╚═════════════════
"""

helpmed ="""╔═════════════════
╠   Social Media Command
╠➩〘ปฏิทิน〙
╠➩〘อู้-Id〙
╠➩〘อู้-En〙
╠➩〘อู้-Jp〙
╠➩〘อู้-Ko〙
╠➩〘th-id〙
╠➩〘th-en〙
╠➩〘th-jp〙
╠➩〘th-ko〙
╠➩〘th@id〙
╠➩〘th@en〙
╠➩〘th@jp〙
╠➩〘th@ko〙
╠➩〘th@ar〙
╠➩〘say-id〙
╠➩〘say-en〙
╠➩〘say-jp〙
╠➩〘say-ko〙
╠➩〘say-Th〙
╠➩〘S.ay (ข้อความ)〙
╠➩〘ไอ.จี (ชื่อยูส)〙
╠➩〘เฟส.บุค〙
╠➩〘ส่อง.เฟส (ชื่อเฟส) 〙
╠➩〘wiki.pedia (ข้อความ)〙
╠➩〘Twit.ter (ชนิดหรือชื่อทวิท)〙
╠➩〘sm.ule (ข้อความ)〙
╠➩〘gi.thub (ข้อความ)〙 
╠➩〘วี.ดีโอ (ชื่อวีดี.โอ)〙
╠➩〘เพล.สโต (ชื่อแอพ)〙
╠➩〘รู.ป (ชื่อรูป)〙
╠➩〘กู.เกิ้ล (ข้อความ)〙
╠➩〘ยู.ทูป (ข้อความ)〙
╚═════════════════
"""
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []

KAC = [cl]
mid = cl.getProfile().mid
Bots = [mid]
admin = [mid]
Creator = [mid]

wait = {
    "likeOn":False,
    "alwayRead":False,
    "detectMention":True,
    'Tagvirus':False,
    "kickMention":False,
    "steal":False,
    'stiker':False,
    "gift":False,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":50},
    'BotCancel':True,
    "AutoJoinCancel":True,
    "memberscancel":10,
    "Members":1,
    'leaveRoom':False,
    "Selfbot":False,
    'timeline':True,
    'autoAdd':False,
    'autoBlock':True,
    'AutoKick':True,
    'message':"""🌾(●´з`)♡🌹แอดมาทำไมคับ 🌸แอดมาจีบรึแอดมารัน🌹(´ε｀ )♡🌾""",
    "lang":"JP",
    "comment":"""
                                      🌟
                                 🚩🔱🚩
                       👍AutoLike by👍
             🌾RED BOT LINE THAILAND🌾
               ─┅═✥👊ᵀᴴᴬᴵᴸᴬᴺᴰ👊✥═┅─ 
      🎎  💀[RED SAMURI SELFBOT]💀  🎎
╔══╗────────╔╗────────────────
║═╦╝╔═╗─╔══╗╠╣╔╗─╔╦╗ ╔══╗─╔╦╗
║╔╝─║╬╚╗║║║║║║║╚╗║║║ ║║║║   ║║║
╚╝──╚══╝╚╩╩╝╚╝╚═╝╠╗║ ╚╩╩╝   ╠╗║
─────────────────╚═╝───── ╚═╝──""",
    "commentOn":False,
    "commentBlack":{},
    "comment1":"""
▄▄▄RED SAMURI SELFBØT▄▄▄
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█ 🌾RED BOT LINE THAILAND🌾
█   ─┅═✥👊ᵀᴴᴬᴵᴸᴬᴺᴰ👊✥═┅─
█   💀 [ RED SAMURI BOT] 💀
█   💀💀💀💀💀💀💀💀💀
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ """,
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"─═ই꫞ஆัঐ௫နιшิa७꫞ ‮࿐)",
    "cNames":" ─┅͜͡✥ه﷽ Red﷽ه✥͜͡",
    "winvite":False,
    "Sambutan":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "pname":False,
    "pname":{},
    "pro_name":{},
    "Sider":{},
    "Backup":{},
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "BlGroup":{}
}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

save1 = {
    "Saved":False,
    "displayName":"",
    "statusMessage":"",
    "pictureStatus":""
}

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage                        
backup.pictureStatus = contact.pictureStatus

contact = cl.getContact(mid)
profile = cl.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d ชั่วโมง %02d นาที %02d วินาที ' % (hours, mins, secs) 
    
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download audio failure.')

        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise (e)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nรู้นะว่าอ่านอยู่. . .\nออกมาคุยเดี๋ยวนี้ (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
                                    else:
                                        cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nนี่ก็อีกคน. . .อ่านอย่างเดียวเลย\nไม่ออกมาคุยล่ะ (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
                                else:
                                    cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nแอบกันจังเลยนะ???\nคิดว่าเป็นนินจารึไง...??😆😆   ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                    c.contentMetadata={'mid':op.param2}
                                    cl.sendMessage(c)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            cl.leaveRoom(op.param1)

        if op.type == 21:
            cl.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"Maaf " + cl.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        cl.leaveGroup(op.param1)                        
		    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               cl.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    cl.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        cl.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                cl.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
            if wait["Sambutan"] == True:
                if op.param2 in Creator:
                    return
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                cl.sendText(op.param1,"สวัสดี " + cl.getContact(op.param2).displayName + "\nยินดีต้อนรับเข้าสู่กลุ่ม ☞ " + str(ginfo.name) + " ☜" + "\nเข้ามาแล้วอย่าลืมดูที่โน๊ตกลุ่มด้วยนะ\nอย่าลืมปิดเสียงแจ้งเตือนด้วยล่ะ ^_^")
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':op.param2}
                cl.sendMessage(c)  
                cl.sendImageWithURL(op.param1,image)
                d = Message(to=op.param1, from_=None, text=None, contentType=7)
                d.contentMetadata={
                                        "STKID": "410",
                                         "STKPKGID": "1",
                                         "STKVER": "100" }                
                cl.sendMessage(d)
                jawaban1 = ("มาใหม่แก้ผ้าด้วยเด้อ อิ๊ขึอิ๊ขึ ฮิฮิฮิ")
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')             
                print "MEMBER JOIN TO GROUP"
            
        if op.type == 19:
            if wait["Sambutan"] == True:
                if op.param2 in Creator:
                    return
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + " มึงแกล้งน้องเค้าอีกแระบักปอบ")
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':op.param2}
                cl.sendMessage(c)  
                cl.sendImageWithURL(op.param1,image)
                d = Message(to=op.param1, from_=None, text=None, contentType=7)
                d.contentMetadata={
                                        "STKID": "518",
                                         "STKPKGID": "2",
                                         "STKVER": "100" }                
                cl.sendMessage(d)
                jawaban1 = ("คือหยังมั่นโหดแท๊วะ")
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
                print "MEMBER KICK OUT FORM GROUP"

        if op.type == 15:
            if wait["Sambutan"] == True:
                if op.param2 in Creator:
                    return
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                cl.sendText(op.param1,"Goodbye.. " + cl.getContact(op.param2).displayName +  "\nแล้วเจอกันใหม่นะ. . . (p′︵‵。) 🤗")
                c = Message(to=op.param1, from_=None, text=None, contentType=13)
                c.contentMetadata={'mid':op.param2}
                cl.sendMessage(c)  
                cl.sendImageWithURL(op.param1,image)
                d = Message(to=op.param1, from_=None, text=None, contentType=7)
                d.contentMetadata={
                                        "STKID": "428",
                                        "STKPKGID": "1",
                                        "STKVER": "100" }                
                cl.sendMessage(d)
                jawaban1 = ("ฟั้งไปใสน้อ...บัดนี่")
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')                  
                print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 25:
            msg = op.message
            
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to,data['result']['response'].encode('utf-8'))

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
	        if mid in op.param3:
                 wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
                cl.comment(url[25:58], url[66:], wait["comment"])
        if op.type == 26:
            msg = op.message
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
                cl.comment(url[25:58], url[66:], wait["comment"])
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                               cl.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         cl.findAndAddContactsByMid(invite)
                                         cl.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break

        if op.type == 25:
            msg = op.message

            if msg.text in ["Bot on"]:
                wait["Selfbot"] = True
                cl.sendText(msg.to,"Selfbot Sudah On Kembali.")

        if op.type == 25:
          if wait["Selfbot"] == True:
            msg = op.message

        if op.type in [26,25]:
            msg = op.message
            if msg.contentType == 7:
                if wait['stiker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "[Stiker Check] \nSTKID : %s\nSTKPKGID : %s \nSTKVER : %s\n =>> Link...\nline://shopdetail/%s"%(stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass

        if op.type == 26:
            msg = op.message
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['Tagvirus'] == True:
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in mid:
                                  msg.contentType = 13
                                  msg.contentMetadata = {'mid': "JANDA'"}
                                  cl.sendMessage(msg)
                                  break
            
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["ว่าไงคับน้องสาว? " + cName + "มีอะไรให้ผมรับใช้คับ😂😂",cName + " แทคทำไมมิทราบ? มีอิโรยก๊ะว่ามา",cName + " แทคบ่อยๆเดะจับทำเมียนะ -..-","หยุดแทคสักพัก" + cName + " แล้วมาพบรักที่หลังแชท😝😝","😎😎😎\nคับ มีไรคับ " + cName, "ยังไม่ว่าง เดี๋ยวมาตอบนะ " + cName, "ไม่อยู่ ไปทำธุระ " + cName + "มีไรทิ้งแชทไว้ที่แชท.สตนะ?", "อ่ะ เอาอีกแระ " + cName + "แทคตมอย??????????????????","ป๊าาาด " + cName + " คุณนายคับ จะแทคทำไมคับ!"]
                    balas1 = "รูปภาพคนแทค. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,balas1)
                                  cl.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "410",
                                                       "STKPKGID": "1",
                                                       "STKVER": "100" }
                                  cl.sendMessage(msg)
                                  jawaban1 = ("By Redsamuri Selfbot")
                                  tts = gTTS(text=jawaban1, lang='en')
                                  tts.save('tts.mp3')
                                  cl.sendAudio(msg.to,'tts.mp3')                               
                                  break
                                  
            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                cl.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break
                                     
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"ชื่อ :\n" + contact.displayName + "\n\nไอดี :\n" + msg.contentMetadata["mid"] + "\n\nสเตตัส :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"รูปโปรไฟล " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"รูปปก " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "ลิ้งโพส URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpmsg)
                else:
                    cl.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'help3':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpgrup)
                else:
                    cl.sendText(msg.to,helpgrup)
            elif msg.text.lower() == 'help2':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpset)
                else:
                    cl.sendText(msg.to,helpset)
            elif msg.text.lower() == 'help1':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpmed)
                else:
                    cl.sendText(msg.to,helpmed)
            elif msg.text.lower() == 'speed':
                cl.sendText(msg.to, "「Speed My SelfBot」")
                start = time.time()
                time.sleep(0.07)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "☞「 ความเร็วของเซลบอท 」\n☞ Type: Speed\n☞ Speed : %sseconds" % (elapsed_time))
            elif msg.text.lower() == 'sp':
                cl.sendText(msg.to, "「Speed My SelfBot」")
                start = time.time()
                time.sleep(0.07)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "☞「 ความเร็วของเซลบอท 」\n☞ Type: Speed\n☞ Speed : %sseconds" % (elapsed_time))
            elif msg.text.lower() == 'crash':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u350cc7408cc6cc82e056ee046131f925',"}
                cl.sendMessage(msg)
            elif msg.text.lower() == '$':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                contact = cl.getContact(msg.contentMetadata["mid"])
                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                jawaban1 = ("สวัสดีชาวโลก")
                cl.sendMessage(msg)
                cl.sendText(msg.to,contact.displayName)
                cl.sendText(msg.to,contact.statusMessage)
                cl.sendText(msg.to,mid)
                cl.sendImageWithURL(msg.to,image)
                cl.sendImageWithURL(msg.to,path)
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')             
                msg.contentType = 7   
                msg.text = None
                msg.contentMetadata = {
                                      "STKID": "48178",
                                      "STKPKGID": "2000000",
                                      "STKVER": "100" }
                cl.sendMessage(msg)
                cl.sendText(msg.to,"SELFBOT BY: " + "\n"  + str(wait["comment1"])) 
                
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                contact = cl.getContact(msg.contentMetadata["mid"])
                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                jawaban1 = ("만나서 반가워요.")
                cl.sendMessage(msg)
                cl.sendText(msg.to,contact.displayName)
                cl.sendText(msg.to,contact.statusMessage)
                cl.sendText(msg.to,mid)
                cl.sendImageWithURL(msg.to,image)
                cl.sendImageWithURL(msg.to,path)
                tts = gTTS(text=jawaban1, lang='ko')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
                msg.contentType = 7   
                msg.text = None
                msg.contentMetadata = {
                                      "STKID": "153585",
                                      "STKPKGID": "2000007",
                                      "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendText(msg.to,"SELFBOT BY: " + "\n" + str(wait["comment1"]))
#========================== B O T ``C O M M A N D =============================#
#==============================================================================#
            elif msg.text.lower() == 'เปิดคท':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to on")
                    else:
                        cl.sendText(msg.to,"contact already on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to on")
                    else:
                        cl.sendText(msg.to,"contact already on")
            elif msg.text.lower() == 'ปิดคท':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to off")
                    else:
                        cl.sendText(msg.to,"contact already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to off")
                    else:
                        cl.sendText(msg.to,"contact already off")
            elif msg.text.lower() == 'ลอคชื่อ':
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                else:
                    cl.sendText(msg.to,"bone..")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif msg.text.lower() == 'ปิดลอค':
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"Done..")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"bone..")
            elif "ปิดเชิญ" == msg.text:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"Done..")
            elif "เปิดเชิญ" == msg.text:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"Done..")
				except:
					pass
            elif msg.text.lower() == 'เปิดกัน':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
            elif msg.text.lower() == 'เปิดกันลิ้ง':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to on")
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to on")
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
            elif msg.text.lower() == 'เปิดกันเชิญ':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to on")
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to on")
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
            elif msg.text.lower() == 'เปิดกันยก':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
            elif msg.text.lower() == 'เปิดเข้า':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on")
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on")
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
            elif msg.text.lower() == 'ปิดเข้า':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off")
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off")
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
            elif msg.text.lower() == 'ปิดกัน':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
            elif msg.text.lower() == 'ปิดกันลิ้ง':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
            elif msg.text.lower() == 'ปิดกันเชิญ':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
            elif msg.text.lower() == 'ปิดกันยก':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
            elif msg.text in ["เปิดบอทยก"]:
	     if msg.from_ in admin:	        
                wait["BotCancel"] = True
                cl.sendText(msg.to,"เปิดใช้ระบบบอทยกเชิญอัติโนมัติ")
		print wait["BotCancel"]
	     else:
		    cl.sendText(msg.to,"คุณไม่มีสิทย์ใช้คำสั่งนี้(-..-)")
            elif msg.text in ["ปิดบอทยก"]:
	     if msg.from_ in admin:	        
                wait["BotCancel"] = False
                cl.sendText(msg.to,"ปิดใช้ระบบบอทยกเชิญอัติโนมัติแล้ว")
		print wait["BotCancel"]
	     else:
		    cl.sendText(msg.to,"คุณไม่มีสิทย์ใช้คำสั่งนี้(-..-)")
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar")
                    else:
                        cl.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'เปิดออก':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'ปิดออก':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'เปิดแชร์':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to on")
                    else:
                        cl.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to on")
                    else:
                        cl.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'ปิดแชร์':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to off")
                    else:
                        cl.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to off")
                    else:
                        cl.sendText(msg.to,"Share already off")
            elif msg.text.lower() == 'เช็ค':
                md = ""
                if wait["contact"] == True: md+="􏿿Contact:on 􀜁􀄯􏿿\n"
                else: md+="􏿿Contact:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􏿿Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􏿿Auto Join:off􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􏿿Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+="􏿿Group cancel:off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􏿿Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􏿿Auto leave:off 􀜁􀄰􏿿\n"
                if wait["BotCancel"] == True: md+="􏿿Bot cancel:on 􀜁􀄯􏿿\n"
                else: md+="􏿿Bot cancel:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􏿿Share:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􏿿Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Auto add:off 􀜁􀄰􏿿\n"
                if wait["autoBlock"] == True: md+="􏿿Auto Block:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Auto Block:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􏿿Protect:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Protect:off 􀜁􀄰􏿿\n"
                if wait["linkprotect"] == True: md+="􏿿Link Protect:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Link Protect:off 􀜁􀄰􏿿\n"
                if wait["inviteprotect"] == True: md+="􏿿Invitation Protect:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Invitation Protect:off 􀜁􀄰􏿿\n"
                if wait["cancelprotect"] == True: md+="􏿿Cancel Protect:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Cancel Protect:off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ub5abe828cd964292195c3c59d6322033"}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"By: RED SAMURI SELFBØT")
            elif cms(msg.text,["ผส","ผู้สร้าง"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ub5abe828cd964292195c3c59d6322033"}
                cl.sendMessage(msg)
                cl.sendText(mag.to,"Ini Creator Saya Jan Lupa Di add Ya kak")
            elif msg.text.lower() == 'เปิดแอด':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'ปิดแอด':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
            elif msg.text in ["Block on","เปิดออโต้บล็อค","เปิดบล็อค"]:
                if wait["autoBlock"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✔👎〘•ระบบออโต้บล็อค\nเปิดใช้งานอยุ่แล้ว•〙👍")
                    else:
                        cl.sendText(msg.to,"✔👎〘•เปิดใช้ระบบออโต้บล็อค\nเรียบร้อยแล้ว•〙👍")
                else:
                    wait["autoBlock"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"✔👎〘•เปิดใช้ระบบออโต้บล็อค\nเรียบร้อยแล้ว•〙👍")
                    else:
                        cl.sendText(msg.to,"✔👎〘•ระบบออโต้บล็อค\nเปิดใช้งานอยุ่แล้ว•〙👍")

            elif msg.text in ["AutoBlock off","ปิดออโต้บล็อค","ปิดบล็อค"]:
                if wait["autoBlock"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👎〘•ระบบออโต้บล็อค\nปิดใช้งานอยู่แล้ว•〙👎")
                    else:
                        cl.sendText(msg.to,"👎〘•ปิดระบบออโต้บล็อค\nเรียบร้อยแล้ว•〙👎")
                else:
                    wait["autoBlock"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👎〘•ปิดระบบออโต้บล็อค\nเรียบร้อยแล้ว•〙👎")
                    else:
                        cl.sendText(msg.to,"👎〘•ระบบออโต้บล็อค\nปิดใช้งานอยู่แล้ว•〙👎")
            elif "ตั้งข้อความแอด:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                cl.sendText(msg.to,"เชิญทำการเปลี่ยนแปลงข้อความคนแอด")
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ข้อความเมื่อเพิ่มเพื่อนโดยอัตโนมัติตั้งไว้ดังนี้ \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"ปลี่ยนการตั้งค่า ข้อความคนแอด ของคุณแล้ว \n  ดังนี้\n" + wait["message"])
            elif "ตั้งคอมเม้น:" in msg.text:
                c = msg.text.replace("คอมเม้น:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"เปลี่ยนการตั้งค่าคอมเม้นของคุณแล้ว ดังนี้")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"เปลี่ยนการตั้งค่าคอมเม้นของคุณแล้ว \n  ดังนี้\n" + c)
            elif msg.text in ["Com on","เปิดเม้น","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di")
                    else:
                        cl.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Actived")
                    else:
                        cl.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["ปิดเม้น"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["เช็คเม้น","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["คอมเม้น","Comment"]:
                cl.sendText(msg.to,"ข้อความแสดงความคิดเห็นอัตโนมัติถูกตั้งไว้ดังนี้:??\n\n" + str(wait["comment"]))
            elif msg.text in ["ข้อความแอด","message"]:
                cl.sendText(msg.to,"ข้อความตอบรับคนแอดถูกตั้งไว้ดังนี้:??\n\n" + str(wait["message"]))
            elif msg.text in ["ดำ"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"กรุณาส่ง คอนแทค บุคคลที่คุณต้องการเพิ่มในบัญชีดำ")
            elif msg.text in ["ขาว"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"กรุณาส่ง คอนแทค บุคคลที่คุณต้องการเพิ่มในบัญชีขาว")
            elif msg.text in ["บัญชีดำ"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"ไม่มีอะไรในบัญชีดำ")
                else:
                    cl.sendText(msg.to,"ต่อไปนี้เป็นรายชื่อที่อยู่ในบัญชีดำ")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Jam already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Jam")
#==============================================================================#
#==============================================================================#
            elif msg.text in ["Invite"]:
                wait["winvite"] = True
                cl.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["ดึง"]:
                wait["winvite"] = True
                cl.sendText(msg.to,"Send Contact")

            elif msg.text in ["Bot off"]:
                wait["Selfbot"] = False
                cl.sendText(msg.to,"Selfbot Sudah Di Nonaktifkan.")

            elif msg.text in ["เช็คคท"]:
                wait["contact"] = True
                cl.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                cl.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["Like on","เปิดไลค์"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","ปิดไลค์"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")

            elif msg.text in ["เปิดติ๊ก","Sticker on"]:
                if wait['stiker'] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Stiker Already On")
                    else:
                        cl.sendText(msg.to,"Stiker Already On")
                else:
                    wait["stiker"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Stiker Already On")
                    else:
                        cl.sendText(msg.to,"Stiker Already On")

            elif msg.text in ["ปิดติ๊ก","Sticker off"]:
                if wait["stiker"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Stiker Already Off")
                    else:
                        cl.sendText(msg.to,"Stiker Already Off")
                else:
                    wait["stiker"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Stiker Already Off")
                    else:
                        cl.sendText(msg.to,"Stiker Already Off")

            elif msg.text in ["Sambut2 on","รับแขก on"]:
                if wait["Wc2"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ yg joιn poto on")
                else:
                    wait["Wc2"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")

            elif msg.text in ["Sambut2 off","รับแขก off"]:
                if wait["Wc2"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ yg joιn poto off")
                else:
                    wait["Wc2"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                        
            elif msg.text in ["ใครเตะ on"]:
                if wait["Ki"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ yg kick on")
                else:
                    wait["Ki"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["ใครเตะ off"]:
                if wait["Ki"] == False:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"noтιғ yg kick off")
                else:
                    wait["Ki"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already oғғ")

            elif msg.text in ["Pergi on","ส่งแขก on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"noтιғ yg leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Pergi off","ส่งแขก off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"noтιғ yg leave off")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already oғғ")
            elif msg.text in ["เปิดก๊อก"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดใช้ระบบแจ้งเตือนคนเข้าออกอยู่แล้ว")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดใช้ระบบแจ้งเตือนคนเข้าออก")
            elif msg.text in ["ปิดก๊อก"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                         cl.sendText(msg.to,"ปิดใช้ระบบแจ้งเตือนคนเข้าออกอยู่แล้ว")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดใช้ระบบแจ้งเตือนคนเข้าออกแล้ว")
#=============================================================================#
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Success deactive simisimi")
                
            elif msg.text in ["Read on","เปิดอ่าน"]:
                wait['alwayRead'] = True
                cl.sendText(msg.to,"Auto Sider ON")
                
            elif msg.text in ["Read off","ปิดอ่าน"]:
                wait['alwayRead'] = False
                cl.sendText(msg.to,"Auto Sider OFF")
                
            elif msg.text in ["Autorespon on","เปิดแทค","Respon on","Respon:on"]:
                wait["detectMention"] = True
                wait["kickMention"] = False
                wait["Tagvirus"] = False
                cl.sendText(msg.to,"Auto Respon ON")
                
            elif msg.text in ["Autorespon off","ปิดแทค","Respon off","Respon:off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"Auto Respon OFF")

            elif msg.text in ["เปิดแทคเจ็บ","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                wait["detectMention"] = False
                wait["Tagvirus"] = False
                cl.sendText(msg.to,"[AUTO RESPOND] Auto Kick yang tag ON")
                
            elif msg.text in ["ปิดแทคเจ็บ","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"[AUTO RESPOND] Auto Kick yang tag ON")

            elif msg.text in ["Tagvirus on","เปิดแทคดับ"]:
                wait["Tagvirus"] = True
                wait["detectMention"] = False
                wait["kickMention"] = False
                cl.sendText(msg.to,"[AUTO RESPOND] tagvirus yang tag OFF")
                
            elif msg.text in ["Tagvirus off","ปิดแทคดับ"]:
                wait["Tagvirus"] = False
                cl.sendText(msg.to,"[AUTO RESPOND] tagvirus yang tag OFF")
#==============================================================================#
            elif "Hay" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Hay","")
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendMessage(msg.to,"Grup Dibersihkan")
            elif ("หวด " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
            elif ("ทดสอบ " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                           cl.cancelGroupInvitation(msg.to,[target])
                           cl.inviteIntoGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            
            elif "ปลิว: " in msg.text.lower():
                midd = msg.text.lower().replace("ปลิว: ","")
                cl.kickoutFromGroup(msg.to,[midd])
            
            elif ('invite ' in msg.text):
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)
                    cl.inviteIntoGroup(msg.to, [key])
                    contact = cl.getContact(key)
            
            elif msg.text.lower() == 'ยก':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak ada undangan")
                        else:
                            cl.sendText(msg.to,"Invitan tidak ada")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"Invitan tidak ada")
            
            elif msg.text.lower() == 'เปิดลิ้ง':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'ปิดลิ้ง':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","ลิ้ง"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                    
            elif msg.text in ["Backup:on","Backup on","เปิดดึงกลับ"]:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดระบบดึงคนกลับ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah on Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off","Backup off","ปิดดึงกลับ"]:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดระบบดึงคนกลับแล้ว\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Backup Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Sudah off Bos\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    
            elif msg.text.lower() == 'เช็คบอท':
                eltime = time.time() - mulai
                start = time.time()
                time.sleep(0.07)
                elapsed_time = time.time() - start
                van = "ระยะเวลาการทำงานของบอท : " + "\n" +waktu(eltime)
                md = ""
                if wait["contact"] == True: md+="􏿿Contact:on 􀜁􀄯􏿿\n"
                else: md+="􏿿Contact:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􏿿Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􏿿Auto Join:off􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􏿿Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+="􏿿Group cancel:off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􏿿Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􏿿Auto leave:off 􀜁􀄰􏿿\n"
                if wait["BotCancel"] == True: md+="􏿿Bot cancel:on 􀜁􀄯􏿿\n"
                else: md+="􏿿Bot cancel:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􏿿Share:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􏿿Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Auto add:off 􀜁􀄰􏿿\n"
                if wait["autoBlock"] == True: md+="􏿿Auto Block:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Auto Block:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􏿿Protect:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Protect:off 􀜁􀄰􏿿\n"
                if wait["linkprotect"] == True: md+="􏿿Link Protect:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Link Protect:off 􀜁􀄰􏿿\n"
                if wait["inviteprotect"] == True: md+="􏿿Invitation Protect:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Invitation Protect:off 􀜁􀄰􏿿\n"
                if wait["cancelprotect"] == True: md+="􏿿Cancel Protect:on 􀜁􀄯􏿿\n"
                else:md+="􏿿Cancel Protect:off 􀜁􀄰􏿿\n"
                cl.sendText(msg.to,"ครับผม! บอทยังอยู่ครับ" + " \n" + van + "\n\n☞「 ความเร็วของเซลบอท ณ ตอนนี้อยู่ที่」\n☞ Speed : %sseconds" % (elapsed_time) + "\n\n🌴การตั้งค่าของบอทถูกตั้งไว้ดังนี้🌴" + "\n" + md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ub5abe828cd964292195c3c59d6322033"}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"By: RED SAMURI SELFBØT")
                 

        
#================================  STARTED ==============================================#

            elif cms(msg.text,["ผู้สร้าง","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u46a050ebcc66a90b47fae6256547cc53"}
                cl.sendMessage(msg)
                    
            elif "แอด" == msg.text.lower():
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
                    cl.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == 'ดึง:แอด':
                if msg.toType == 2:
                       ginfo = cl.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           cl.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           cl.inviteIntoGroup(msg.to,[gcmid])
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    cl.updateGroup(X)
            
            elif msg.text.lower() == 'ข้อมูลกลุ่ม':        
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[ชื่อของกลุ่ม 👉 ]\n" + group.name + "\n\n[Iไอดีของกลุ่ม : ]\n" + group.id + "\n\n[ผู้สร้างกลุ่ม :]\n" + gCreator + "\n\n[รูปภาพของกลุ่ม : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nลิ้งของกลุ่ม : เปิด"
                    else: md += "\n\nลิ้งของกลุ่ม : ปิด"
                    if group.invitee is None: md += "\nจำนวนสมาชิก : " + str(len(group.members)) + " คน" + "\nจำนวนสมาชิกค้างเชิญ : 0 คน"
                    else: md += "\nจำนวนสมาชิก : " + str(len(group.members)) + " คน" + "\nจำนวนสมาชิกค้างเชิญ : " + str(len(group.invitee)) + " คน"
                    cl.sendText(msg.to,md)
            
            elif msg.text.lower() == 'ไอดีกลุ่ม':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
#==============================================================================#
            elif "เช็ค: " in msg.text:
                saya = msg.text.replace("เช็ค: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                cl.sendMessage(msg)
                contact = cl.getContact(saya)
                cu = cl.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"ชื่อ. :\n" + contact.displayName + "\n\nสเตตัส. :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"รูปโปร. " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"รูปปก. " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "เช็คกลุ่ม: " in msg.text:
                saya = msg.text.replace("เช็คกลุ่ม: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).id
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "ชื่อกลุ่ม :\n" + group.name + "\n\nไอดีกลุ่ม :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nลิ้งกลุ่ม : ปิด"
                            else: md += "\n\nลิ้งกลุ่ม : เปิด"
                            if group.invitee is None: md += "\nจำนวนสมาชิก : " + str(len(group.members)) + " คน" + "\nจำนวนสมาชิกค้างเชิญ : " + str(len(group.invitee)) + " 0 คน"
                            else: md += "\nจำนวนสมาชิก : " + str(len(group.members)) + " คน" + "\nจำนวนสมาชิกค้างเชิญ : " + str(len(group.invitee)) + " 8o"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["รายชื่อเพื่อน"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["รายชื่อสมาชิก"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif ('Grupmember' in msg.text):
                saya = msg.text.replace('Grupmember','')
                gid = cl.getGroupIdsJoined()
                num=1
                msgs="═════════List Member═════════-"
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    me = gna.members(i)
                    msgs+="\n[%i] %s" % (num, me.displayName)
                    num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(me)
                    if h == saya:
                        cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="═════════List FriendMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["เช็คบล็อค"]: 
                blockedlist = cl.getBlockedContactIds()
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["รายชื่อกลุ่ม"]:  
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["เช็คไอดีกลุ่ม"]:   
                gruplist = cl.getGroupIdsJoined()
                kontak = cl.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "ชื่อกลุ่ม" in msg.text.lower():
                saya = msg.text.lower().replace('ชื่อกลุ่ม','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ชื่อกลุ่ม : ]\n" + gid.name)
            
            elif "ไอดีกลุ่ม" in msg.text:
                saya = msg.text.replace('ไอดีกลุ่ม','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ไอดีกลุ่ม : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                saya = msg.text.replace('Grupinfo: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    group = cl.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            cl.sendText(msg.to,md)
                            cl.sendMessage(msg)
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Glist"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (cl.getGroup(i).name +" ? ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
                
            elif "กันรัน" in msg.text:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"คำเชิญเข้ากลุ่มจะถูกปฏิเสธคำเชิญทั้งหมด")
                else:
                    cl.sendText(msg.to,"เปิดปฏิเสธคำเชิญทั้งหมดอยู่แล้ว")
            elif msg.text in ["ลบรัน"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ลบห้องเชิญเรียบร้อยแล้ว")
            elif msg.text in ["Delete chat","ล้างแชท"]:
                cl.removeAllMessages(op.param2)
                cl.sendText(msg.to,"สำเร็จ..Delete Chat")
                cl.sendText(msg.to,"Success...")
            elif "ลบแชท" in msg.text:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")
                    
            elif msg.text.lower() == 'gcancel':
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
                         
            elif "แอดทั้งห้อง" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.findAndAddContactsByMids(mi_d)
                cl.sendText(msg.to,"แอดทุกคนในห้องนี้แล้วคับ")
#==============================================================================#
            elif "แจ๊ะ" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "แทคสมาชิกแล้วจำนวน:\n" + str(jml) +  " คน"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)

            elif msg.text in ["Setview","จับ","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "☆Checkpoint Checked☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","อ่าน","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠═════════════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        cl.sendText(msg.to, "☆Auto Checkpoint☆")                        
                    else:
                        cl.sendText(msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"
            elif "ประกาศกลุ่ม: " in msg.text:
                bc = msg.text.replace("ประกาศกลุ่ม: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.sendText(i,"======[ข้อความประกาศกลุ่ม]======\n\n"+bc+"\n\nBy: RED SAMURI SELFBOT!!")
                    
            elif "ประกาศแชท: " in msg.text:
                bc = msg.text.replace("ประกาศแชท: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendText(i,"======[ข้อความประกาศแชท]======\n\n"+bc+"\n\nBy: RED SAMURI SELFBOT!!")
            
            elif "ส่งรูปภาพตามกลุ่ม: " in msg.text:
                bc = msg.text.replace("ส่งรูปภาพตามกลุ่ม: ","")
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.sendImageWithURL(i, bc)
                    
            elif "ส่งรูปภามตามแชท: " in msg.text:
                bc = msg.text.replace("ส่งรูปภาพตามแชท: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendImageWithURL(i, bc)
            
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")
    
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["commen1"])
            
            elif "Halo @" in msg.text:
                _name = msg.text.replace("Halo @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "รันคทไวรัส @" in msg.text:
                _name = msg.text.replace("รันคทไวรัส @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': "u46a050ebcc66a90b47fae6256547cc53',"}
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(g.mid,msg)
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
            elif "github " in msg.text:
                    a = msg.text.replace("github ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"เริ่มต้นค้นหา ...")
                    cl.sendText(msg.to, "Title: " + a + "\nLink: https://github.com/search?q=" +b)
                    cl.sendText(msg.to, "☝กดลิ้งเข้าไปหาเองเด้อ🔬👌🔭")
            elif "เพลสโต " in msg.text:
                    tob = msg.text.replace("เพลสโต ","")
                    cl.sendText(msg.to,"กำลังค้นหาชื่อแอพ...")
                    cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    cl.sendText(msg.to,"☝กดลิ้งเข้าไปโหลดได้เลยนะ ^ - ^")
            elif "twitter " in msg.text:
                    a = msg.text.replace("twitter ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"เริ่มต้นทำการค้นหา ...")
                    cl.sendText(msg.to, "https://www.twitter.com/search?q=" + b)
                    cl.sendText(msg.to,"ทำการค้นหาสำเร็จ เชิญเข้าไปส่องโลด😆😆") 
            elif "smule " in msg.text:
                    a = msg.text.replace("smule ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"กำลังเริ่มต้นค้นหา ...")
                    cl.sendText(msg.to, "Nama: "+b+"\nId smule: http://smule.com/search?q=" +b)
            elif "ไอจี " in msg.text:
                     a = msg.text.replace("ไอจี ","")
                     b = urllib.quote(a)
                     cl.sendText(msg.to,"กำลังเริ่มต้นค้นหา ...")                       
                     cl.sendText(msg.to,  "https://www.instagram.com/"+b+"?hl=th")
                     cl.sendText(msg.to,"ทำการค้นหาสำเร็จ เชิญเข้าไปส่องโลด😆😆")
            elif "เฟสบุค" in msg.text:
                    a = msg.text.replace("เฟสบุค","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"กำลังเริ่มต้นค้นหา ...")
                    cl.sendText(msg.to, "https://www.facebook.com" + b)
                    cl.sendText(msg.to," ทำการค้นหาสำเร็จ ") 
            elif "ส่องเฟส " in msg.text:
                    a = msg.text.replace("ส่องเฟส ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"กำลังเริ่มต้นค้นหา ...")
                    cl.sendText(msg.to, "https://www.facebook.com/search/top/?q=" + b)
                    cl.sendText(msg.to,"ทำการค้นหาสำเร็จ เชิญเข้าไปส่องโลด😆😆")
            elif "กูเกิ้ล " in msg.text:
                    a = msg.text.replace("กูเกิ้ล ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"โปรดรอสักครู่...")
                    cl.sendText(msg.to, "https://www.google.co.th/search?q=" + b)
                    cl.sendText(msg.to,"ทำการค้นหาสำเร็จ↖(^ω^)↗")
            elif "ยูทูป " in msg.text:
                    a = msg.text.replace("ยูทูป ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"โปรดรอสักครู่...")
                    cl.sendText(msg.to, "https://www.youtube.com/results?search_query=" + b)
                    cl.sendText(msg.to,"ทำการค้นหาสำเร็จ↖(^ω^)↗")                
            elif 'wikipedia ' in msg.text:
                try:
                    wiki = msg.text.replace("wikipedia ","")
                    wikipedia.set_lang("th")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    cl.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="ข้อความยาวเกินไปโปรดกดที่ลิ้งเพื่อดูข้อมูล\n"
                            pesan+=wikipedia.page(wiki).url
                            cl.sendText(msg.to, pesan)
                        except Exception as e:
                            cl.sendText(msg.to, str(e))
                            
            elif "video " in msg.text:
		    a = msg.text.replace("video ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"โปรดรอสักครู่...")
                    cl.sendText(msg.to, "{ Xvideos search page }\n\nTitle: "+b+"\nSource : https://porngangs.com/?tag=" +b)
                    
            elif "วีดีโอ " in msg.text:
                    a = msg.text.replace("วีดีโอ ", "")
                    b = urllib.quote(a)                        
                    url = "https://www.youtube.com/watch?v=" + b
                    cl.sendText(msg.to,"โปรดรอสักครู่...")
                    cl.sendText(msg.to,url)
                    cl.sendVideoWithURL(msg.to, url)
                    cl.sendText(msg.to,"ทำการค้นหาสำเร็จ↖(^ω^)↗")
            
            elif "Youtube " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
            elif "mp4 " in msg.text:
                        a = msg.text.replace("mp4 ", "").strip()
                        query = urllib.quote(a)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find()
                        ght = ('https://www.youtube.com' + results)
                        cl.sendVideoWithUrl(msg.to, ght)
                            
            elif "say " in msg.text:
                say = msg.text.replace("say ","")
                lang = 'th'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif msg.text in ["ส่งของขวัญ"]:
                wait["gift"] = True
                cl.sendText(msg.to,"ส่งคทมาเลยคับ") 
                
            elif msg.text in ["ก๊อปคท"]:
                wait2["copy"] = True
                cl.sendText(msg.to,"ส่งคทมาเลยคับ") 
                
            elif msg.text in ["รันของขวัญ"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg) 
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)    
                
            elif msg.text in ["เชิญ:@"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
                       
            elif msg.text in ["Leaveallgroup"]: 
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                for i in gid:
                  vipro.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh selfbot...!!!\nMakasih...!!!")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
                  
            elif "tak" in msg.text:
              if msg.from_ in creator + admin:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*200 : (j+1)*200]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
            elif msg.text in ["kick:@"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
                        
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                        
            elif "/Sendpm " in msg.text:
                    bctxt = msg.text.replace("/Sendpm ", "")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendText(manusia, (bctxt))
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")

#            elif msg.text.lower() in dangerMessage:
#                if msg.toType == 2:
#                    try:
#                        cl.kickoutFromGroup(msg.to,[msg.from_])
#                    except:
#                        cl.kickoutFromGroup(msg.to,[msg.from_])
#                        cl.sendText(msg.to, "Hati-Hati bicara ya kak....!!!")
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                cl.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                cl.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                cl.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["pap"])
#==============================================================================#
            elif 'รูป ' in msg.text:
                googl = msg.text.replace('รูป ',"")

                url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl

                raw_html =  (download_page(url))

                items = []

                items = items + (_images_get_all_items(raw_html))

                path = random.choice(items)

                try:

                    start = timeit.timeit()

                    cl.sendImageWithURL(msg.to,path)

                    cl.sendText(msg.to, "Google Image \nType: Search Image\nWaktu dicari: %s" % (start) +"\nTotal Image Links = "+str(len(items)))

                    print "[Notif] Search Image Google Sucess"

                except Exception as e:

                    cl.sendText(msg.to, str(e))
            elif msg.text.lower() == 'ไอดี':
                cl.sendText(msg.to,mid)
            elif "โพส: " in msg.text:
                tl_text = msg.text.replace("โพส: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "เปลี่ยนชื่อ: " in msg.text:
                string = msg.text.replace("เปลี่ยนชื่อ: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เปลี่ยนชื่อของคุณแล้วดังนี้👇 " + "\n" + string + "")
            elif "เปลี่ยนตัส: " in msg.text:
                string = msg.text.replace("เปลี่ยนตัส: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"เปลี่ยนตัสของคุณแล้วดังนี้ " + string + "")
            elif msg.text in ["ชื่อ"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["ตัส"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["รูปโปร"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["วีดีโอโปร"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["ลิ้งรูปโปร"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["รูปปก"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
            elif msg.text in ["ลิ้งรูปปก"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendText(msg.to, path)
#======================================================================#
            elif "เปิดสแกน" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"เปิดระบบสแกนคนอ่านอัตโนมัติ")
                
            elif "ปิดสแกน" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "ปิดระบบสแกนคนอ่านอัตโนมัติแล้ว")
                else:
                    cl.sendText(msg.to, "โปรดใช้คำสั่งเปิดแสกนก่อนจะปิด")
#============================================================================#
            elif "idline: " in msg.text:
                msgg = msg.text.replace('idline: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)
            elif "ไอดี @" in msg.text:
                _name = msg.text.replace("ไอดี @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "ข้อมูล " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "ตัส " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "ชื่อ " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "รูปปก " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "คท " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
                
            elif "รูปโปร @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("รูปโปร @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
                
            elif "วีดีโอโปร @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("วีดีโอโปร @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
                
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
                
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            
            elif "ลิ้งรูปปก @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("ลิ้งรูปปก @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "รูปกลุ่ม" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "ลิ้งรูปกลุ่ม" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
            elif "Clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = cl.getContact(target)
                        X = contact.displayName
                        profile = cl.getProfile()
                        profile.displayName = X
                        cl.updateProfile(profile)
                        cl.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = cl.getProfile()
                        lol.statusMessage = Y
                        cl.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        hun = cl.getProfile()
                        hun.pictureStatus = P
                        cl.updateProfile(hun)
                    except Exception as e:
                        cl.sendText(msg.to, "Failed!")
                        print e

            elif msg.text in ["คืนร่าง"]:
                try:
                    cl.updateProfile.pictureStatus(backup.pictureStatus)
                    cl.updateProfile.statusMessage(backup.statusMessage)
                    cl.updateProfile.displayName(backup.displayName)
                    cl.sendText(msg.to, "กลับร่างเดิมแล้ว")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text.lower() == 'แปลงร่าง ':
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            cl.CloneContactProfile(contact)
                            cl.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            cl.sendMessage(msg.to, "Gagal clone member")
                            
            elif "ก๊อป @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("ก๊อป @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
            elif msg.text == "Copy":
                if msg.toType == 0:
                    targ = cl.getContact(msg.to)
                    me = cl.getProfile()
                    me.displayName = targ.displayName
                    me.statusMessage = targ.statusMessage
                    me.pictureStatus = targ.pictureStatus
                    cl.updateDisplayPicture(me.pictureStatus)
                    cl.updateProfile(me)
                    cl.sendText(msg.to,"สำเร็จแล้ว")
                else:
                    cl.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในแชทส่วนตัวเท่านั้น")
#==============================================================================#
            elif "/fancytext: " in msg.text:
                txt = msg.text.replace("/fancytext: ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)
                
            elif "อู้-id " in msg.text:
                isi = msg.text.replace("อู้-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "อู้-en " in msg.text:
                isi = msg.text.replace("อู้-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "อู้-ar" in msg.text:
                isi = msg.text.replace("อู้-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "อู้-jp" in msg.text:
                isi = msg.text.replace("อู้-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "อู้-ko" in msg.text:
                isi = msg.text.replace("อู้-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            
            elif "Th@en" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Th@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO ENGLISH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "En@th" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("En@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM EN🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Th@jp" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Th@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO JP🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Jp@th" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Jp@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM JP🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM ID🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO ID🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Th@ar" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Th@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO AR🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Ar@th" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Ar@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM AR🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Th@ko" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Th@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM TH🍁\n" + "" + kata + "\n🍁TO KO🍁\n" + "" + result + "\n🍁SUKSES🍁")
            elif "Ko@th" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Ko@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"🍁FROM KO🍁\n" + "" + kata + "\n🍁TO TH🍁\n" + "" + result + "\n🍁SUKSES🍁")
                
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"🙏สวัสดีคับคนมาใหม่ 🙏" + "\n🌾ยินดีต้อนรับเข้าสู่กลุ่ม 🌾" + "\n👉" + str(ginfo.name) + "👈" + "\nมาใหม่แก้ผ้าด้วยนะ😂😂")
                cl.sendText(msg.to,"By: •─✯RED★SAMURI★SELFBOT✯─•")
                jawaban1 = ("ยินดีที่ได้รู้จักนะครับ " + "ผมชื่อเรด นะ")
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
                
            elif msg.text.lower() == 'แนะนำตัว':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"🙏สวัสดีคับทุกคน 🙏" + "\n🌾ยินดีที่ได้เข้ามาในกลุ่ม 🌾" + "\n👉" + str(ginfo.name) +"👈")
                cl.sendText(msg.to," สวัสดีแอดด้วยนะ"  +  "\nมาใหม่ต้องแก้ผ้าด้วยรึเปล่า 😆😆" + "\n\nBy: •─✯RED★SAMURI★SELFBOT✯─•")
                jawaban1 = ("ผมชื่อเรดนะ" + "ยินดีที่ได้รู้จักกับทุกคนครับ")
                tts = gTTS(text=jawaban1, lang='th')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-Th " in msg.text:
                say = msg.text.replace("Say-Th ","")
                lang = 'Th'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                  
            elif "แซว" in msg.text:
                  tanya = msg.text.replace("แซว","")
                  jawab = ("สอ บอ มอ ยอ หอ","ว่าไงน้องสาว","ใครโสดขอมือหน่อย","ตับ ตับตับ ตับตับ")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='th')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')                     
            
            elif 'Music ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Music ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
            
            elif "/รูป " in msg.text:
                search = msg.text.replace("/รูป ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif "เช็คไอจี " in msg.text:
                    try:
                        instagram = msg.text.replace("เช็คไอจี  ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?hl=th")
                        data = response.read()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendText(msg.to, str(text))
                        cl.sendImageWithURL(msg.to, profileIG)
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
                        
            elif "/postig" in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                cl.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                cl.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                        
            elif msg.text.lower() == 'time':
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bulan = blan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst)

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text.lower() == 'ปฏิทิน':
	    	    wait2['setTime'][msg.to] = datetime.today().strftime('วันเดือนปี : %Y-%m-%d \nDay : %A \nเวลา : %H:%M:%S')
	            cl.sendText(msg.to, "🍁ปฏิทิน👉REDSAMURI SELFBØT🍁\n\n" + (wait2['setTime'][msg.to]))
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif msg.text.lower() == 'reboot':
                    print "[Command]Restart"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        cl.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif "Turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
                
            elif msg.text.lower() == 'runtime':
                cl.sendText(msg.to,"「Please wait..」\nType  :Loading...\nStatus : Loading...")
                eltime = time.time() - mulai
                van = "Type : Bot Sedang Berjalan \nStatus : Aktif \nMySelbot sudah berjalan selama"+waktu(eltime)
                cl.sendText(msg.to,van)                    
#==============================================================================#
            elif "รันโลด" in msg.text:
                thisgroup = cl.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"RED SAMURI")
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"RED SAMURI")
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"RED SAMURI")
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"RED SAMURI")
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"RED SAMURI")
                cl.createGroup("RED SAMURI SELFBOT", mi_d)
                cl.sendText(msg.to,"RED SAMURI")


            elif "รัน @" in msg.text:
                print "[Command]covergroup"
                _name = msg.text.replace("รัน @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                           thisgroup = cl.getGroups([msg.to])
                           Mids = [target for contact in thisgroup[0].members]
                           mi_d = Mids[:33]
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.createGroup("RED SAMURI Group",mi_d)
                           cl.sendText(msg.to,"🏂⛷️[จะออกไปแตะขอบฟ้า]")
                           cl.sendText(msg.to,"เรียบร้อย")
                        except:
                            pass
                print "[Command]covergroup"

            elif "รันแชท @" in msg.text:
                _name = msg.text.replace("รันแชท @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI") 
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(g.mid,"RED SAMURI")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
            elif "รัน: " in msg.text: 
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)                   
                    contact = cl.getContact(key)
                    cl.createGroup(msg.to,contact)
                    cl.sendText(msg,to,"┌∩┐(◣_◢)┌∩┐")
 #           var gname = this.messages.text.split(" ",2)[1];
 #       var uids = this.messages.text.replace("run "+gname+" ","").split(" ");
#        while(uids.indexOf("") != -1){
 #           let i = uids.indexOf("");
#           uids.splice(i,1);
#        }
   #     for(let i = 0; i < 1000; i++){
  #          this._createGroup(gname,uids);
#=================================================================================#
            elif "ของขวัญ @" in msg.text:
                _name = msg.text.replace("ของขวัญ @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 2
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)
                        cl.sendText(msg.to, "🌸ตรวจสอบของขวัญได้ที่แชทนะจ๊ะ🌸...😘😘")
            elif "ส่งของขวัญ " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("ส่งของขวัญ ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + "🌸ตรวจสอบของขวัญได้ที่แชทนะจ๊ะ🌸...😘😘")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
            elif "ของขวัญ2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("ของขวัญ1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " 🌸ตรวจสอบของขวัญได้ที่แชทนะจ๊ะ🌸...😘😘")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "ของขวัญ3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("ของขวัญ2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " 🌸ตรวจสอบของขวัญได้ที่แชทนะจ๊ะ🌸...😘😘")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "ของขวัญ4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("ของขวัญ4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " 🌸ตรวจสอบของขวัญได้ที่แชทนะจ๊ะ🌸...😘😘")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
            elif msg.text in ["แสกนดำ"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user\nมีบัญชีดำของคุณอยู่กลุ่มนี้")
                    xname = ""
                    for mi_d in wait["blacklist"]:
                        xname = cl.getContact(mi_d).displayName + ""
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
                    try:
                        cl.sendMessage(msg)
                    except Exception as error:
                        print error
            elif "แบนกลุ่ม: " in msg.text:
		grp = msg.text.replace("แบนกลุ่ม: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = red.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus red")
 
            elif msg.text in ["กลุ่มติดดำ","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        cl.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        cl.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["ล้างแบนกลุ่ม: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("ล้างแบนกลุ่ม: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus red")
            elif "แบน @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("แบน @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                cl.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "ล้างแบน @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("ล้างแบน @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                cl.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                cl.sendText(msg.to,_nametarget + " Not In Blacklist")
            elif msg.text in ["แบน"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["ล้างแบน"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")

            elif "แบน:" in msg.text:                  
                       nk0 = msg.text.replace("แบน:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "ล้างแบน:" in msg.text:                  
                       nk0 = msg.text.replace("ล้างแบน:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    cl.sendText(msg.to,_name + " Not In Blacklist")
                                    
            elif msg.text in ["เครีย์แบน"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text.lower() == '/ดำ':
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == '/ขาว':
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["เช็คดำ"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"ไม่มีอะไรในบัญชีดำ")
                else:
                    cl.sendText(msg.to,"รายชื่อสมาชิกในบัญชีดำ")
                    num=1
                    msgs="══════════List Blacklist═════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "══════════List Blacklist═════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'ไล่ดำ':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "#Banall" in msg.text:
                       nk0 = msg.text.replace("#Banall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "#Unbanall" in msg.text:
                       nk0 = msg.text.replace("#Unbanall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")
                                    
        elif msg.text in ["ดับไฟ"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u46a050ebcc66a90b47fae6256547cc53',"}
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
        elif msg.text.lower() == 'รี':
                if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"waitting...")
                        cl.leaveGroup(msg.to)

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)

                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
        elif msg.text.lower() == 'บูท':
                if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"waitting...")
                        cl.leaveGroup(msg.to)

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        cl.leaveGroup(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        cl.leaveGroup(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        cl.leaveGroup(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
        elif "Leave all" == msg.text:
		gid = cl.getGroupIdsJoined()
                if msg.from_ in mid:
		    for i in gid:
			cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        cl.leaveGroup(i)
		    cl.sendText(msg.to,"Success Leave All Group")
		else:
		    cl.sendText(msg.to,"คุณไม่มีสิทย์ใช้คำสั่งนี้")
		
        elif msg.text in ["ออก"]:
              if msg.from_ in mid:
				gid = cl.getGroupIdsJoined()
				for i in gid:
					cl.leaveGroup(i)
					
        elif msg.text in ["Acc invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"ยอมรับคำเชิญทั้งหมดจากกลุ่มแล้ว :\n" + _list)
                    else:
                        cl.sendText(msg.to,"ไม่มีกลุ่มที่รอดำเนินการในขณะนี้")
        elif "@bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass                         
#===============================================================================#  
                
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            G = cl.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[cl]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.1)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       cl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots:
                    try:
                        gs = cl.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            cl.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    cl.cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 5:
            if wait["autoBlock"] == True:
                cl.BlockedContactIds(op.param1)
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        pass
                    pass
                    cl.sendText(op.param1,"Group Name Lock")
                    cl.sendText(op.param1,"Haddeuh dikunci Pe'a")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param2}
                    cl.sendMessage(c)                           
                            
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in admin:
		    cl.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"Maaf " + red.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        cl.leaveGroup(op.param1)                        
		    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = ck.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
	    else:
                if wait["BotCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
			cl.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
#==============================================================================#
#------------------------------------------------------------------------------#
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nรู้นะว่าอ่านอยู่. . .\nออกมาคุยเดี๋ยวนี้ (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
                                    else:
                                        cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nนี่ก็อีกคน. . .อ่านอย่างเดียวเลย\nไม่ออกมาคุยล่ะ (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                        c.contentMetadata={'mid':op.param2}
                                        cl.sendMessage(c)
                                else:
                                    cl.sendText(op.param1, "ฮั่นแน่ " + "☞ " + Name + " ☜" + "\nแอบกันจังเลยนะ???\nคิดว่าเป็นนินจารึไง...??😆😆   ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                    c.contentMetadata={'mid':op.param2}
                                    cl.sendMessage(c)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
 
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,200):
      hasil = cl.activity(limit=200)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)

def likeme():
    for zx in range(0,200):
        hasil = cl.activity(limit=200)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like"
                
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
        
