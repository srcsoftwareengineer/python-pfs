#!/usr/bin/python3
# -*- encoding: utf-8 -*-

'''
Created on 18 de ago de 2021
@module: main
@summary:
@author: Sandro Regis Cardoso | Software Engineer
@contact: src.softwareengineer@gmail.com
'''

import time
import threading
import logging

from srvcresources.srvc_utils import __templogger_util__
from srvcresources.srvc_utils import __read_cfg__
from srvcresources.srvc_common import SrvcCommon

from srvcresources.__init__ import __genesis_msg1__
from srvcresources.__init__ import __genesis_msg2__
from srvcresources.__init__ import __genesis_msg5__
from srvcresources.__init__ import __genesis_msg6__
from srvcresources.__init__ import __genesis_msg7__


def do_bootstrap():
    try:
        tlog = __templogger_util__()
        # log notification
        tlog.info(__genesis_msg1__)
        # log reading mainsrvc config file
        tlog.info(__genesis_msg2__)
        mainsrvc_cfg = __read_cfg__(tlog)
        common_obj = SrvcCommon(tlog)
        common_obj.set_global_cfg(mainsrvc_cfg)
        common_obj.set_parsed_vals(mainsrvc_cfg['exec_main'])
        # create new logger instance using config parameters
        log = common_obj.create_log_instance()
        log.info(__genesis_msg5__)
        return log
    except BaseException as excpt:
        tlog.exception(excpt)
    finally:
        log.info(__genesis_msg5__)
        log.info(__genesis_msg6__)
        tlog.removeHandler(tlog.removeHandler('fh_tlog'))
        del(tlog)
        log.info(__genesis_msg7__)


def dispatcher(arg: list, log: logging):
    while arg['stop'] is not True:
        try:
            log.info("Dispatcher is waiting for instructions from MainSrvc...")
            time.sleep(4)
        except BaseException as excpt:
            log.exception(excpt)
        finally:
            NotImplemented


def main(*args, **kwargs):  # @UnusedVariable
    info = {'stop': False}
    log = do_bootstrap()
    thread = threading.Thread(target=dispatcher, args=(info, log))

    while True:
        try:
            log.info(__genesis_msg7__)
            time.sleep(3.75)
            if thread._started._flag is False:
                thread.start()
        except KeyboardInterrupt as keyexcpt:
            info['stop'] = True
            log.warning("Keyboard Interruption: %s" % keyexcpt)
            break
    thread.join()


if __name__ == '__main__':
    main()
