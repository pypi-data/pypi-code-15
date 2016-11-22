#coding:utf8
__author__ = 'root'
import traceback
from ObserverModel import Subject, Observer
import threading, time
from pyetc import load, reload, unload
import logging, os, sys
import time
from datetime import datetime

class threadReloadConfig(threading.Thread):
    LogSubjectObj = None

    def debugLog(self, msg):
        print("module:%s; time:%s; Msg:%s" %(__name__, datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"), msg+"\r\n"))
        #f = open(self.LogSubjectObj.basePath+ "/"+self.LogSubjectObj.debugFile, "a+")
        #f.write("module:%s; time:%s; Msg:%s" %(__name__, datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"), msg+"\r\n"))
        #f.close()

    def __init__( self, LogSubjectObjx):
        threading.Thread.__init__(self, name="threadReloadConfig")
        self.LogSubjectObj = LogSubjectObjx

    def var_dump(self, obj):
        import pprint
        output = pprint.saferepr(obj)
        return output

    def run(self):
        while True:
            # reload new log config
            self.LogSubjectObj.configuration = reload(self.LogSubjectObj.configuration)
            self.LogSubjectObj.data = dict(self.LogSubjectObj.config_all_default, **self.LogSubjectObj.configuration.config)

            # update ROOT-logger' configuration
            # do somethings

            # notification all observers
            self.LogSubjectObj.notifyObservers()
            timeSleep = 5
            if int(self.LogSubjectObj.data['monitorInterval']) > 5:
                timeSleep = int(self.LogSubjectObj.data['monitorInterval'])
            time.sleep(timeSleep)
            print("CurrentTime:"+datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))

class LogSubject(Subject):
    debugFile = "log4py.debug"
    reloadConfig = None
    daemonFlag = True
    timer_log = 0
    timer_interval = 3
    configuration = 0
    time_load_config = 0
    configurationFile = "log4p.py"
    basePath = ""
    t1 = 0
    config_all_default = {
        'debug' : False,
        'monitorInterval' : 0,
        'loggers' :{
            'root' :{
                'level' : "ERROR",
                'AppenderRef' : 'console'
            }
        },
        'appenders' :{
            'console' :{
                'type' :"console",
                'target' :"console",
                'PatternLayout' :"[%(levelname)s] %(asctime)s %(message)s"
            }
        }
    }

    def __init__(self):
        super(LogSubject, self).__init__()
        self.basePath = os.path.split(os.path.realpath( sys.argv[0]))[0]
        self.data = 0
        self.start()
        self.debugLog("Finish Start logger thread...")

    def debugLog(self, msg):
        if self.data['debug'] == False:
            return
        f = open(self.basePath+ "/"+self.debugFile, "a+")
        f.write("module:%s; time:%s; Msg:%s" %(__name__, datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"), msg+"\r\n"))
        f.close()

    def restart(self):
        self.debugLog("Enter to Restart")
        self.reloadConfig = threadReloadConfig(self)
        self.reloadConfig.setDaemon(True)
        self.reloadConfig.start()
        self.debugLog("Leave to Restart")

    def start(self):
        self.t1 = time.time()
        # check "configuration" file exist?
        if os.path.exists(self.basePath +"/"+ self.configurationFile):
            self.configuration = load(self.basePath +"/"+ self.configurationFile)
            self.data = dict(self.config_all_default, **self.configuration.config)
        else:
            self.debugLog("Configuration File Not Found!! Use default Configuration...")
            self.data = self.config_all_default

        self.reloadConfig = threadReloadConfig(self)
        self.reloadConfig.setDaemon(True)
        self.reloadConfig.start()

    def update_root(self):
        g_logger = logging.getLogger("root")
        pass

if __name__ == '__main__':
    log = LogSubject()
    log.start()
