# !/usr/bin/python3
# -*- encoding: utf-8 -*-

'''
Created on 7 de ago de 2021
@module: srvcresources.srvc_utils
@summary:
@author: Sandro Regis Cardoso | Software Engineer
@contact: src.softwareengineer@gmail.com
'''
import yaml

import logging

from .__init__ import __project_name__, __srvc_name__, __repository__, \
    __version__, __author__, __contact__, __license__, __data_deploy__, \
    __country__
# , __genesis_msg1__, __genesis_msg2__


def __templogger_util__():
    '''
    docstring
    '''
    templog = None

    def mount_sector(sector_name: str):
        lastcursorposition = 185
        breakline = '\n'
        linediv = '#'
        title = '#\t\t\t\t\t\t\t\t\t\t%s' % sector_name
        while lastcursorposition > 1:
            linediv += '='
            lastcursorposition -= 1
        linediv += '#'
        sector_block = "%s%s%s%s%s%s" % (breakline, linediv, breakline,
                                         title, breakline, linediv)
        return sector_block

    try:
        # global templog
        templog = logging.getLogger('tlogger')
        templog.setLevel(logging.INFO)
        fh = logging.FileHandler('./logs/main_srvc.log')
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(name)-16s %(levelname)-8s \
    %(threadName)-20s %(funcName)-24s %(message)s", "%Y-%m-%dT%H:%M:%S%z")
        fh.setFormatter(formatter)
        templog.addHandler(fh)
        templog.info(">>>>>>> Starting component processes")
        templog.info(mount_sector("HEADER"))
        templog.warn("Using Temporary Logger Service for recording initial \
    events")
        # log project informations
        templog.info(__project_name__)
        templog.info(__repository__)
        templog.info(__license__)
        templog.info("Component name: %s" % __srvc_name__)
        templog.info(__version__)
        templog.info(__data_deploy__)
        templog.info(__author__)
        templog.info(__contact__)
        templog.info(__country__)
        templog.info(mount_sector("EVENTS"))
        return templog
    except BaseException as excpt:
        templog.exception(excpt)


def __read_cfg__(log: logging):
    '''
    @todo:    Recovery cfg_file (config file path and name) from database
    @author:  Sandro Regis Cardoso | Software Engineer
    '''
    try:
        path = './cfg'
        cfg_file = "%s/mainsrvc_cfg.yaml" % path
        with open(cfg_file, 'r', encoding='utf-8') as cfg_params:
            params_exec_main = yaml.load(cfg_params)
            return params_exec_main
    except (IOError, EOFError) as error:
        log.exception("Error opening or reading config file: %s"
                      % (error.args[-1]))
