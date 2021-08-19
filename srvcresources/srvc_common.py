# !/usr/bin/python3
# -*- encoding: utf-8 -*-

'''
Created on 7 de ago de 2021
@module: srvcresources.srvc_common
@summary:
@author: Sandro Regis Cardoso | Software Engineer
@contact: src.softwareengineer@gmail.com
'''

import argparse
import logging
from logging import config


class SrvcCommon(object):

    global_cfg = {}
    parsed_vals = []

    def __init__(self, tlog: logging):
        super(SrvcCommon, self).__init__()
        self.log = tlog
        del(tlog)
        return

    def set_global_cfg(self, globconf: dict):
        try:
            self.log.info("Setting global config parameters")
            self.global_cfg = globconf
            del(globconf)
            self.log.info("Done!")
        except BaseException as excpt:
            self.log.exception("Exception on global resources: %s" % excpt)

    def set_parsed_vals(self, mainsrvc_params: dict):
        try:
            self.log.info("%s will parse global config parameters " % (
                mainsrvc_params['srvc_name'])
            )
            progname = mainsrvc_params['srvc_name']
            desc = mainsrvc_params['description']
            cfg_acron1 = mainsrvc_params['cfg_acron1']
            cfg_acron2 = mainsrvc_params['cfg_acron2']
            hlp = mainsrvc_params['help']
            rqd = mainsrvc_params['required']
            deflt = mainsrvc_params['default']
            parse_vals = argparse.ArgumentParser(prog=progname,
                                                 description=desc)
            parse_vals.add_argument(cfg_acron1, cfg_acron2, help=hlp,
                                    required=rqd, default=deflt)
            argparse._sys.argv = []
            self.parsed_vals = parse_vals.parse_args()
            self.log.info("%s Parser finish it tasks" % progname)
        except BaseException as excpt:
            self.log.exception("Exception on global resources: %s" % excpt)

    def create_log_instance(self):
        try:
            self.log.info("Creating default logger instance")
            # set object logging parameters
            logsrvc = self.global_cfg['logg']
            config.dictConfig(logsrvc)
            # get log service name from yaml logg <root> parameter
            logger_srvcname = logsrvc['logger_name']
            # initialize instance of object logging parameters
            logger = logging.getLogger(logger_srvcname)
            return logger
        except BaseException as excpt:
            self.log.exception("Exception on create log instance: %s" % excpt)
