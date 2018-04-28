# -*- coding: utf-8 -*-
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time,random,sys,json,codecs,threading,glob,re,urllib.request,urllib.error,urllib.parse,pickle,requests,base64,antolib,subprocess,unicodedata
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,timeit,atexit
import html5lib,shutil
import wikipedia,goslate
import youtube_dl, pafy, asyncio
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE()
#cl = LINE('Esz49nFgTyepKfF4zUV7.6s2jZdrOy8zaUkEfxHsR1W.r3Mpn9WdxWVf87SdXUJE7Qg4hkkoweOVUeUIAAA0grQ=')
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
wait = {
    "group":True,
    "autoblock":True,	
    "wblacklist":False,
    "dblacklist":False,
    "blacklist":{},
    "dblack":False,
    "commentBlack":{},
    "wblack":False,	
}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
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
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
bot1 = cl.getProfile().mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
admin=['udb07f5e1b807b625801f5ef2af08a2da',clMID]
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
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
       cl.sendMessage(msg)
    except Exception as error:
       print(error)	
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
 
def helpmessage():
    helpMessage = """
《ShengYeSeltBot》
【Help】【Wind:help】
【HelpTag】
【HelpKick】
【Wind:rebot】
【Runtime】
【Speed】
【Set】
【About】
【Wind:bye】
【Creator】
【Add On/Off】
【Join On/Off】
【Leave On/Off】
【Read On/Off】
【Inviteprotect On/Off】
【Reread On/Off】
【Qr On/Off】
【Qrjoin On/Off】
【Ck On/Off】
【Groupprotect On/Off】
【Kc On/Off】
【Ptt On/Off】
【Me】
【MyMid】
【MyName】
【MyBio】
【MyPicture】
【MyCover】
【Contact @】
【Mid @】
【Name @】
【Bio @】
【Picture @】
【Cover @】
【Friendlist】
【Gowner】
【Gurl】
【O/Curl】
【Lg】
【Gb】
【Ginfo】
【Ri @】
【Ri:mid】
【Tk @】
【Mk @】
【Vk @】
【Vk:mid】
【Nk Name】
【Kickall】
【Uk mid】
【NT Name】
【Zk】
【Zt】
【Zm】
【Cancel】
【Gcancel】
【Gn Name】
【Gc @】
【Inv mid】
【Ban @】
【Unban @】
【Clear Ban】
【Kill Ban】
【Killbanall】
【Zk】
【Banlist】
【Sc gid】
【Mc mid】
【Tagall】
【S N/F/R】
【R】
【F/Gbc】
【/invitemeto:】
【Op @】
【Deop @】
【Oplist】
"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""
【Ri @】
【Tk @】
【Mk @】
【Vk @】
【Gc @】
【Mid @】
【Name @】
【Bio @】
【Picture @】
【Cover @】
【Ban @】
【Unban @】
"""
    return helpMessageTag
def helpmessagekick():
    helpMessageKick ="""
【Ri @】
【Tk @】
【Mk @】
【Vk @】
【Vk:mid】
【Nk Name】
【Uk mid】
【Kill ban】
【Zk】
"""
    return helpMessageKick
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                cl.blockContact(op.param1)		
        if op.type == 13:
            if clMID in op.param3:
                G = cl.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)					
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "อย่าเปิดลิ้ง！")
                    cl.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param3])
                    time.sleep(0.15)
                    cl.kickoutFromGroup(op.param1,[op.param2])
            if clMID in op.param3:
                if settings["autoPtt"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.leaveGroup(op.param1)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print(("[19] กลุ่มชื่อ: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid:" + contact1.mid + "\n被踢者: " + contact2.displayName + "\nMid:" + contact2.mid ))
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kickContact"] == True:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
                        cl.sendMessage(op.param1, "คนเตะมีดังนี้！")
                        cl.sendContact(op.param1,op.param2)
                        time.sleep(0.1)
                        cl.sendMessage(op.param1, "ผู้ที่ถูกเตะมีดังนี้！")
                        cl.sendContact(op.param1,op.param3)
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        settings["blacklist"][op.param2] = True
                        time.sleep(0.1)
            else:
                if settings["kickContact"] == True:
                    cl.sendMessage(op.param1, "คนเตะมีดังนี้！")
                    cl.sendContact(op.param1,op.param2)
                    time.sleep(0.1)
                    cl.sendMessage(op.param1, "ผู้ที่ถูกเตะมีดังนี้！")
                    cl.sendContact(op.param1,op.param3)
                else:
                    pass
        if op.type == 24:
            print ("[ 24 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新配置文件")
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    cl.sendMessage(to, str(ret_))
            if msg.contentType == 13:
                if settings["contact"] == True:
                    #msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[ชื่อ]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[เข้าสู่ระบบ]:\n" + contact.statusMessage + "\n[โปรไฟล์]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[หน้าปก]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[ชื่อ]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[เข้าสู่ระบบ]:\n" + contact.statusMessage + "\n[โปรไฟล์]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[หน้าปก]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "ลิ้งโพส\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendMessage(msg.to,msg.text)
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if msg.text in ["Help","Wind:help"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendMessage(to, "My Creator:")
                    cl.sendContact(to, "udb07f5e1b807b625801f5ef2af08a2da")
                elif text.lower() == 'helptag':
                    helpMessageTag = helpmessagetag()
                    cl.sendMessage(to, str(helpMessageTag))
                elif text.lower() == 'helpkick':
                    helpMessageKick = helpmessagekick()
                    cl.sendMessage(to, str(helpMessageKick))
                elif text.lower() == 'creator':
                    cl.sendMessage(to, "My Creator:")
                    cl.sendContact(to, "udb07f5e1b807b625801f5ef2af08a2da")
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif "Ri:" in msg.text:
                    midd = text.replace("Ri:","")
                    cl.kickoutFromGroup(to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(to,[midd])
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "Mk " in msg.text:
                    Mk0 = text.replace("Mk ","")
                    Mk1 = Mk0.rstrip()
                    Mk2 = Mk1.replace("@","")
                    Mk3 = Mk2.rstrip()
                    _name = Mk3
                    gs = cl.getGroup(to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Kickall" in msg.text:
                    if settings["kickmeber"] == True:
                        if msg.toType == 2:
                            _name = msg.text.replace("Kickall","")
                            gs = cl.getGroup(to)
                            cl.sendMessage(to, "ปิดกลุ่ม...")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                pass
                            else:
                                for target in targets:
                                    if target in admin:
                                        pass
                                    else:
                                        try:
                                            cl.kickoutFromGroup(to, [target])
                                        except:
                                            pass
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "Vk:" in text:
                    midd = msg.text.replace("Vk:","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
                elif "Vk " in msg.text:
                        vkick0 = msg.text.replace("Vk ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(msg.to,[target])
                                    cl.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = cl.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            mc = sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to,mc)
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to, "🤔แน๊ะไม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to, mc)
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        cl.sendMessage(to, "🤗ไม่มีmidคนใส่ร่องหน🤗")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        cl.sendMessage(to,mc)
                elif text.lower() == 'zc':
                    gs = cl.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        cl.sendMessage(to, "🤔แน๊ะไม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(to, mi_d)
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    cl.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = cl.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ไม่พบ"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "沒有"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "[ข้อมูลกลุ่ม]"
                    ret_ += "\nชื่อที่แสดง : {}".format(str(group.name))
                    ret_ += "\nรหัสกลุ่ม : {}".format(group.id)
                    ret_ += "\nผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\nจำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\nจำนวนคำเชิญ : {}".format(gPending)
                    ret_ += "\nURL ของกลุ่ม : {}".format(gQr)
                    ret_ += "\nURL ของกลุ่ม : {}".format(gTicket)
                    ret_ += "\n[.]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "ยกเลิกแล้ว\nยกเลิกเวลา: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "ยกเลิกจำนวน:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower() == 'gcancel':
                    gid = cl.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "全部กลุ่ม邀請已取消")
                    cl.sendMessage(to, "取消時間: %s秒" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"ไม่สามารถใช้ภายนอกกลุ่มได้")
                elif text.lower().startswith('op '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.append(str(inkey))
                        cl.sendMessage(to, "เพิ่มสิทธิ์！")
                elif text.lower().startswith('deop '):
                        MENTION = eval(msg.contentMetadata['MENTION'])
                        inkey = MENTION['MENTIONEES'][0]['M']
                        admin.remove(str(inkey))
                        cl.sendMessage(to, "ลบสิทธิ์แล้ว！")
                elif text.lower() == 'oplist':
                    if admin == []:
                        cl.sendMessage(to, "ไม่มีอำนาจ")
                    else:
                        cl.sendMessage(to, "ต่อไปนี้เป็นผู้ตรวจสอบ")
                        mc = ""
                        for mi_d in admin:
                            mc += "◉ " + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc)
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"ชื่อ:\n" + contact.displayName + "\n\nmid:\n" + contact.mid + "\n\nข้อมูลส่วนตัว:\n" + contact.statusMessage + "\n\nโปรไฟล์ :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nหน้าปก :\n" + str(cu))
                        except:
                            cl.sendMessage(msg.to,"ชื่อ:\n" + contact.displayName + "\n\nmid:\n" + contact.mid + "\n\nข้อมูลส่วนตัว:\n" + contact.statusMessage + "\n\nหน้าปก:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif ("Ban " in msg.text):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes Banned")
                        except:
                                pass

                elif "Unban @" in msg.text:
                    if msg.toType == 2:
                        print("[Unban]ok")
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip()
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                        if targets == []:
                                cl.sendText(msg.to,"Not found")
                        else:
                                for target in targets:
                                    try:
                                        del wait["blacklist"][target]
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Target Unlocked")
                                    except:
                                        cl.sendText(msg.to,"Error")

                elif "Ban:" in msg.text:                      
                        nk0 = msg.text.replace("Ban:","")
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

                elif "Unban:" in msg.text:                      
                        nk0 = msg.text.replace("Unban:","")
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
                elif "Allban" in msg.text:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("Allban","")
                           gs = cl.getGroup(msg.to)
                           cl.sendMessage(msg.to,"Banned all")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                cl.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in admin:
                                       try:
                                           wait["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           cl.sentMessage(msg.to,"All members has been added ban.")
                elif 'ban:on' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               wait["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               cl.sendMessage(msg.to,"Succes added for the blacklist ")
                               print ("Banned User")
                           except:
                               cl.sendMessage(msg.to,"Contact Not Found")
										   
                elif msg.text.lower() == 'banlist':
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                                matched_list+=[str for str in gMembMids if str == tag]
                        cocoa = ""
                        for mm in matched_list:
                                cocoa += "�" +cl.getContact(mm).displayName + "\n"
                        cl.sendText(msg.to,cocoa + "รายชื่อผู้ที่ติดดำ")			
                elif msg.text in ["cb","ล้างดำ"]:
                    wait["blacklist"] = {}
                    cl.sendText(msg.to,"clear")		
                elif msg.text in [" Ban","ดำ"]:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact to ban")
                
                elif msg.text in ["Unban","ขาว"]:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact to ban")
                
                elif msg.text in ["Banlist","เชคดำ"]:
                    if wait["blacklist"] == {}:
                        cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                    else:
                        cl.sendText(msg.to,"Daftar Banlist􏿿")
                        mc = "[⎈]Blacklist [⎈]\n"
                        for mi_d in wait["blacklist"]:
                                mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                        cl.sendText(msg.to, mc + "")
                elif msg.text in ["Ban cek","Cekban"]:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                                matched_list+=[str for str in gMembMids if str == tag]
                        cocoa = "[⎈]Mid Blacklist [⎈]"
                        for mm in matched_list:
                                cocoa += "\n" + mm + "\n"
                        cl.sendText(msg.to,cocoa + "")						
                elif msg.text.lower() == 'kill':
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                                matched_list+=[str for str in gMembMids if str == tag]
                        if matched_list == []:
                                cl.sendText(msg.to,"ไม่มีสมาชิกที่ติดแบน")
                                return
                        for jj in matched_list:
                                try:
                                    cl.kickoutFromGroup(msg.to,[jj])
                                    print((msg.to,[jj]))
                                except:
                                    pass
                elif msg.text.lower().startswith("cover "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("copy "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            cl.cloneContactProfile(contact)
                            cl.sendMessage(msg.to, "😊😊")
                        except:
                            cl.sendMessage(msg.to, "😊😊")
                            
                elif text.lower() == 'restore':
                    try:
                        clProfile.displayName = str(myProfile["displayName"])
                        clProfile.statusMessage = str(myProfile["statusMessage"])
                        clProfile.pictureStatus = str(myProfile["pictureStatus"])
                        cl.updateProfileAttribute(8, clProfile.pictureStatus)
                        cl.updateProfile(clProfile)
                        cl.sendMessage(msg.to, "Berhasil restore profile")
                    except:
                        cl.sendMessage(msg.to, "Gagal restore profile")
                        									
                elif text.lower() == 'wind:bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            cl.sendMessage(to, "บ้ายบาย~(｡•́︿•̀｡)")
                            cl.leaveGroup(to)
                        except:
                            pass
                elif msg.text in ["Friendlist"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"「 รายชื่อเพื่อน 」\n"+ap+"จำนวน : "+str(len(anl)))
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(msg.to,"กำลังทดสอบ..")
                    elapsed_time = time.time() - start
                    cl.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'speed':
                    start = time.time()
                    cl.sendMessage(msg.to,"กำลังทดสอบ..")
                    elapsed_time = time.time() - start
                    cl.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'wind:rebot':
                    cl.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ...")
                    time.sleep(5)
                    cl.sendMessage(to, "รีสตาร์ทเสร็จสิ้น!")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "ระยะเวลาการทำงานของบอท {}".format(str(runtime)))
                elif text.lower() == 'youtube':
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ผลการค้นหา]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่ค้นพบ {} ]".format(len(datas))
                        cl.sendMessage(to, str(ret_))					
                elif "google " in msg.text.lower():
                    spl = re.split("google ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        if spl[1] != "":
                                try:
                                    if msg.toType != 0:
                                        cl.sendText(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    else:
                                        cl.sendText(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                                    resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                    text = "ผลการค้นหาจาก Google:\n\n"
                                    for el in resp.findAll("h3",attrs={"class":"r"}):
                                        try:
                                                tmp = el.a["class"]
                                                continue
                                        except:
                                                pass
                                        try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                        except:
                                                continue
                                        text += el.a.text+"\n"
                                        text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                    text = text[:-2]
                                    if msg.toType != 0:
                                        cl.sendText(msg.to,str(text))
                                    else:
                                        cl.sendText(msg.from_,str(text))
                                except Exception as e:
                                    print(e)						
#==================================================				
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "udb07f5e1b807b625801f5ef2af08a2da"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "n《เกี่ยวกับตัวคุณ》"
                        ret_ += "\nชื่อ : {}".format(contact.displayName)
                        ret_ += "\nกลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\nเพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\nบล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n《เกียบกับบอท》"
                        ret_ += "\nร่น: BOT TON Beta"
                        ret_ += "\nผู้สร้าง : {}".format(creator.displayName)
                        ret_ += "\n(´・ω・｀)"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "[ ตั้งค่า ]"
                        if settings["autoAdd"] == True: ret_ += "\nรับแอดออโต้✔"
                        else: ret_ += "\nรับแอดออโต้✘"
                        if wait["group"] == True: ret_ += "\nข้อความต้อนรับ✔"
                        else: ret_ += "\nข้อความต้อนรับ✘"
                        if settings["autoCancel"]["on"] == True:ret_+="\nยกเลิกเชิญกลุ่ม: " + str(settings["autoCancel"]["members"]) + " → ✔"
                        else: ret_ += "\ยกเลิกเชิญกลุ่ม ✘"						
                        if settings["autoJoin"] == True: ret_ += "\nเข้าร่วมออโต้ ✔"
                        else: ret_ += "\nเข้าร่วมออโต้ ✘"
                        if settings["autoJoinTicket"] == True: ret_ += "\nมุดลิ้ง ✔"
                        else: ret_ += "\nมุดลิ้ง ✘"
                        if settings["autoLeave"] == True: ret_ += "\nออกแชทรวม ✔"
                        else: ret_ += "\nออกแชทรวม ✘"
                        if settings["autoRead"] == True: ret_ += "\nอ่านออโต้ ✔"
                        else: ret_ += "\nอ่านออโต้ ✘"
                        if settings["protect"] == True: ret_ += "\nป้องกันลบ ✔"
                        else: ret_ += "\nป้องกันลบ ✘"
                        if settings["inviteprotect"] == True: ret_ += "\nป้องกันเชิญ✘ ✔"
                        else: ret_ += "\nป้องกันเชิญ✘"
                        if settings["qrprotect"] == True: ret_ += "\nป้องกันลิ้งค์ ✔"
                        else: ret_ += "\nป้องกันลิ้งค์ ✘"
                        if settings["contact"] == True: ret_ += "\nเช็คContact ✔"
                        else: ret_ += "\nเช็คContact ✘"
                        if settings["reread"] == True: ret_ += "\nอ่าน ✔"
                        else: ret_ += "\nอ่าน ✘"
                        if settings["detectMention"] == False: ret_ += "\nเปิดตอบกลับคนแทค ✔"
                        else: ret_ += "\nเปิดตอบกลับคนแทค ✘"
                        if settings["checkSticker"] == True: ret_ += "\nเช็คสติ๊ก ✔"
                        else: ret_ += "\nเช็คสติ๊ก ✘"
                        if settings["kickContact"] == True: ret_ += "\nลบด้วยContact ✔"
                        else: ret_ += "\nลบด้วยContact ✘"
                        if settings["autoPtt"] == True: ret_ += "\nออกกลุ่มออโต้ ✔"
                        else: ret_ += "\nออกกลุ่มออโต้ ✘"
                        ret_ += "\n"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "รับแอดออโต้ ✔")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "รับแอดออโต้ ✘")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "เข้าร่วมออโต้ ✔")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "เข้าร่วมออโต้ ✘")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "ออกแชทรวม ✔")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "ออกแชทรวม ✘")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    cl.sendMessage(to, "เชคContact ✔")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    cl.sendMessage(to, "เชคContact ✘")
                elif text.lower() == 'groupprotect on':
                    settings["protect"] = True
                    cl.sendMessage(to, "ป้องกัน ✔")
                elif text.lower() == 'groupprotect off':
                    settings["protect"] = False
                    cl.sendMessage(to, "ป้องกัน ✘")
                elif text.lower() == 'inviteprotect on':
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "ป้องกันเชิญ ✔")
                elif text.lower() == 'inviteprotect off':
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "ป้องกันเชิญ ✘")
                elif text.lower() == 'qr on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "ป้องกันURLของกลุ่ม ✔")
                elif text.lower() == 'qr off':
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "ป้องกันURLของกลุ่ม ✘")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "อ่าน ✔")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "อ่าน ✘")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "อ่านออโต้ ✔")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "อ่านออโต้ ✘")
                elif text.lower() == 'qrjoin on':
                    settings["autoJoinTicket"] = True
                    cl.sendMessage(to, "มุดลิ้ง ✔")
                elif text.lower() == 'qrjoin off':
                    settings["autoJoinTicket"] = False
                    cl.sendMessage(to, "มุดลิ้ง ✘")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "เปิดตอบกลับคนแทค ✔")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "เปิดตอบกลับคนแทค ✘")
                elif text.lower() == 'ck on':
                    settings["checkSticker"] = True
                    cl.sendMessage(to, "เช็คสติ๊กเกอร์ ✔")
                elif text.lower() == 'ck off':
                    settings["checkSticker"] = False
                    cl.sendMessage(to, "เช็คสติ๊กเกอร์✘")
                elif text.lower() == 'kc on':
                    settings["kickContact"] = True
                    cl.sendMessage(to, "ลบด้วยContact ✔")
                elif text.lower() == 'kc off':
                    settings["kickContact"] = False
                    cl.sendMessage(to, "ลบด้วยContact ✘")
                elif text.lower() == 'ptt on':
                    settings["autoPtt"] = True
                    cl.sendMessage(to, "ออกกลุ่มออโต้ ✔")
                elif text.lower() == 'ptt off':
                    settings["autoPtt"] = False
                    cl.sendMessage(to, "ออกกลุ่มออโต้ ✘")					
                elif text.lower() == 'group on':
                    wait["group"] = True
                    cl.sendMessage(to, "เปิดแจ้งเตือน ✔")					
                elif text.lower() == 'group off':
                    wait["group"] = False
                    cl.sendMessage(to, "ปิดเเจ้งเเตือนของคุณเเล้ว ✘")	
                elif "Gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                                else:
                                    cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    cl.sendText(msg.to,strnum + " สมาชิกในกลุ่มจะปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                cl.sendText(msg.to,"Value is wrong")
                        else:
                                cl.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[ชื่อที่แสดง]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[ข้อความสถานะ]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls + "\n"
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ ชื่อ ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ เข้าสู่ระบบ ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("mpicture "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendVideoWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif text.lower() == 'gowner':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'gid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[กลุ่มID : ]\n" + gid.id)
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ URL ของกลุ่ม ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "URL ของกลุ่มเปิด".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "URL ของกลุ่ม已เปิด")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "ปลดแบนเปิดURL ของกลุ่ม")
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")							
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "URL ของกลุ่ม")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "URL ของกลุ่ม")
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ไม่พบ"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ปิด"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "ข้อมูลกลุ่ม"
                    ret_ += "\nชื่อที่แสดง : {}".format(str(group.name))
                    ret_ += "\nรหัสกลุ่ม : {}".format(group.id)
                    ret_ += "\nผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\nจำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\nจำนวนคำเชิญ : {}".format(gPending)
                    ret_ += "\nURL ของกลุ่ม : {}".format(gQr)
                    ret_ += "\nURL ของกลุ่ม : {}".format(gTicket)
                    ret_ += "\n[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'gb':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "[รายชื่อสมาชิก]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n{}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n[จำนวน： {} คน]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'lg':
                        groups = cl.groups
                        ret_ = "[รายชื่อกลุ่ม]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n[จำนวน {} กลุ่ม]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "จำนวน {} คน".format(str(len(nama))))
                elif text.lower() == 'sn':
                    tz = pytz.timezone("Asia/Taipei")
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
                                cl.sendMessage(msg.to,"ตั้งค่าจุดอ่านแล้ว")
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
                            cl.sendMessage(msg.to, "ตังค่าจุดอ่าน:\n" + readTime)
                            
                elif text.lower() == 'sf':
                    tz = pytz.timezone("Asia/Taipei")
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
                    if msg.to not in read['readPoint']:
                        cl.sendMessage(msg.to,"已讀點已刪除")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        cl.sendMessage(msg.to, "ลบจุดอ่าน:\n" + readTime)
    
                elif text.lower() == 'sr':
                    tz = pytz.timezone("Asia/Taipei")
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
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        cl.sendMessage(msg.to, "อิย้า:\n" + readTime)
                    else:
                        cl.sendMessage(msg.to, "อ้าาา")
                        
                elif text.lower() == 'r':
                    tz = pytz.timezone("Asia/Taipei")
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
                        if list(read["ROM"][receiver].items()) == []:
                            cl.sendMessage(receiver,"[ คนที่อ่าน ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ คนที่อ่าน ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[อ่านเวลา ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        cl.sendMessage(receiver,"ไม่มีการตั้งค่าจุดอ่าน")
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"<嗯？你以為收回有用嗎？>\n%s\n<看我講出你收回什麼~>\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print(["收回訊息"])
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            msg = op.message
            if msg.text in ["Me","me",".me",".Me","คท"]:
                cl.sendText(msg.to,"😜เชคจัง กลัวบอทหลุดละสิ😂")
            if msg.text in ["sp","speed",".speed","/speed"]:
                cl.sendText(msg.to,"😜แรงครับแรงแล้ว😂")
            if msg.text in ["runtime","Runtime","/uptime","ออน"]:
                cl.sendText(msg.to,"จะล็อคเซลนานไปไหน")
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
          if wait["group"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus			
            cl.sendText(op.param1, " ยินดีต้อนรับ. เข้ามาแล้วก็อย่าลืมปิดแจ้งเตือนกันน่ะครับ" + cl.getContact(op.param2).displayName + " สู่กลุ่ม " + "👉" + str(ginfo.name) + "👈""\nหรือสนใจลงบอทป้องกันบอทแท็ก ติดต่อได้ที่Line ID :\nhttp://line.me/ti/p/18y6421FL-")			
# ----------------- NOTIFED MEMBER OUT GROUP
        if op.type == 15:
          if wait['group'] == True:
            if op.param2 in bot1:
                return
            cl.sendText(op.param1,"good Bye" + cl.getContact(op.param2).displayName + "รีบไปไหนอ่ะ. ไม่เป็นไรไว้เจอกันใหม่น่ะจ๊ะ")
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == False:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "ต้องการไร")
                                    sendMessageWithMention(to, contact.mid)
                                break
        if op.type == 55:
            print ("[ 55 ] ตรวจพบข้อความ")
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
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
