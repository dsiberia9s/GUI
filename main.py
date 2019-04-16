from m5ui import *
import utime as time
import random

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
    __Focusable = False
    __Function = None
    
    @property
    def X(self):
        return self.__X
    
    @property
    def X_(self):
        return self.__X_
    
    @X.setter
    def X(self, X):
        self.__X_ = self.__X
        self.__X = X
    
    @property
    def Y(self):
        return self.__Y
    
    @Y.setter
    def Y(self, Y):
        self.__Y = Y
    
    @property
    def Height(self):
        return self.__Height
  
    @Height.setter
    def Height(self, Height):
        self.__Height = Height
  
    @property
    def Width(self):
        return self.__Width
    
    @Width.setter
    def Width(self, Width):
        self.__Width = Width
    
    @property
    def Scene(self):
        return self.__Scene
    
    @Scene.setter
    def Scene(self, Scene):
        self.__Scene = Scene
    
    @property
    def Status(self):
        return self.__Status
    
    @Status.setter
    def Status(self, Status):
        self.__Status = Status
    
    @property
    def Time(self):
        return self.__Time
    
    @Time.setter
    def Time(self, Time):
        self.__Time = Time
    
    @property
    def NumberValue(self):
        return self.__NumberValue
    
    @property
    def NumberValue_(self):
        return self.__NumberValue_
    
    @NumberValue.setter
    def NumberValue(self, NumberValue):
        self.__NumberValue_ = self.__NumberValue
        self.__NumberValue = NumberValue
    
    @NumberValue_.setter
    def NumberValue_(self, NumberValue_):
        self.__NumberValue_ = NumberValue_
    
    @property
    def Name(self):
        return self.__Name
    
    @Name.setter
    def Name(self, Name):
        self.__Name = Name
    
    @property
    def Type(self):
        return self.__Type
    
    @Type.setter
    def Type(self, Type):
        self.__Type = Type
    
    @property
    def Label(self):
        return self.__Label
    
    @property
    def Label_(self):
        return self.__Label_
    
    @Label.setter
    def Label(self, Label):
        self.__Label_ = self.__Label
        self.__Label = Label
    
    @Label_.setter
    def Label_(self, Label_):
        self.__Label_ = Label_
    
    @property
    def TextValue(self):
        return self.__TextValue
    
    @property
    def TextValue_(self):
        return self.__TextValue_
    
    @TextValue.setter
    def TextValue(self, TextValue):
        self.__TextValue_ = self.__TextValue
        self.__TextValue = TextValue
    
    @TextValue_.setter
    def TextValue_(self, TextValue_):
        self.__TextValue_ = TextValue_
    
    @property
    def Focusable(self):
        return self.__Focusable
    
    @Focusable.setter
    def Focusable(self, Focusable):
        self.__Focusable = Focusable
  
    @property
    def Function(self):
        return self.__Function
  
    @Function.setter
    def Function(self, Function):
        self.__Function = Function
  
    def live(self):
        if self.__Type == "inputbox":
            return GUIInputbox(self)
        elif self.__Type == "human":
            return GUIHuman(self)
        elif self.__Type == "button":
            return GUIButton(self)

GUIRoll = []
GUIActiveScene = 0

def GUIPString(idSp, sp, srcStr):
    dstStr = ''
    cnt = 0
    for i in range(len(srcStr)):
        if srcStr[i] == sp:
            cnt += 1
        else:
            if cnt == idSp:
                dstStr += srcStr[i]
                
            elif cnt > idSp:
                break
    return dstStr

def GUILive():
    if buttonA.wasPressed():
        GUITab("<")
    if buttonC.wasPressed():
        GUITab(">")
    if buttonB.wasPressed():
        for i in range(0, len(GUIRoll)):
            if (GUIRoll[i]).Scene == GUIActiveScene and (GUIRoll[i]).Status == 1:
                (GUIRoll[i]).Status = 2
    for i in range(0, len(GUIRoll)):
        if (GUIRoll[i]).Scene == GUIActiveScene:
            GUIRoll[i] = (GUIRoll[i]).live()
            
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
            elif k == 'X.':
                lcd.rect(rX, rY, sk, sk, color=0xff0000)
                lcd.print(k[0], tX, tY, color=0xff0000)
                rgb.set_all(0xff0000)
            elif k == 'O.':
                lcd.rect(rX, rY, sk, sk, color=0x00ff00)
                lcd.print(k[0], tX, tY, color=0x00ff00)
                rgb.set_all(0x00ff00)
            elif k == '<b' or k == '>b':
                lcd.rect(rX, rY, sk, sk, color=0xffffff)
                lcd.print(k[0], tX, tY, color=0xffffff)
            elif k == 'A.':
                if caps == 1:
                    lcd.print(k[0].upper(), tX, tY, color=0x00ff00)
                else:
                    lcd.print(k[0].lower(), tX, tY, color=0x999999)
                lcd.rect(rX, rY, sk, sk, color=0x00ff00)
            else:
                lcd.rect(rX, rY, sk, sk, color=0x33ccff)
                lcd.print(k[0], tX, tY, color=0x33ccff)
                rgb.set_all(0x000000)
        else:
            lcd.rect(rX, rY, sk, sk, color=0x666666)
            if k == 'A.':
                if caps == 1:
                    lcd.print(k[0], tX, tY, color=0x00ff00)
                else:
                    lcd.print(k[0].lower(), tX, tY, color=0x999999)
            else:
                lcd.print(k[0], tX, tY, color=0x999999)
    if buttonB.wasPressed():
        wait(0.1)
        key = key + 1
        if key >= al:
            key = 0
    if buttonA.wasPressed():
        wait(0.1)
        key = key + rs
        if key >= al:
            key = key - (int(key / rs) * rs)
    if buttonC.wasPressed():
        wait(0.1)
        rgb.set_all(0x000000)
        k = keys[key]
        if len(k) == 1:
            return (keys[key].upper() if caps == 1 else keys[key].lower()), key, caps
        else:
            if k == 'A.':
                caps = 1 if caps == 0 else 0
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
    return '', key, caps

def GUIAttach(obj):
    inFocus = -1
    for i in range(0, len(GUIRoll)):
        if (GUIRoll[i]).Scene == obj.Scene and (GUIRoll[i]).Focusable:
            if (GUIRoll[i]).Status == 1:
                inFocus = i
            if obj.Status == 1:
                (GUIRoll[i]).Status = 0
    if inFocus == -1 and obj.Focusable:
        obj.Status = 1
    GUIRoll.append(obj)

def GUI(Name):
    for i in range(0, len(GUIRoll)):
        if GUIRoll[i].Name == Name:
            return GUIRoll[i]
            
def GUITab(Dir):
    inFocus = -1
    for i in range(0, len(GUIRoll)):
        if (GUIRoll[i]).Scene == GUIActiveScene:
            if (GUIRoll[i]).Status == 1:
                inFocus = i
    if Dir == ">":
        for i in range(inFocus + 1, len(GUIRoll)):
            if (GUIRoll[i]).Scene == GUIActiveScene and (GUIRoll[i]).Focusable:
                (GUIRoll[inFocus]).Status = 0
                (GUIRoll[i]).Status = 1
                return
    else:
        for i in range(inFocus, 0, -1):
            if (GUIRoll[i - 1]).Scene == GUIActiveScene and (GUIRoll[i - 1]).Focusable:
                (GUIRoll[inFocus]).Status = 0
                (GUIRoll[i - 1]).Status = 1
                return
              
def GUIScene(Number):
    global GUIActiveScene
    GUIActiveScene = Number
    lcd.fill(0x000000)

def GUIInputbox(obj):
    if obj.Status == 0:
        x = obj.X
        y = obj.Y
        width = obj.Width
        color = 0xcccccc
    elif obj.Status == 1:
        x = obj.X
        y = obj.Y
        width = obj.Width
        color = 0x33ccff
    else:
        lcd.fill(0x000000)
        x = 10
        y = 35
        width = 300
        color = 0x33ccff
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
                if k == 'backspace':
                    if cp > 0:
                        s = s[0:xp+cp-1] + s[xp+cp:]
                        k = 'left'
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
                    break
                if k == 'left':
                    lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0x000000)
                    if cp - 1 > 0:
                        cp = cp - 1
                    else:
                        xp = xp - 1 if xp - 1 >= 0 else xp
                if k == 'right':
                    lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0x000000)
                    if cp + 1 <= len(s[xp:xp+mx]):
                        cp = cp + 1
                    else:
                        xp = xp + 1 if xp + 1 + cp <= len(s) else xp
                for i in range(mx):
                    lcd.print('W', x + i * cw, y + 20, 0x000000)
                st = s[xp:xp+mx]
                stl = len(st)
                for i in range(stl):
                    lcd.print(st[i], x + i * cw, y + 20, 0xffffff)
            else:
                if time.ticks_us() - obj.Time >= 500000:
                    obj.Time = time.ticks_us()
                    if cs == 0:
                        lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0xffffff)
                        cs = 1
                    else:
                        lcd.line(x + cp * cw, y + 20 - 4, x + cp * cw, y + 20 + ch, 0x000000)
                        cs = 0
    return obj

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
    lcd.print(obj.Label, int(x - len(obj.Label) * cw / 3), int(y + r + 1 + tail + r + r / 2), 0xcccccc)
    if time.ticks_us() - obj.Time >= 400000:
        obj.Time = time.ticks_us()
        if obj.NumberValue >= len(obj.TextValue):
            obj.NumberValue = 0
        for i in range(0, cells):
            lcd.print("W", int(x - ch / 3), int(y - r * 3 - i * ch), 0x000000)
            if len(obj.TextValue) > 0:
                j = obj.NumberValue - i
                if j >= 0:
                    lcd.print(obj.TextValue[j], int(x - ch / 3), int(y - r * 3 - i * ch), random.randint(0x00ffcc, 0x00ffff))
        obj.NumberValue = obj.NumberValue + 1
    return obj

def GUIButton(obj):
    if obj.Status == 1:
        lcd.print(obj.Label, obj.X, obj.Y, 0x33ccff)
    elif obj.Status == 2:
        lcd.print(obj.Label, obj.X, obj.Y, 0xffd700)
        if obj.Function != None:
          obj.Function(obj)
        obj.Status = 1
    else:
        lcd.print(obj.Label, obj.X, obj.Y, 0xcccccc)
    return obj

def GUIRange(obj):
  if obj.Status == 1:
    pass
  elif obj.Status == 2:
    pass
  else:
    lcd.print(obj.Label, obj.X, obj.Y, 0xcccccc)
    
#########################################################
##################### GUI END ###########################
#########################################################

def myFunc(obj):
  speaker.tone(obj.NumberValue, 200)

obj = GUIObject()
obj.Name = "myFirstButton"
obj.Type = "button"
obj.NumberValue = 1000 # 1000 Hz
obj.Label = "Beep 1000 Hz"
obj.X = 10
obj.Y = 19
obj.Scene = 0
obj.Focusable = True
obj.Function = myFunc
GUIAttach(obj)
obj = None

obj = GUIObject()
obj.Name = "myFirstButton"
obj.Type = "button"
obj.NumberValue = 2000 # 2000 Hz
obj.Label = "Beep 2000 Hz"
obj.X = 10
obj.Y = 59
obj.Scene = 0
obj.Focusable = True
obj.Function = myFunc
GUIAttach(obj)
obj = None

lcd.fill(0x000000)
while True:
    GUILive()
    wait(0.001)