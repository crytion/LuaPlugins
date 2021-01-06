import wave
import math
import struct
ff=wave.open("morse.wav","w")
ff.setframerate(8000)
ff.setnchannels(1)
ff.setsampwidth(2)
 
def wv(t=0,f=0,v=0.5,wf=ff,sr=8000):
    '''
    t:写入时长
    f:声音频率
    v：音量
    wf：一个可以写入的音频文件
    sr：采样率
    '''
    tt=0
    dt=1.0/sr
    while tt<=t:
        s=math.sin(tt*math.pi*2*f)*v*32768 #采样，调节音量，映射到[-2^15,2^15)
        s=int(s)
        fd=struct.pack("h",s) #转换成8bit二进制数据
        wf.writeframes(fd) #写入音频文件
        tt+=dt #时间流逝
         
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher
 
def decrypt(message):
 
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
    return decipher
 
def main(msg):
    message = msg
    if u'\u0039' >= message >= u'\u0030' or u'\u005a' >= message >= u'\u0041' or u'\u007a'>= message >= u'\u0061': #判断是否只有数字字母
        li = encrypt(message.upper())
        print (li)
        mo = []
        for i in li:
            if i=="-":
                mo.append("2")
                mo.append("0")
            elif i == ".":
                mo.append("1")
                mo.append("0")
            elif i==" ":
                mo.append("3")
        print(mo)
        lo = []
        for i in mo:
            if i =="0" or i == "1":
                lo.append(1)
            elif i =="2" or i == "3":
                lo.append(3)
        print(lo)
        note= {"1":600,"2":600,"3":0,"0":0} #600是滴答正玄波频率，如更改2个都改
        for i in range(len(mo)):
            wv(lo[i]/17.0,note[mo[i]]) #改变17数值cw快慢
        ff.close()
    else:
        result = decrypt(message)
        print (result)
 
if __name__ == '__main__':
    main("123456789")