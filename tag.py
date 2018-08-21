# ™❍✯͜͡RED™SAMURI✯͜͡❂➣
# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

red = LINE('EuVDmOMxhlXsUH1PNcf0.ikpGEj3TiZYQPDo1K/dkaa.9CWLht8bEEgj6r5QD0/7317c+ZmOj3BDNNltA0ttkv8=')
#red = LINE("TOKEN KAMU")
#red = LINE("Email","Password")
red.log("Auth Token : " + str(red.authToken))
channelToken = red.getChannelResult()
red.log("Channel Token : " + str(channelToken))

redMID = red.profile.mid
redProfile = red.getProfile()
redSettings = red.getSettings()
oepoll = OEPoll(red)
Rfu = [red]
RfuBot=[redMID]
admin=['ub5abe828cd964292195c3c59d6322033','u9f85803bded7abba7b0f5e11fe6dfbf8',redMID]
Family=["ub5abe828cd964292195c3c59d6322033","u9f85803bded7abba7b0f5e11fe6dfbf8",redMID]
RfuFamily = RfuBot + Family

wbanlist = []
wblacklist = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)

settings = {
   'acommentOn':False,
   'bcommentOn':False,
   'bcommentOn':False,
   'autoRead':False,
   'autoJoinTicket':True,
   'autoLeave':True,
   'autoAdd':True,
   'autoBlock':True,
   'autoJoin':True,
   'comment':"""💗RED SAMURAI SELFBOT💗 
🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁
🎀รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา
💝ราคาดูที่หน้างาน
📌มีบริการให้เช่าเซลบอท SAMURAI 
📌ร่างครึ่งคนครึ่งบอท
📌ราคาว่ากันตามคุณภาพนะครับ
📌ราคา200บาทต่อเดือน (ถูกมาก..)
📌เพิ่มคิกเกอร์ตัวละ100👌
👉บินได้ครับ
👉รันได้ครับ
👉ป้องกันกลุ่มเจอบินได้
👉มีเปิดปิดแสกนคำหยาบกับบอทบิน
👉แอบดูคนอ่านแบบดึง คท.ได้
👉แทคได้ทั้งห้อง
👉แทคแบบสั่งจำนวนเป็นรายบุคคลได้
👉แทคแบบสั่งจำนวนในแชทส่วนตัวได้
👉รันแชทได้
👉สั่งบล็อคใครก็ได้
👉สั่งเพิ่มเพื่อนแบบแทคได้
👉ลบแชทได้
👉กันรันได้100%
👉ลบรันได้
👉มุดลิ้งได้
👉เช็คโพส,เช็คคท,เช็คข้อมูลคนอื่นได้
👉เช็คข้อมูลตัวเอง,เช็คข้อมูลกลุ่มได้
👉ปฏิเสธคำเชิญแบบใส่ข้อความลงไปได้
👉ดึงห้องรวมได้
👉ตั้งปฏิเสธกลุ่มเชิญตามจำนวนสมาชิกได้
👉เล่นเซลในแชทสตได้
👉ตั้งข้อความคนเข้าคนออกได้
👉ตั้งข้อความคนลบสมาชิกได้
👉ตั้งข้อความคนแอดได้
👉สมารถเรียกดูการตั้งค่าข้อความได้ทั้งหมด
👉ตั้งหรือลบสติ๊กเกอร์ คนเข้า คนออก คนลบ
👉ตั้งหรือลบสติ๊กเกอร์ คนแอด คนแอบ คนแทค
👉ตั้งคำห้ามพิม ใครพิมจะโดนเตะ
👉ถามปัญหาได้ทุกคำถาม
👉สั่งเขียนข้อความได้ตามใจ
👉ดึงคท จากไอดีไลน์ หรือจาก mid ได้
👉อัพเดตลูกเล่นใหม่ๆทุกเดือน
🍷มีความสามารถอีกเยอะดูเอาระกัน🍷
🎀สนใจรีบทัก🎀
🎉บอทpython3ฟังชั่นล้นหลาม คุณภาพแน่นปึ๊ก
🎁กำลังรอให้คุณเป็นเจ้าของ....
╔══════════════┓
╠™❍✯͜͡RED™SAMURAI✯͜͡❂➣ 
╚══════════════┛
🎀รับทำชื่อ🎀ทำตัส🎀ทำดิส🎀ทำปก🎀
🎀ราคากันเอง..ไม่แพงแน่นอน🎀（＾ω＾）

สนใจทักมาได้ที่  👇👇👇👇👇👇👇👇👇
1. https://line.me/ti/p/~samuri5

หรือโทรมาได้ที่เบอร์นี้ 👇👇👇👇👇👇
1. โทร📲0946345913📞
2. โทร📲0631041275📞
ขอแสดงความนับถือ
จากทีมงาน SAMURAI ทุกคน""",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "addPesan": "🙏สวัสดีครับ🙏เพื่อนใหม่\n👉สนใจทำเซลบอท แก้ไฟลเซล เพิ่มไฟลเซล สอนทำเซล กด1\n👉สนใจทำปก ทำดิส กด2\n👉สนใจสั่งตั๋วสิริ ลงบอทสิริ บอทapi กด3\n👉สนใจเช่าเซิฟ Vps กด4\n👉สนใจสั่งซื้อสติ๊กเกอร์ ทีมไลน์ กด5\n👉แอดมาเก็บคท กด6\n👉แอดแล้วไม่พูดไม่ทัก กดบล็อค\n👉แต่ถ้าทักแล้วไม่ตอบ. หรือตอบช้า โทรมาเบอร์นี้เลยคับ 094 634 5913 @!",
    "addSticker": {
        "name": "",
        "status": False,
    },
    "mentionPesan": " ว่าไง? ที่รัก􀄃􀈻",
    "messageSticker": {
        "addName": "",
        "addStatus": False,
        "listSticker": {
            "addSticker": {
                "STKID": "409",
                "STKPKGID": "1",
                "STKVER": "100"
            },
            "leaveSticker": {
                "STKID": "51626533",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "kickSticker": {
                "STKID": "123",
                "STKPKGID": "1",
                "STKVER": "100"
            },
            "readerSticker": {
                "STKID": "51626530",
                "STKPKGID": "11538",
                "STKVER": "1"
            },
            "responSticker": {
                "STKID": "103",
                "STKPKGID": "1",
                "STKVER": "100"
            },
            "sleepSticker": "",
            "welcomeSticker": {
                "STKID": "51626527",
                "STKPKGID": "11538",
                "STKVER": "1"
            }
        }
    },
    "mimic": {
       "copy": False,
       "status": False,
       "target": {}
    }
}
RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
    "autoBlock": True,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = redMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = red.getProfile() 
backup = red.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 

myProfile["displayName"] = redProfile.displayName
myProfile["statusMessage"] = redProfile.statusMessage
myProfile["pictureStatus"] = redProfile.pictureStatus
#==============================================================================#
def RhyN_(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@Rh'
        red.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#==============================================================================================================
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        red.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        red.sendMessage(to, "[ INFO ] Error :\n" + str(error))                        
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + red.profile.userid
                        red.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+red.getContact(redMID).pictureStatus, red.getContact(redMID).displayName)
                    except Exception as error:
                        logError(error)
                        
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    red.sendMessage(to, '', contentMetadata, 7)

def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            red.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
        
def Rapid1Say(mtosay):
    red.sendText(Rapid1To,mtosay)

def delete_log():
    ndt = datetime.datetime.now()
    for data in msg_dict:
        if (datetime.datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = red.genOBSParams({'oid': redMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = red.server.postContent('{}/talk/vp/upload.nhn'.format(str(red.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        red.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

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
    print ("TAG ALL")
    try:
       red.sendMessage(msg)
    except Exception as error:
       print(error)
def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    red.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        red.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[ชื่อกลุ่ม {} ]\n╠".format(str(red.getGroup(to).name))
        arr = []
        no = 0 + 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[จำนวนคนที่แท็ก {} คน] ".format(str(len(mid)))
                except:
                    pass
        red.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        red.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def helpmessage():
    helpMessage =  "╔═══════════════" + "\n" + \
                  "║™❍✯͜͡SAMURI✯͜͡❂➣" + "\n " \
                  "║🗡.ข้างหน้าทั้งหมด" + "\n " \
                  "║🗡วัดรอบ➥เช็คความเร็วบอท" + "\n" \
                  "║🗡แทค➥แทคสมาชิกในกลุ่ม" + "\n" \
                  "║🗡เชคค่า➥เช็คการตั้งค่าบอท" + "\n" \
                  "║🗡เชคแอด➥เช็คคนสร้างกลุ่ม" + "\n" \
                  "║🗡ชื่อกลุ่ม➥แสดงชื่อกลุ่ม" + "\n" \
                  "║🗡รูปกลุ่ม➥แสดงรูปกลุ่ม" + "\n" \
                  "║🗡ไอดีกลุ่ม➥เช็คไอดีกลุ่ม" + "\n" \
                  "║🗡รายชื่อสมาชิก➥ชื่อสมาชิกกลุ่ม" + "\n" \
                  "║🗡ทีมงาน➥คนพัฒนา" + "\n" \
                  "║🗡คท @➥ส่งคอนแท็กคนที่แท็ก" + "\n" \
                  "║🗡ไอดี @➥ส่งMIDคนที่แท็ก" + "\n" \
                  "║🗡ชื่อ @➥ส่งชื่อคนที่แท็ก" + "\n" \
                  "║🗡ตัส @➥ส่งตัสคนที่แท็ก" + "\n" \
                  "║🗡ดิส @➥ส่งดิสคนที่แท็ก" + "\n" \
                  "║🗡วีดีโอ @➥ส่งวีดีโอคนที่แท็ก" + "\n" \
                  "║🗡ปก @➥ส่งปกคนที่แท็ก" + "\n" \
                  "║🗡แทคล่อง➥แท็กคนใส่ชื่อล่องหน" + "\n" \
                  "║🗡ไอดีล่อง➥หาmidคนใส่ชื่อล่องหน" + "\n" \
                  "║🗡คทล่อง➥ส่งคอนแท็กคนใส่ล่องหน" + "\n" \
                  "║🗡ตั้งเวลา➥เปิดหาคนซุ่ม" + "\n" \
                  "║🗡อ่าน➥แสดงชื่อคนซุ่ม" + "\n" \
                  "║™❍✯͜͡SAMURI✯͜͡❂➣" + "\n " \
                  "╚═══════════════"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   ".ข้างหน้าแทน-ทั้งหมด" + "\n " \
                         " " + "\n " \
                         "-เตะ @" + "\n" + \
                         "-ออก" + "\n" \
                         "-ยกเลิก" + "\n" + \
                         "-ลบรัน" + "\n" + \
                         "-โทร(เลข)" + "\n" + \
                         "-รายชื่อกลุ่ม" + "\n" + \
                         "-แทคล่อง" + "\n " + \
                         "-เปิดเข้า" + "\n" + \
                         "-ปิดเข้า" + "\n" + \
                         "-เปิดออก" + "\n" + \
                         "-เปิดออก" + "\n" + \
                         "-เปิดตอนรับ" + "\n" + \
                         "-ปิดต้อนรับ" + "\n" + \
                         "-เปิดคนออก" + "\n" + \
                         "-ปิดคนออก" + "\n" + \
                         "-เปิดคนเตะ" + "\n" + \
                         "-เปิดคนเตะ" + "\n" + \
                         "-เปิดแอด" + "\n" + \
                         "-ปิดแอด" + "\n" + \
                         "-ตั้งเข้า:" + "\n" + \
                         "-ตั้งออก:" + "\n" + \
                         "-ตั้งแอด:" + "\n" + \
                         "-เชคเข้า" + "\n" + \
                         "-เชคออก" + "\n" + \
                         "-เชคแอด" + "\n" + \
                         "-ลิ้ง" + "\n" + \
                         "-เปิดลิ้ง" + "\n" + \
                         "-ปิดลิ้ง" + "\n" + \
                         "-เปิดมุด" + "\n" + \
                         "-ปิดมุด" + "\n" + \
                         " " + "\n " + \
                         "**คำสั่งเฉพาะแอดมิน**"
    return helpTextToSpeech
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return

        if op.type == 5:
            if settings["autoAdd"] == True:
                red.findAndAddContactsByMid(op.param1)
            if settings["autoBlock"] == True:
                red.blockContact(op.param1)
            msgSticker = settings["messageSticker"]["listSticker"]["addSticker"]
            if msgSticker != None:
                sid = msgSticker["STKID"]
                spkg = msgSticker["STKPKGID"]
                sver = msgSticker["STKVER"]
                sendSticker(op.param1, sver, spkg, sid)
                red.sendMessage(op.param1,str(settings["comment"]))

        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = red.getGroup(op.param1)
            if settings["autoJoin"] == True:
                red.acceptGroupInvitation(op.param1)
                red.sendMessage(op.param1,str(settings["comment"]))
        
        if op.type == 15:
            print ("[ 15 ]  NOTIFIED LEAVE GROUP")
            if settings["bcommentOn"] == True:
                #if "{gname}" in settings['bye']:
                    #gName = red.getGroup(op.param1).name
                    #msg = settings['bye'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                msgSticker = settings["messageSticker"]["listSticker"]["leaveSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        if op.type == 19:
            if settings["ccommentOn"] == True:
                #if "{gname}" in settings['kick']:
                    #gName = red.getGroup(op.param1).name
                    #msg = settings['kick'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                msgSticker = settings["messageSticker"]["listSticker"]["kickSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        if op.type == 17:
            print ("[ 17 ]  NOTIFIED ACCEPT GROUP INVITATION")
            if settings["acommentOn"] == True:
                #if "{gname}" in settings['welcome']:
                    #gName = red.getGroup(op.param1).name
                    #msg = settings['welcome'].replace("{gname}", gName)
                    msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                    if msgSticker != None:
                        sid = msgSticker["STKID"]
                        spkg = msgSticker["STKPKGID"]
                        sver = msgSticker["STKVER"]
                        sendSticker(op.param2, sver, spkg, sid)
                msgSticker = settings["messageSticker"]["listSticker"]["welcomeSticker"]
                if msgSticker != None:
                    sid = msgSticker["STKID"]
                    spkg = msgSticker["STKPKGID"]
                    sver = msgSticker["STKVER"]
                    sendSticker(op.param1, sver, spkg, sid)
        
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                red.leaveRoom(op.param1)

        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != red.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#

#==============================================================================#
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != red.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    red.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
            if msg.contentType == 0:
                if text is None:
                    return
                if "/ti/g/" in msg.text.lower():
                    if settings["autoJoinTicket"] == True:
                        link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                        links = link_re.findall(text)
                        n_links = []
                        for l in links:
                            if l not in n_links:
                                n_links.append(l)
                        for ticket_id in n_links:
                            group = red.findGroupByTicket(ticket_id)
                            red.acceptGroupInvitationByTicket(group.id,ticket_id)
                            red.sendMessage(to, "มุดลิ้งเข้าไปในกลุ่ม👉 %s 👈 เรียบร้อยแล้ว" % str(group.name))
#==============================================================================#
                if msg.text in [".คำสั่ง","Help","help"]:
                    helpMessage = helpmessage()
                    red.sendMessage(to, str(helpMessage))
                if text.lower() == '.คำสั่ง2':
                  if msg._from in admin:
                         helpTextToSpeech = helptexttospeech()
                         red.sendMessage(to, str(helpTextToSpeech))
#==============================================================================#
                if msg.text.lower().startswith(".เตะ "):
                  if msg._from in admin:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                  for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                  for target in targets:
                        try:
                            redkickoutFromGroup(msg.to,[target])
                        except:
                            red.sendText(msg.to,"Error")
                if text.lower() == '.เชคค่า':
                    try:
                        ret_ = "╔════════════"
                        if settings["autoAdd"] == True: ret_ += "\n║ ระบบแอดออโต้ ✔"
                        else: ret_ += "\n║ ระบบแอดออโต้ ✘"
                        if settings["autoJoin"] == True: ret_ += "\n║ ระบบเข้ากลุ่มออโต้ ✔"
                        else: ret_ += "\n║ ระบบเข้ากลุ่มออโต้ ✘"
                        if settings["autoLeave"] == True: ret_ += "\n║ ระบบออกกลุ่มออโต้  ✔"
                        else: ret_ += "\n║ ระบบออกกลุ่มออโต้ ✘"
                        if settings["acommentOn"] == True: ret_ += "\n║ ระบบต้อนรับคนเข้ากลุ่ม ✔"
                        else: ret_ += "\n║ ระบบต้อนรับคนเข้ากลุ่ม ✘"
                        if settings["bcommentOn"] == True: ret_ += "\n║ ระบบแจ้งเตือนคนออกกลุ่ม ✔"
                        else: ret_ += "\n║ ระบบแจ้งเตือนคนออกกลุ่ม ✘"
                        if settings["ccommentOn"] == True: ret_ += "\n║ ระบบแจ้งเตือนคนเตะออกกลุ่ม ✔"
                        else: ret_ += "\n║ ระบบแจ้งเตือนคนเตะออกกลุ่ม ✘"
                        ret_ += "\n╚════════════"
                        red.sendMessage(to, str(ret_))
                    except Exception as e:
                        red.sendMessage(msg.to, str(e))

                if ".ยกเลิก" == msg.text.lower():
                  if msg._from in admin:
                         if msg.toType == 2:
                             group = red.getGroup(msg.to)
                             gMembMids = [contact.mid for contact in group.invitee]
                         for _mid in gMembMids:
                             red.cancelGroupInvitation(msg.to,[_mid])
                             red.sendMessage(to,"ยกเลิกค้างเชิญเสร็จสิ้น(。-`ω´-)")

                if text.lower() == '.ลบรัน':
                  if msg._from in admin:
                      gid = red.getGroupIdsInvited()
                      start = time.time()
                      for i in gid:
                          red.rejectGroupInvitation(i)
                      elapsed_time = time.time() - start
                      red.sendMessage(to, "กำลังดำเนินการ(。-`ω´-)")
                      red.sendMessage(to, "เวลาที่ใช้: %sวินาที(。-`ω´-)" % (elapsed_time))

                if ".โทร" in msg.text.lower():
                  if msg._from in admin:
                      if msg.toType == 2:
                          sep = text.split(" ")
                          strnum = text.replace(sep[0] + " ","")
                          num = int(strnum)
                          red.sendMessage(to, "เชิญเข้าร่วมการโทร(。-`ω´-)")
                      for var in range(0,num):
                          group = red.getGroup(to)
                          members = [mem.mid for mem in group.members]
                          red.acquireGroupCallRoute(to)
                          red.inviteIntoGroupCall(to, contactIds=members)
                if text.lower() == '.เปิดมุด':
                  if msg._from in admin:
                 settings["autoJoinTicket"] = True
                 red.sendMessage(to, "เปิดระบบมุดตามลิ้งเรียบร้อย")
                if text.lower() == '.ปิดมุด':
                  if msg._from in admin:
                 settings["autoJoinTicket"] = False
                 red.sendMessage(to, "ปิดระบบมุดลิ้งแล้ว")
                if text.lower() == '.ออก':
                  if msg._from in admin:
                      if msg.toType == 2:
                          ginfo = ref.getGroup(to)
                          try:
                              red.sendMessage(to, "บอทออกเรียบร้อย(。-`ω´-)")
                              red.leaveGroup(to)
                          except:
                             pass

                if ".ทีมงาน" == msg.text.lower():
                    msg.contentType = 13
                    red.sendMessage(to, "™❍✯͜͡SAMURI✯͜͡❂➣")
                    red.sendContact(to, "ub5abe828cd964292195c3c59d6322033")
                    red.sendContact(to, "u4db055855928255a6f53054d0915f196")
                    red.sendContact(to, "ue06dc4e846567f9c887ae7482e25c140")

                if msg.text in ["Me","me","คท","!me","!Me",".me",".Me",".คท"]:
                    red.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)

                if msg.text in ["Speed","speed","Sp","sp",".Sp",".sp",".Speed",".speed","\Sp","\sp","\speed","\Speed","สปีด"]:
                    start = time.time()
                    red.sendMessage(to, "การตอบสนองของบอท(。-`ω´-)")
                    elapsed_time = time.time() - start
                    red.sendMessage(msg.to, "[ %s Seconds ]\n[ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")

                if msg.text in ["ออน",".ออน","\ออน",".uptime",".Uptime"]:
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    red.sendMessage(to, "ระยะเวลาการทำงานของบอท(。-`ω´-)\n{}".format(str(runtime)))

                if msg.text in ["Tag","tagall","แทค","แท็ก","Tagall","tag",".แทค"]:
                    group = red.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        red.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                if msg.text.lower().startswith(".คท "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = red.getContact(ls)
                            mi_d = contact.mid
                            red.sendContact(msg.to, mi_d)

                if msg.text.lower().startswith(".ไอดี "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += ls
                        red.sendMessage(msg.to, str(ret_))

                if msg.text.lower().startswith(".ชื่อ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = red.getContact(ls)
                            red.sendMessage(msg.to, contact.displayName)

                if msg.text.lower().startswith(".ตัส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = red.getContact(ls)
                            red.sendMessage(msg.to, contact.statusMessage)

                if msg.text.lower().startswith(".ดิส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + red.getContact(ls).pictureStatus
                            red.sendImageWithURL(msg.to, str(path))

                if msg.text.lower().startswith(".ดิสวีดีโอ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + red.getContact(ls).pictureStatus + "/vp"
                            red.sendImageWithURL(msg.to, str(path))

                if msg.text.lower().startswith(".ปก "):
                    if red != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = "http://dl.profile.line-cdn.net/" + red.getProfileCoverURL(ls)
                                red.sendImageWithURL(msg.to, str(path))

                if text.lower() == '.แทคล่อง':
                    gs = red.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        red.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหน(。-`ω´-)")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        red.sendMessage(to, mc)

                if text.lower() == '.ไอดีล่อง':
                    gs = red.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        red.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหน(。-`ω´-)")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        red.sendMessage(to,mc)

                if text.lower() == '.คทล่อง':
                    gs = red.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        red.sendMessage(to, "ไม่มีคนใส่ชื่อร่องหน(。-`ω´-)")
                    else:
                        for ls in lists:
                            contact = red.getContact(ls)
                            mi_d = contact.mid
                            red.sendContact(to, mi_d)

#==============================================================================#
                if text.lower() == '.รีบูส':
                  if msg._from in admin:
                    red.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ..")
                    red.sendMessage(to, "Success Restarting.")
                    restartBot()
                if text.lower() == '.เชคแอด':
                    group = red.getGroup(to)
                    GS = group.creator.mid
                    red.sendContact(to, GS)
                if text.lower() == '.ไอดีกลุ่ม':
                    gid = red.getGroup(to)
                    red.sendMessage(to, "\n" + gid.id)
                if text.lower() == '.รูปกลุ่ม':
                    group = red.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    red.sendImageWithURL(to, path)
                if text.lower() == '.ชื่อกลุ่ม':
                    gid = red.getGroup(to)
                    red.sendMessage(to, "\n" + gid.name)
                if text.lower() == '.รายชื่อสมาชิก':
                    if msg.toType == 2:
                        group = red.getGroup(to)
                        ret_ = "╔══[ รายชื่อสมชิกกลุ่ม ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวนสมาชิก {} คน(。-`ω´-) ]".format(str(len(group.members)))
                        red.sendMessage(to, str(ret_))
                if text.lower() == '.รายชื่อกลุ่ม':
                  if msg._from in admin:
                      groups = red.groups
                      ret_ = "╔══[ รายชื่อกลุ่ม ]"
                      no = 0 + 1
                      for gid in groups:
                         group = red.getGroup(gid)
                         ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                         no += 1
                      ret_ += "\n╚══[ จำนวนกลุ่ม {} กลุ่ม(。-`ω´-)]".format(str(len(groups)))
                      red.sendMessage(to, str(ret_))

                if text.lower() == '.ลิ้ง':
                  if msg._from in admin:
                    if msg.toType == 2:
                        group = red.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = red.reissueGroupTicket(to)
                            red.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            red.sendMessage(to, "กรุณาเปิดลิ้งกลุ่มก่อนลงคำสั่งนี้ด้วยครับ(。-`ω´-)".format(str(settings["keyCommand"])))

                if text.lower() == '.เปิดลิ้ง':
                  if msg._from in admin:
                    if msg.toType == 2:
                        group = red.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            red.sendMessage(to, "ลิ้งกลุ่มเปิดอยู่แล้ว(。-`ω´-)")
                        else:
                            group.preventedJoinByTicket = False
                            red.updateGroup(group)
                            red.sendMessage(to, "เปิดลิ้งกลุ่มเรียบร้อย(。-`ω´-)")

                if text.lower() == '.ปิดลิ้ง':
                  if msg._from in admin:
                    if msg.toType == 2:
                        group = red.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            red.sendMessage(to, "ลิ้งกลุ่มปิดอยู่แล้ว(。-`ω´-)")
                        else:
                            group.preventedJoinByTicket = True
                            red.updateGroup(group)
                            red.sendMessage(to, "ลิ้งกลุ่มปิดเรียบร้อย(。-`ω´-)")
#=====================================================================#
                if text.lower() == '.เปิดแอด':
                  if msg._from in admin:
                      settings["autoAdd"] = True
                      red.sendMessage(to, "เปิดระบบออโต้แอด(。-`ω´-)")
                if text.lower() == '.ปิดแอด':
                  if msg._from in admin:
                      settings["autoAdd"] = False
                      red.sendMessage(to, "ปิดระบบออโต้แอด(。-`ω´-)")
                      
                if text.lower() == '.เปิดบล็อค':
                  if msg._from in admin:
                      settings["autoBlock"] = True
                      red.sendMessage(to, "เปิดระบบออโต้บล็อค(。-`ω´-)")
                if text.lower() == '.ปิดบล็อค':
                  if msg._from in admin:
                      settings["autoBlock"] = False
                      red.sendMessage(to, "ปิดระบบออโต้บล็อค(。-`ω´-)")  

                if text.lower() == '.เปิดเข้า':
                  if msg._from in admin:
                      settings["autoJoin"] = True
                      red.sendMessage(to, "เปิดระบบเข้ากลุ่มออโต้(。-`ω´-)")
                if text.lower() == '.ปิดเข้า':
                  if msg._from in admin:
                      settings["autoJoin"] = False
                      red.sendMessage(to, "ปิดระบบเข้ากลุ่มออโต้(。-`ω´-)")

                if text.lower() == '.เปิดออก':
                  if msg._from in admin:
                      settings["autoLeave"] = True
                      red.sendMessage(to, "เปิดระบบออกกลุ่มออโต้(。-`ω´-)")
                if text.lower() == '.ปิดออก':
                  if msg._from in admin:
                      settings["autoLeave"] = False
                      red.sendMessage(to, "ปิดระบบออกกลุ่มออโต้(。-`ω´-)")

                if msg.text.lower() ==  '.เปิดต้อนรับ':
                  if msg._from in admin:
                      settings['acommentOn'] = True
                      red.sendMessage(msg.to,"เปิดระบบต้อนรับสมาชิกเข้ากลุ่ม(。-`ω´-)")
                if msg.text.lower() ==  '.ปิดต้อนรับ':
                  if msg._from in admin:
                      settings['acommentOn'] = False
                      red.sendMessage(msg.to,"ปิดระบบต้อนรับสมาชิกเข้ากลุ่ม(。-`ω´-)")

                if msg.text.lower() == '.เปิดคนออก':
                  if msg._from in admin:
                      settings["bcommentOn"] = True
                      red.sendMessage(msg.to,"เปิดระบบแจ้งเตือนสมาชิกออกกลุ่ม(。-`ω´-)")
                if msg.text.lower() == '.ปิดคนออก':
                  if msg._from in admin:
                      settings['bcommentOn'] = False
                      red.sendMessage(msg.to,"ปิดระบบแจ้งเตือนสมาชิกออกกลุ่ม(。-`ω´-)")
                      
                if msg.text.lower() == '.เปิดคนเตะ':
                  if msg._from in admin:
                      settings["ccommentOn"] = True
                      red.sendMessage(msg.to,"เปิดระบบแจ้งเตือนคนเตะสมาชิกออกกลุ่ม(。-`ω´-)")
                if msg.text.lower() == '.ปิดคนเตะ':
                  if msg._from in admin:
                      settings['ccommentOn'] = False
                      red.sendMessage(msg.to,"ปิดระบบแจ้งเตือนคนเตะสมาชิกออกกลุ่ม(。-`ω´-)")

                if ".ตั้งเข้า:" in msg.text.lower():
                  if msg._from in admin:
                      c = msg.text.replace(".ตั้งเข้า:","")
                      if c in [""," ","\n",None]:
                         red.sendMessage(msg.to,"เกิดข้อผิดพลาด(。-`ω´-)")
                      else:
                         settings["acomment"] = c
                         red.sendMessage(msg.to,"ตั้งค่าข้อความตอนรับเสร็จสิ้น(。-`ω´-)")

                if ".ตั้งแอด: " in msg.text:
                  if msg._from in admin:
                      settings["addmsg"] = msg.text.replace(".ตั้งแอด: ","")
                      red.sendMessage(msg.to,"ตั้งค่าข้อความแอดเสร็จสิ้น(。-`ω´-)")

                if ".ตั้งออก:" in msg.text.lower():
                  if msg._from in admin:
                      c = msg.text.replace(".ตั้งออก:","")
                      if c in [""," ","\n",None]:
                          red.sendMessage(msg.to,"เกิดข้อผิดพลาด(。-`ω´-)")
                      else:
                         settings["bcomment"] = c
                         red.sendMessage(msg.to,"ตั้งค่าข้อความตอนรับออกเสร็จสิ้น(。-`ω´-)")

                if msg.text in [".เชคเข้า"]:
                  if msg._from in admin:
                      red.sendMessage(msg.to,"เช็คข้อความตอนรับล่าสุด(。-`ω´-)" + "\n\n➤" + str(settings["acomment"]))
                if msg.text in [".เชคออก"]:
                  if msg._from in admin:
                      red.sendMessage(msg.to,"เช็คข้อความตอนรับออกล่าสุด(。-`ω´-)" + "\n\n➤" + str(settings["bcomment"]))
                if msg.text in [".เชคแอด"]:
                  if msg._from in admin:
                      red.sendMessage(msg.to,"เช็คข้อความแอดล่าสุด(。-`ω´-)" + "\n\n➤" + str(settings["addmsg"]))
#=====================================================================#
                elif ".ประกาศกลุ่ม " in msg.text:
                    bc = msg.text.replace(".ประกาศกลุ่ม ","")
                    gid = red.getGroupIdsJoined()
                    for i in gid:
                        red.sendText(i,"======[ข้อความประกาศกลุ่ม]======\n\n"+bc+"\n\nBy: RED SAMURAi SELFBOT!!")
                    
                elif ".ประกาศแชท " in msg.text:
                    bc = msg.text.replace(".ประกาศแชท ","")
                    gid = red.getAllContactIds()
                    for i in gid:
                        red.sendText(i,"======[ข้อความประกาศแชท]======\n\n"+bc+"\n\nBy: RED SAMURAI SELFBOT!!")
                elif ".ส่งเสียงกลุ่ม " in msg.text:
                    bctxt = msg.text.replace(".ส่งเสียงกลุ่ม ", "")
                    bc = ("บาย...เรด..ซามูไร..เซลบอท")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = red.getGroupIdsJoined()
                    for manusia in n:
                        red.sendAudio(manusia, 'tts.mp3')

                elif ".ส่งเสียงแชท " in msg.text:
                    bctxt = msg.text.replace(".ส่งเสียงแชท ", "")
                    bc = ("บาย...เรด..ซามูไร..เซลบอท")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='th', slow=False)
                    tts.save('tts.mp3')
                    n = red.getAllContactIdsJoined()
                    for manusia in n:
                        red.sendAudio(manusia, 'tts.mp3')
                    
                elif text.lower() == '.ปฏิทิน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = "🌴ปฏิทินโดย SAMURAI SELFBOT🌴\n\n🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\n🍁" + hasil + "\n🍁 ที่ " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y')  + "\n🍁 เวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]" + "🌿🌸🍃🌸🍃🌸🍃🌸🍃🌸🍃🌸🌿" + "\n\nBY: ™❍✯͜͡RED™SAMURI✯͜͡❂➣ \nhttps://github.com/Redsamuri"
                    red.sendMessage(msg.to, readTime)

                elif "screenshotwebsite " in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        red.sendImageWithURL(to, data["result"])

                elif ".รูปภาพ" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            red.sendImageWithURL(to, str(path))
                elif ".รูปการ์ตูน" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            red.sendImageWithURL(to, str(path))
      
                elif ".ยูทูป" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        red.sendMessage(to, str(ret_))

                elif ".วีดีโอ " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "วีดีโอ ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        red.sendMessage(to, str(ret_))
                        
                elif ".หนัง" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "หนัง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        red.sendMessage(to, str(ret_))
                        
                elif ".เพลง" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + "เพลง ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        red.sendMessage(to, str(ret_))

                elif msg.text in [".เปิดแสกน"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    red.sendMessage(msg.to,"เปิดระบบแสกนคนอ่านอัตโนมัติ")
                elif msg.text in [".ปิดแสกน"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        red.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        red.sendMessage(msg.to, "ปิดระบบแสกนคนอ่านแล้ว")
#==============================================================================#
                if msg.text.lower().startswith(".พูด "):
                       sep = text.split(" ")
                       say = text.replace(sep[0] + " ","")
                       lang = 'th'
                       tts = gTTS(text=say, lang=lang)
                       tts.save("hasil.mp3")
                       red.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#
                if text.lower() == '.ตั้งเวลา':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                red.sendMessage(msg.to,"เปิดหาคนซุ่ม(。-`ω´-)")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            red.sendMessage(msg.to, "Set reading point:\n" + readTime)
                  
                if text.lower() == '.อ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            red.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = red.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            red.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        red.sendMessage(receiver,"กรุณาพิม [ตั้งเวลา] ก่อนลงคำสั่งนี้คับ(。-`ω´-)")
#==============================================================================#
        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["acommentOn"] == True:
             if op.param2 in redMID:
                 return
             dan = red.getContact(op.param2)
             tgb = red.getGroup(op.param1)
             sendMessageWithMention(op.param1, op.param2)
             red.sendMessage(op.param1,"สวัสดีจ้าคนมาใหม่\n 􀬁􀅳sparkle􏿿• 􂘁􀄗w􏿿􂘁􀄅e􏿿􂘁􀄌l􏿿􂘁􀄃c􏿿􂘁􀄏o􏿿􂘁􀄍m􏿿􂘁􀄅e􏿿 •􀬁􀅳sparkle􏿿\n🙏 {} 🙏\n       ❂➣👇 ᵀᴼ ᴳᴿᴼᵁᴾ👇 \n👉{}👈\n\n 􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿\n\n❂➣เข้ามาแล้วก็ทำตัวให้น่ารักๆน๊ะ\n🔇⏯อย่าลืมปิดแจ้งตื่นกันด้วยนะจ๊ะ\n🎙มีข้อสงสัยติดต่อถามได้ที่แอดมินนนะจ๊ะ\n\n".format(str(dan.displayName),str(tgb.name)))
             red.sendContact(op.param1, op.param2)
             red.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             red.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
             red.sendMessage(msg.to, None, contentMetadata={"PRDID":"a0768339-c2d3-4189-9653-2909e9bb6f58","PRDTYPE":"THEME","MSGTPL":"6"}, contentType=9)
        if op.type == 19:
           print ("MEMBER KICKOUT TO GROUP")
           if settings["ccommentOn"] == True:
             if op.param2 in redMID:
                 return
             dan = red.getContact(op.param2)
             tgb = red.getGroup(op.param1)
             red.sendMessage(op.param1,"▄︻̷̿ {} ┻̿═━一 ได้ทำการลบสมาชิกในกลุ่ม Σ(っﾟДﾟ；)っ ".format(str(dan.displayName)))
             red.sendContact(op.param1, op.param2)
             red.sendMessage(op.param1,"สเตตัส\n{}".format(str(dan.statusMessage)))
             red.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["bcommentOn"] == True:
             if op.param2 in redMID:
                 return
             dan = red.getContact(op.param2)
             tgb = red.getGroup(op.param1)
             red.sendMessage(op.param1,"🌠สมาชิกผู้มีเกียรตินามว่า🌠\n👉  {}  👈\nได้ออกจากกลุ่ม\n👉 {} 👈\nไปแล้ว  (｀・ω・´)👀ก็ขอให้โชคดีน๊ะจ๊ะ\n      􀼂􀅝church􏿿􀼂􀅜arbor􏿿﹏􀼂􀅞limo 1􏿿􀼂􀅟limo 2􏿿􀼂􀅠limo 3􏿿﹏􀼂􀅜arbor􏿿􀼂􀅝church􏿿\n\n".format(str(dan.displayName),str(tgb.name)))
             red.sendContact(op.param1, op.param2)
             red.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath)) 
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = red.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['จ๊ะเอ๋','รู้นะว่าแอบอยู่','เล่นซ่อนแอบกันเหรอ','คิดว่าเป็นนินจารึไง','ว่าไง','อ่านอย่างเดียวเลยนะ','ออกมาคุยหน่อย','ออกมาเดี๋ยวนี้']
                            sendMessageWithMention(op.param1, op.param2)
                            red.sendMessage(op.param1, str(random.choice(pref)) + '\n♪ ♬ ヾ(´︶`♡)ﾉ ♬ ♪')
                            red.sendContact(op.param1, op.param2)
                            sider = red.getContact(op.param2).picturePath
                            image = 'http://dl.profile.line.naver.jp'+sider
                            red.sendImageWithURL(op.param1, image)
                            msgSticker = settings["messageSticker"]["listSticker"]["readerSticker"]
                            if msgSticker != None:
                                sid = msgSticker["STKID"]
                                spkg = msgSticker["STKPKGID"]
                                sver = msgSticker["STKVER"]
                                sendSticker(op.param1, sver, spkg, sid)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = red.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	red.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print (" [™❍✯͜͡RED™SAMURI✯͜͡❂➣]  ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
