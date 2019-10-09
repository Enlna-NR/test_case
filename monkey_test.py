#第一步：安装app并开启
#第二步：杀掉app进程，并每次执行脚本前都杀死一次
#第三步：执行monkey命令，进行循环
#第四步：输出bugreport
import os,time


# flies = os.listdir("apk");
# print(flies)
# WORKSPACE = os.path.abspath(".")
#phone = "1192dcfc"


def install_apk():
    # root = os.getcwd()#获取当前目录
    # print(root)
    # name = 'com.iqiyi.comic.apk'#获取apk名
    # file_name = os.path.join(root,name)#拼接
    # print(file_name)
    # installApp = 'adb -s %s install -r %s'%(phone,file_name)#执行adb命令
    # print(installApp)
    # os.popen(installApp)#输出
    # print('install done')


    list = 'adb shell pm list packages'
    print(type(list))
    print(list)
    result= os.popen(list).read()
    # lo = str(os.system(list))
    # print(type(lo))
    print(result)
    if 'package:com.iqiyi.comic' not in result:
        files = os.listdir(r'.')#进入当前目录
        for file in files:
            if file[len(file) - 3:len(file)] == "apk":
                string = 'adb install ' + "\"" + file + "\""
                print(string)
                oss = os.system(string)
                print(oss)
    else:
        print('已安装apk')


def kill_app():
    stop = 'adb shell am force-stop com.iqiyi.comic'
    os.system(stop)
    print('已杀死进程')

def fullmonkey():
    kill_app()
    monkeycmd="adb shell monkey -p com.iqiyi.comic -s 12345 --throttle 300 --pct-touch 35 --pct-motion 10 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --bugreport -v 1000000"
    #跑完后--bugreport这个参数会自动保存log到sd卡根目录
    os.system(monkeycmd)



if __name__=='__main__':
    install_apk()
    for i in range(1):
        print("execute monkey ,loop = %s" % (i + 1))
        fullmonkey()
        time.sleep(30)
    print('the end')