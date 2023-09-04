import os
import sys
exts = {
    '.zip': ("-P '%s'", 'unzip %s "%s/%s" -d "%s/%s"'),
    '.rar': ("'-p%s'", 'rar x %s "%s/%s" "%s/%s"')  
}
passwd = ''
rdir = '.'
en = True

i = 1
while i<len(sys.argv):
    if sys.argv[i]=="-i":
        rdir = sys.argv[i+1]
        assert os.path.exists(rdir)
        if(rdir[-1]=='/'): rdir = rdir[:-1]
        i += 1
    elif sys.argv[i]=="-p":
        passwd = sys.argv[i+1]
        i += 1
    elif sys.argv[i]=="-zip":
        exts = {'.zip': exts['.zip']}
    elif sys.argv[i]=="-rar":
        exts = {'.rar': exts['.rar']}
    elif sys.argv[i]=="-h" or sys.argv[i]=="--help":
        en = False
        print('批量解压缩脚本')
        print('-'*20)
        print("例子：python3 unzip.py -i ./Downloads/Name -p 'yourPassword' -zip")
        print("例子：python3 unzip.py -i .")
        print('-'*20)
        print('-i 目标地址')
        print('-p 密码')
        print('-zip 只解压zip')
        print('-rar 只解压rar')
        
    else:
        en = False
        print('unexpected indent:'+sys.argv[i])
        print('using -h for help')
    i += 1


dirlist = os.listdir(rdir+'/')
if en:
    for di in dirlist:
        if os.path.isfile(di):
            #过滤后缀名
            for ext, met in exts.items():
                if di[-len(ext):].lower() == ext:
                    print(di)

                    #填入密码
                    pwtmp = ''
                    if passwd:
                        pwtmp = met[0] % passwd
        
                    #新建目录
                    if not os.path.exists(rdir+'/'+di[:-len(ext)]):
                        os.mkdir(rdir+'/'+di[:-len(ext)])

                    #解压
                    print(met[1] % (pwtmp, rdir, di, rdir, di[:-len(ext)]))
                    os.system(met[1] % (pwtmp, rdir, di, rdir, di[:-len(ext)]))

                    break
