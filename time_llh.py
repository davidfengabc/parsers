from sbp.client.drivers.file_driver import FileDriver
from sbp.client.loggers.json_logger import JSONLogIterator
from sbp.client import Handler, Framer
from sbp.client.loggers.json_logger import JSONLogger
from sbp.navigation import SBP_MSG_BASELINE_NED, MsgBaselineNED, MsgPosLLH, MsgGPSTime
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Swift Navigation SBP Example.")
    parser.add_argument("file")
    args = parser.parse_args()


    with JSONLogIterator(open(args.file)) as iterator:
        for msg, data in next(iterator):
            if isinstance(msg, MsgBaselineNED) or isinstance(msg, MsgPosLLH) or isinstance(msg, MsgGPSTime):
                print(msg)


if __name__ == "__main__":
    main()