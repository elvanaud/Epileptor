import win32clipboard as cb
import random
import sys

def copy_html(rawText, htmlFragment):
    cb.OpenClipboard()
    
    cb.EmptyClipboard()
    
    HtmlFormat = cb.RegisterClipboardFormat("HTML Format")
    
    data = "Version:0.9\r\nStartHTML:0000000105\r\nEndHTML:"+ str(len(htmlFragment.encode("UTF-8")) + 34 + 36 + 105).zfill(10) +"\r\nStartFragment:0000000141\r\nEndFragment:"+str(len(htmlFragment.encode("utf-8"))+ 36 + 105).zfill(10)+"\r\n<html>\r\n"
    data += "<body>\r\n<!--StartFragment-->" + htmlFragment + "<!--EndFragment-->"
    data += "</body>\r\n</html> "
    
    data = data.encode("UTF-8")
    
    cb.SetClipboardData(HtmlFormat, data)
    cb.SetClipboardData(cb.CF_TEXT, rawText.encode("ANSI"))
    
    cb.CloseClipboard()
    
#rawText = "le texte a copier éùçà".encode("ANSI")
#htmlFragment = '<div style="color: #d4d4d4;background-color: #1e1e1e;font-family: Consolas, \'Courier New\', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color: #569cd6;">import</span><span style="color: #d4d4d4;"> </span><span style="color: #c8c8c8;">win32clipboard</span><span style="color: #d4d4d4;"> </span><span style="color: #569cd6;">as</span><span style="color: #d4d4d4;"> </span><span style="color: #c8c8c8;">cb</span></div><br><div><span style="color: #c8c8c8;">cb</span><span style="color: #d4d4d4;">.</span><span style="color: #c8c8c8;">OpenCléùàçipboard</span><span style="color: #d4d4d4;">()</span></div><br><div><span style="color: #c8c8c8;">cb</span><span style="color: #d4d4d4;">.</span><span style="color: #c8c8c8;">EmptyClipboard</span><span style="color: #d4d4d4;">()</span></div></div>'

def randomHexColor():
    r = int(random.random()*256)
    g = int(random.random()*256)
    b = int(random.random()*256)
    return "#"+hex(r)[2:]+hex(g)[2:]+hex(b)[2:]
    
filePath = "message.txt"
if len(sys.argv) == 2:
    filePath = sys.argv[1]
htmlFragment = ''
msg = open(filePath, encoding="utf-8").read()
for c in msg:
    if c == "\n": 
        htmlFragment += "<br>"
        continue
    randSize = str(int(random.random()*(30-5)+5))
    htmlFragment += '<span style="color: '+randomHexColor()+'; background: '+ randomHexColor()+';font-size: '+ randSize+'px;">'
    htmlFragment += c+"</span>"

htmlFragment += '<audio controls><source src="https://raw.githubusercontent.com/elvanaud/Epileptor/main/message.wav" type="audio/wav"><source src="horse.mp3" type="audio/mpeg">Your browser does not support the audio element.</audio>'

copy_html(msg, htmlFragment)

##########################################
#from jaraco import clipboard
#clipboard.copy_html('<html><body><!--StartFragment--><span style="color: rgb(237, 92, 87); background-color: rgb(0, 255, 0); font-size: 18pt;">cec</span><span style="color: rgb(237, 92, 87); background-color: rgb(102, 102, 102); font-size: 18pt;">i es</span><span style="color: rgb(237, 92, 87); background-color: rgb(0, 255, 0); font-size: 18pt;">t </span><span style="color: rgb(81, 167, 249); background-color: rgb(0, 255, 0); font-size: 18pt;"><b>un t</b></span><span style="color: rgb(237, 92, 87); background-color: rgb(0, 255, 0); font-size: 18pt;"><b>est </b></span><span style="color: rgb(237, 92, 87); background-color: rgb(0, 255, 0);"><b>vfevvv </b></span><!--EndFragment--></body></html> ')
#clipboard.copy("voici un test pour voir")

print("Copied to clipboard !")

#idée post: l'évolution de la gravure du moyen age aux micro puces
#projet: simulation de la machine de babbage

############################