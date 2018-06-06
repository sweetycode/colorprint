#coding=utf8
import sys
import logging


class ColordLogger(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR

    isatty = sys.stdout.isatty()
    level = DEBUG

    @staticmethod
    def colord(c, msg, *args):
        message = msg if len(args) == 0 else (msg % tuple(args))
        if ColordLogger.isatty:
            return c + message + ColordLogger.ENDC
        else:
            return message

    @staticmethod
    def debug(msg, *args):
        if ColordLogger.level <= ColordLogger.DEBUG:
            print ColordLogger.colord(ColordLogger.OKBLUE, msg, *args)

    @staticmethod
    def info(msg, *args):
        if ColordLogger.level <= ColordLogger.INFO:
            print ColordLogger.colord(ColordLogger.OKGREEN, msg, *args)

    @staticmethod
    def warning(msg, *args):
        if ColordLogger.level <= ColordLogger.WARNING:
            print ColordLogger.colord(ColordLogger.WARN, msg, *args)

    @staticmethod
    def error(msg, *args):
        if ColordLogger.level <= ColordLogger.ERROR:
            print ColordLogger.colord(ColordLogger.FAIL, msg, *args)

