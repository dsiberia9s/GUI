from m5ui import *
import utime as time
import random
from m5mqtt import M5mqtt

clear_bg(0x111111)

rgb = RGB_Bar()
btnA = M5Button(name="ButtonA", text="ButtonA", visibility=False)
btnB = M5Button(name="ButtonB", text="ButtonB", visibility=False)
btnC = M5Button(name="ButtonC", text="ButtonC", visibility=False)

#########################################################
######################## GUI ############################
#########################################################

class GUIObject:
    __X = 0
    __Y = 0
    __Height = 0
    __Width = 0
    __Scene = 0
    __Status = 0
    __Time = 0
    __NumberValue = 0
    __NumberValue_ = __NumberValue
    __Name = ""
    __Type = ""
    __Label = ""
    __Label_ = __Label
    __TextValue = ""
    __TextValue_ = __TextValue
    __Focusable = 0
    __Function = None
    
    @property
    def X(self):
        return self.__X
    pass

    @property
    def X_(self):
        return self.__X_
    pass

    @X.setter
    def X(self, X):
        self.__X_ = self.__X
        self.__X = X
    pass

    @property
    def Y(self):
        return self.__Y
    pass

    @Y.setter
    def Y(self, Y):
        self.__Y = Y
    pass

    @property
    def Height(self):
        return self.__Height
    pass

    @Height.setter
    def Height(self, Height):
        self.__Height = Height
    pass

    @property
    def Width(self):
        return self.__Width
    pass

    @Width.setter
    def Width(self, Width):
        self.__Width = Width
    pass
    
    @property
    def Scene(self):
        return self.__Scene
    pass

    @Scene.setter
    def Scene(self, Scene):
        self.__Scene = Scene
    pass

    @property
    def Status(self):
        return self.__Status
    pass

    @Status.setter
    def Status(self, Status):
        self.__Status = Status
    pass

    @property
    def Time(self):
        return self.__Time
    pass

    @Time.setter
    def Time(self, Time):
        self.__Time = Time
    pass

    @property
    def NumberValue(self):
        return self.__NumberValue
    pass

    @property
    def NumberValue_(self):
        return self.__NumberValue_
    pass

    @NumberValue.setter
    def NumberValue(self, NumberValue):
        self.__NumberValue_ = self.__NumberValue
        self.__NumberValue = NumberValue
    pass

    @NumberValue_.setter
    def NumberValue_(self, NumberValue_):
        self.__NumberValue_ = NumberValue_
    pass

    @property
    def Name(self):
        return self.__Name
    pass

    @Name.setter
    def Name(self, Name):
        self.__Name = Name
    pass
    
    @property
    def Type(self):
        return self.__Type
    pass

    @Type.setter
    def Type(self, Type):
        self.__Type = Type
    pass

    @property
    def Label(self):
        return self.__Label
    pass

    @property
    def Label_(self):
        return self.__Label_
    pass

    @Label.setter
    def Label(self, Label):
        self.__Label_ = self.__Label
        self.__Label = Label
    pass

    @Label_.setter
    def Label_(self, Label_):
        self.__Label_ = Label_
    pass

    @property
    def TextValue(self):
        return self.__TextValue
    pass

    @property
    def TextValue_(self):
        return self.__TextValue_
    pass

    @TextValue.setter
    def TextValue(self, TextValue):
        self.__TextValue_ = self.__TextValue
        self.__TextValue = TextValue
    pass

    @TextValue_.setter
    def TextValue_(self, TextValue_):
        self.__TextValue_ = TextValue_
    pass

    @property
    def Focusable(self):
        return self.__Focusable
    pass

    @Focusable.setter
    def Focusable(self, Focusable):
        self.__Focusable = Focusable
    pass

    @property
    def Function(self):
        return self.__Function
    pass

    @Function.setter
    def Function(self, Function):
        self.__Function = Function
    pass
    
    def live(self):
        if self.__Type == "inputbox":
            return GUIInputbox(self)
            pass
        elif self.__Type == "human":
            return GUIHuman(self)
            pass
        elif self.__Type == "button":
            return GUIButton(self)
            pass
    pass
pass

GUIRoll = []
GUIActiveScene = 0

def GUIPString(idSp, sp, srcStr):
    dstStr = ''
    cnt = 0
    for i in range(len(srcStr)):
        if srcStr[i] == sp:
            cnt += 1
            pass
        else:
            if cnt == idSp:
                dstStr += srcStr[i]
                pass
            elif cnt > idSp:
                break
            pass
        pass
    return dstStr
pass

def GUILive():
    if buttonA.wasPressed():
        GUITab("<")
        pass
    if buttonC.wasPressed():
        GUITab(">")
        pass
    if buttonB.wasPressed():
        for i in range(0, len(GUIRoll)):
            if (GUIRoll[i]).Scene == GUIActiveScene and (GUIRoll[i]).Status == 1:
                (GUIRoll[i]).Status = 2
                pass
        pass
        pass
    for i in range(0, len(GUIRoll)):
        if (GUIRoll[i]).Scene == GUIActiveScene:
            GUIRoll[i] = (GUIRoll[i]).live()
            pass
    pass

def GUIKeyboard(key = 0, caps = 0):
    keys = ['~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '!', '@', '#', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '{', '}', '$', '%', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', ';', '"', '\'', '\\', '|', '*', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', '<', '>', '?', '(', ')', '+', '<.', 'X.', 'O.', ' ', '_', 'A.', '<b', '>b']
    al = len(keys)
    w = 320
    pY = 140
    sk = 20
    rs = int(w / sk)
    for i in range(0, al):
        r = int(i / rs)
        rX = i * sk - r * w
        rY = pY + r * sk
        tX = rX + 5
        tY = rY + 4
        k = keys[i]
        if i == key:
            if k == '<.':
                lcd.rect(rX, rY, sk, sk, color=0xffcc00)
                lcd.print(k[0], tX, tY, color=0xffcc00)
                rgb.set_all(0xffcc00)
                pass
            elif k == 'X.':
                lcd.rect(rX, rY, sk, sk, color=0xff0000)
                lcd.print(k[0], tX, tY, color=0xff0000)
                rgb.set_all(0xff0000)
                pass
            elif k == 'O.':
                lcd.rect(rX, rY, sk, sk, color=0x00ff00)
                lcd.print(k[0], tX, tY, color=0x00ff00)
                rgb.set_all(0x00ff00)
                pass
            elif k == '<b' or k == '>b':
                lcd.rect(rX, rY, sk, sk, color=0xffffff)
                lcd.print(k[0], tX, tY, color=0xffffff)
                pass
            elif k == 'A.':
                if caps == 1:
                    lcd.print(k[0].upper(), tX, tY, color=0x00ff00)
                    pass
                else:
                    lcd.print(k[0].lower(), tX, tY, color=0x999999)
                    pass
                lcd.rect(rX, rY, sk, sk, color=0x00ff00)
                pass
            else:
                lcd.rect(rX, rY, sk, sk, color=0x33ccff)
                lcd.print(k[0], tX, tY, color=0x33ccff)
                rgb.set_all(0x000000)
                pass
            pass
        else:
            lcd.rect(rX, rY, sk, sk, color=0x666666)
            if k == 'A.':
                if caps == 1:
                    lcd.print(k[0], tX, tY, color=0x00ff00)
                    pass
                else:
                    lcd.print(k[0].lower(), tX, tY, color=0x999999)
                    pass
                pass
            else:
                lcd.print(k[0], tX, tY, color=0x999999)
                pass
            pass
        pass
    if buttonB.wasPressed():
        wait(0.1)
        key = key + 1
        if key >= al:
            key = 0
            pass
        pass
    if buttonA.wasPressed():
        wait(0.1)
        key = key + rs
        if key >= al:
            key = key - (int(key / rs) * rs)
            pass
        pass
    if buttonC.wasPressed():
        wait(0.1)
        rgb.set_all(0x000000)
        k = keys[key]
        if len(k) == 1:
            return (keys[key].upper() if caps == 1 else keys[key].lower()), key, caps
        else:
            if k == 'A.':
                caps = 1 if caps == 0 else 0
                pass
            elif k == '<.':
                return 'backspace', key, caps
            elif k == 'X.':
                return 'esc', key, caps
            elif k == 'O.':
                return 'enter', key, caps
            elif k == '<b':
                return 'left', key, caps
            elif k == '>b':
                return 'right', key, caps
        pass
    return '', key, caps
pass

def GUIAttach(obj):
    inFocus = -1
    for i in range(0, len(GUIRoll)):
        if (GUIRoll[i]).Scene == obj.Scene and (GUIRoll[i]).Focusable:
            if (GUIRoll[i]).Status == 1:
                inFocus = i
                pass
            if obj.Status == 1:
                (GUIRoll[i]).Status = 0
                pass
            pass
    pass
    if inFocus == -1 and obj.Focusable:
        obj.Status = 1
    GUIRoll.append(obj)
pass

def GUI(Name):
    for i in range(0, len(GUIRoll)):
        if GUIRoll[i].Name == Name:
            return GUIRoll[i]
            pass
    pass
pass

def GUITab(Dir):
    inFocus = -1
    for i in range(0, len(GUIRoll)):
        if (GUIRoll[i]).Scene == GUIActiveScene:
            if (GUIRoll[i]).Status == 1:
                inFocus = i
                pass
    pass
    if Dir == ">":
        for i in range(inFocus + 1, len(GUIRoll)):
            if (GUIRoll[i]).Scene == GUIActiveScene and (GUIRoll[i]).Focusable:
                (GUIRoll[inFocus]).Status = 0
                (GUIRoll[i]).Status = 1
                return
                pass
        pass
        pass
    else:
        for i in range(inFocus, 0, -1):
            if (GUIRoll[i - 1]).Scene == GUIActiveScene and (GUIRoll[i - 1]).Focusable:
                (GUIRoll[inFocus]).Status = 0
                (GUIRoll[i - 1]).Status = 1
                return
                pass
        pass
        pass
pass

def GUIScene(Number):
    global GUIActiveScene
    GUIActiveScene = 1
    lcd.fill(0x000000)
pass

def GUIInputbox(obj):
    if obj.Status == 0:
        x = obj.X
        y = obj.Y
        width = obj.Width
        color = 0xcccccc
        pass
    elif obj.Status == 1:
        x = obj.X
        y = obj.Y
        width = obj.Width
        color = 0x33ccff
        pass
    else:
        lcd.fill(0x000000)
        x = 10
        y = 35
        width = 300
        color = 0x33ccff
        pass
    lcd.font(lcd.FONT_Ubuntu)
    lcd.print(obj.Label, x, y, color)
    lcd.font(lcd.FONT_Default)
    lcd.line(x, y + 40, x + width, y + 40, color)
    cw = 10
    ch = 16
    s = obj.TextValue
    mx = int(width / cw)
    st = s[-mx:]
    stl = len(st)
    xp = len(s) - stl
    
    for i in range(stl):
        lcd.print(st[i], x + i * cw, y + 20, 0xffffff)
        pass
    
    if obj.Status == 2:
        kc = 0
        caps = 0
        cs = 0
        cp = len(s[xp:]) if len(s[xp:]) < mx else mx
        while True:
            k, kc, caps = GUIKeyboard(kc, caps)
            if k != '':
                if len(k) == 1:
                    lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0x000000)
                    s = s[0:xp+cp] + str(k) + s[xp+cp:]
                    k = 'right'
                    pass
                if k == 'backspace':
                    if cp > 0:
                        s = s[0:xp+cp-1] + s[xp+cp:]
                        k = 'left'
                        pass
                    pass
                if k == 'esc':
                    lcd.clear()
                    obj.Status = 1
                    break
                if k == 'enter':
                    lcd.clear()
                    obj.Status = 1
                    obj.TextValue = s
                    if obj.Function != None:
                        obj.Function(obj)
                        pass
                    break
                if k == 'left':
                    lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0x000000)
                    if cp - 1 > 0:
                        cp = cp - 1
                        pass
                    else:
                        xp = xp - 1 if xp - 1 >= 0 else xp
                        pass
                    pass
                if k == 'right':
                    lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0x000000)
                    if cp + 1 <= len(s[xp:xp+mx]):
                        cp = cp + 1
                        pass
                    else:
                        xp = xp + 1 if xp + 1 + cp <= len(s) else xp
                        pass
                    pass
                for i in range(mx):
                    lcd.print('W', x + i * cw, y + 20, 0x000000)
                    pass
                st = s[xp:xp+mx]
                stl = len(st)
                for i in range(stl):
                    lcd.print(st[i], x + i * cw, y + 20, 0xffffff)
                    pass
                pass
            else:
                if time.ticks_us() - obj.Time >= 500000:
                    obj.Time = time.ticks_us()
                    if cs == 0:
                        lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0xffffff)
                        cs = 1
                        pass
                    else:
                        lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0x000000)
                        cs = 0
                        pass
                    pass
                pass
            pass
        pass
    return obj
pass

def GUIHuman(obj):
    r = 8
    tail = r * 2
    cw = 12
    ch = 14
    cells = 5
    color = 0xffffff
    if obj.Height == 0 or obj.Width == 0:
        obj.Height = (r + 1 + tail + r + int(r / 2)) - (r * 3 - cells * ch)
        obj.Width = len(obj.Label) * cw if len(obj.Label) * cw > r * 2 else r * 2
        pass
    x = obj.X + r
    y = obj.Y + obj.Height
    lcd.circle(x, y, r, color=color)
    lcd.circle(int(x - r / 3), int(y - r / 3), int(r / 5), color=0x33ccff)
    lcd.circle(int(x + 1 + r / 3), int(y - r / 3), int(r / 5), color=0x33ccff)
    lcd.line(x, y + r + 1, x, y + r + 1 + tail, color)
    lcd.line(x, int(y + r + 1 + r * 2 / 3), x - r, int(y + r + 1 + r * 2 / 3), color)
    lcd.line(x + 1, int(y + r + 1 + r * 2 / 3), x + r, int(y + r + 1 + r * 2 / 3), color)
    lcd.line(x, y + r + 1 + tail, x - r, y + r + 1 + tail + r, color)
    lcd.line(x, y + r + 1 + tail, x + r, y + r + 1 + tail + r, color)

    if obj.Label != obj.Label_:
        lcd.print(obj.Label_, int(x - len(obj.Label_) * cw / 3), int(y + r + 1 + tail + r + r / 2), 0x000000)
        obj.Label_ = obj.Label
        pass

    lcd.print(obj.Label, int(x - len(obj.Label) * cw / 3), int(y + r + 1 + tail + r + r / 2), 0xcccccc)
    if time.ticks_us() - obj.Time >= 400000:
        obj.Time = time.ticks_us()
        if obj.NumberValue >= len(obj.TextValue):
            obj.NumberValue = 0
            pass
        for i in range(0, cells):
            lcd.print("W", int(x - ch / 3), int(y - r * 3 - i * ch), 0x000000)
            if len(obj.TextValue) > 0:
                j = obj.NumberValue - i
                if j >= 0:
                    lcd.print(obj.TextValue[j], int(x - ch / 3), int(y - r * 3 - i * ch), random.randint(0x00ffcc, 0x00ffff))
                    pass
                pass
        pass
        obj.NumberValue = obj.NumberValue + 1
        pass
    return obj
pass

def GUIButton(obj):
    if obj.Status == 1:
        lcd.print(obj.Label, obj.X, obj.Y, 0x33ccff)
        pass
    elif obj.Status == 2:
        lcd.print(obj.Label, obj.X, obj.Y, 0xffd700)
        obj.Function(obj)
        obj.Status = 1
        pass
    else:
        lcd.print(obj.Label, obj.X, obj.Y, 0xcccccc)
        pass
    return obj
pass

#########################################################
##################### GUI END ###########################
#########################################################

MQTTConnection = None

ChatRoll = []

def MQTTSetup(obj):
    global MQTTConnection
    MQTTConnection = M5mqtt(GUI("MQTTAPIKey").TextValue, GUI("MQTTServerAddress").TextValue, int(GUI("MQTTServerPort").TextValue), GUI("MQTTUsername").TextValue, GUI("MQTTPassword").TextValue, 3000)
    MQTTConnection.subscribe("main", MQTTSubscription)
    MQTTConnection.start()
    GUIScene(1)
pass

def MQTTSubscription(topic_data):
    data = str(topic_data)
    name = GUIPString(0, ':', data)
    message = GUIPString(1, ':', data)
    GUI("human1").Label = name
    GUI("human1").TextValue = message
pass

def usrFunc(obj):
    GUI("human1").TextValue = "Goodbye!"
pass

def usrFunc2(objInputbox):
    GUI("human1").TextValue = objInputbox.TextValue
pass

# Scene 1

obj = GUIObject()
obj.Name = "MQTTServerAddress"
obj.Type = "inputbox"
obj.Label = "Server address:"
obj.TextValue = "m14.cloudmqtt.com"
obj.X = 10
obj.Y = 10
obj.Scene = 0
obj.Width = 145
obj.Focusable = True
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "MQTTServerPort"
obj.Type = "inputbox"
obj.Label = "Server port:"
obj.TextValue = "16318"
obj.X = 165
obj.Y = 10
obj.Scene = 0
obj.Width = 145
obj.Focusable = True
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "MQTTAPIKey"
obj.Type = "inputbox"
obj.Label = "API Key:"
obj.TextValue = "d93f9667-af39-406a-af6c-b3a68e890e4f"
obj.X = 10
obj.Y = 70
obj.Scene = 0
obj.Width = 300
obj.Focusable = True
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "MQTTUsername"
obj.Type = "inputbox"
obj.Label = "User name:"
obj.TextValue = "xiiwgtpp"
obj.X = 10
obj.Y = 130
obj.Scene = 0
obj.Width = 145
obj.Focusable = True
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "MQTTPassword"
obj.Type = "inputbox"
obj.Label = "Password:"
obj.TextValue = "aWoZ8e8nQdEu"
obj.X = 165
obj.Y = 130
obj.Scene = 0
obj.Width = 145
obj.Focusable = True
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "MQTTSetupButton"
obj.Type = "button"
obj.Label = "Start"
obj.X = 130
obj.Y = 210
obj.Scene = 0
obj.Focusable = True
obj.Function = MQTTSetup
GUIAttach(obj)
obj = None

# Scene 2

obj = GUIObject()
obj.Name = "human1"
obj.Type = "human"
obj.Label = "Jack"
obj.TextValue = "Hello, guys! My name is Jack"
obj.X = 50
obj.Y = 10
obj.Scene = 1
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "human2"
obj.Type = "human"
obj.Label = "William"
obj.TextValue = "My name is William. I'am from UK"
obj.X = 100
obj.Y = 10
obj.Scene = 1
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "human3"
obj.Type = "human"
obj.Label = "Daniel"
obj.TextValue = "Hi! I'am Daniel"
obj.X = 150
obj.Y = 10
obj.Scene = 1
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "button2"
obj.Type = "button"
obj.Label = "Button"
obj.X = 220
obj.Y = 100
obj.Scene = 1
obj.Focusable = True
obj.Function = usrFunc
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "NewMessage"
obj.Type = "inputbox"
obj.Label = "Your message:"
obj.TextValue = "hello"
obj.X = 10
obj.Y = 170
obj.Scene = 1
obj.Width = 300
obj.Focusable = True
obj.Function = usrFunc2
GUIAttach(obj)
obj = None

lcd.fill(0x000000)

while True:
    GUILive()
    wait(0.001)