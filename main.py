#from jaraco import clipboard
#clipboard.copy_html('<html><body><!--StartFragment--><span style="color: rgb(237, 92, 87); background-color: rgb(0, 255, 0); font-size: 18pt;">cec</span><span style="color: rgb(237, 92, 87); background-color: rgb(102, 102, 102); font-size: 18pt;">i es</span><span style="color: rgb(237, 92, 87); background-color: rgb(0, 255, 0); font-size: 18pt;">t </span><span style="color: rgb(81, 167, 249); background-color: rgb(0, 255, 0); font-size: 18pt;"><b>un t</b></span><span style="color: rgb(237, 92, 87); background-color: rgb(0, 255, 0); font-size: 18pt;"><b>est </b></span><span style="color: rgb(237, 92, 87); background-color: rgb(0, 255, 0);"><b>vfevvv </b></span><!--EndFragment--></body></html> ')
#clipboard.copy("voici un test pour voir")

print("hello")

#idée post: l'évolution de la gravure du moyen age aux micro puces
#projet: simulation de la machine de babbage

############################

import win32clipboard as cb

cb.OpenClipboard()

cb.EmptyClipboard()

HtmlFormat = cb.RegisterClipboardFormat("HTML Format")

rawText = "le texte a copier éùçà".encode("ANSI")
htmlFragment = '<div style="color: #d4d4d4;background-color: #1e1e1e;font-family: Consolas, \'Courier New\', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color: #569cd6;">import</span><span style="color: #d4d4d4;"> </span><span style="color: #c8c8c8;">win32clipboard</span><span style="color: #d4d4d4;"> </span><span style="color: #569cd6;">as</span><span style="color: #d4d4d4;"> </span><span style="color: #c8c8c8;">cb</span></div><br><div><span style="color: #c8c8c8;">cb</span><span style="color: #d4d4d4;">.</span><span style="color: #c8c8c8;">OpenCléùàçipboard</span><span style="color: #d4d4d4;">()</span></div><br><div><span style="color: #c8c8c8;">cb</span><span style="color: #d4d4d4;">.</span><span style="color: #c8c8c8;">EmptyClipboard</span><span style="color: #d4d4d4;">()</span></div></div>'

htmlFragment = ''
msg = open("message.txt", encoding="utf-8").read()
for c in msg:
    if c == "\n": 
        htmlFragment += "<br>"
        continue
    htmlFragment += '<span style="color: blue; background: red;">'
    htmlFragment += c+"</span>"

data = "Version:0.9\r\nStartHTML:0000000105\r\nEndHTML:"+ str(len(htmlFragment.encode("UTF-8")) + 34 + 36 + 105).zfill(10) +"\r\nStartFragment:0000000141\r\nEndFragment:"+str(len(htmlFragment.encode("utf-8"))+ 36 + 105).zfill(10)+"\r\n<html>\r\n"
data += "<body>\r\n<!--StartFragment-->" + htmlFragment + "<!--EndFragment-->"
data += "</body>\r\n</html> "

data = data.encode("UTF-8")


cb.SetClipboardData(HtmlFormat, data)
cb.SetClipboardData(cb.CF_TEXT, rawText)

cb.CloseClipboard()