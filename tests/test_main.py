# !/usr/bin/python3
# -*- encoding: utf-8 -*-

'''
Created on 18 de ago de 2021
@module: main
@summary:
@author: Sandro Regis Cardoso | Software Engineer
@contact: src.softwareengineer@gmail.com
'''

from srvcresources.__init__ import __genesis_msg1__
from srvcresources.__init__ import __genesis_msg2__
from srvcresources.__init__ import __genesis_msg3__
from srvcresources.__init__ import __genesis_msg4__
from srvcresources.__init__ import __genesis_msg5__
from srvcresources.__init__ import __genesis_msg6__
from srvcresources.__init__ import __genesis_msg7__
from srvcresources.srvc_utils import __templogger_util__
from srvcresources.srvc_utils import __read_cfg__
from srvcresources.srvc_common import SrvcCommon
from logging import Logger


def test_do_bootstrap():
    log = None
    tlog = None
    try:
        tlog = __templogger_util__()
        assert(isinstance(tlog, Logger))
        # log notification
        tlog.info(__genesis_msg1__)

        # log reading mainsrvc config file
        tlog.info(__genesis_msg2__)
        mainsrvc_cfg = __read_cfg__(tlog)
        assert(isinstance(mainsrvc_cfg, dict))
        assert(mainsrvc_cfg.__len__() > 0)
        assert(mainsrvc_cfg['exec_main']['default'].__len__() > 0)
        assert(mainsrvc_cfg['logg']['handlers']['file_handler']['filename'].__len__() > 0)
        tlog.info(__genesis_msg3__)

        common_obj = SrvcCommon(tlog)
        # log parse event
        tlog.info(__genesis_msg4__)
        common_obj.set_global_cfg(mainsrvc_cfg)
        common_obj.set_parsed_vals(mainsrvc_cfg['exec_main'])

        # create new logger instance using config parameters
        log = common_obj.create_log_instance()
        assert(isinstance(log, Logger))
        return log
    except BaseException as excpt:
        tlog.exception(excpt)
        raise excpt
    finally:
        log.info(__genesis_msg5__)
        log.info(__genesis_msg6__)
        tlog.removeHandler(tlog.removeHandler('fh_tlog'))
        del(tlog)
        log.info(__genesis_msg7__)


def main():
    test_do_bootstrap()
    return


if __name__ == '__main__':
    main()
