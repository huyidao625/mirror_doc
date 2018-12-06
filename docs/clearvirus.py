#coding=utf-8
import os,codecs,re
def fuck_virus(path):
    newhtml = None
    try:
        with codecs.open(path,'r','gbk') as f:
            htmls = f.read()
            _virus = re.match('[\w\W]*(?P<v><SCRIPT Language=VBScript>[\w\W]+</SCRIPT>)[\w\W]*', htmls)
            if _virus:
                v =  _virus.group('v')
                newhtml = htmls.replace(v, '')
    except :
        with codecs.open(path,'r','utf-8') as f:
            htmls = f.read()
            _virus = re.match('[\w\W]*(?P<v><SCRIPT Language=VBScript>[\w\W]+</SCRIPT>)[\w\W]*', htmls)
            if _virus:
                v =  _virus.group('v')
                newhtml = htmls.replace(v, '')
        
    with codecs.open(path,'w','gbk') as f:
        if newhtml != None:
            f.write(newhtml)

for root,dirs,files in os.walk('build'):
    for i in files:
        if os.path.splitext(i)[1] == '.html':
            _virus_file = os.path.join(root,i)
            fuck_virus( _virus_file)
            
