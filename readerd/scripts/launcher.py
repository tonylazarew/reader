import argparse
import os
import signal
import sys
from twisted.python import log

def run():
    """Application entry point.
    """
    parser = argparse.ArgumentParser(description="readerd instance manager")
    parser.add_argument("path", metavar="PATH", nargs="?", default=".",
                        help="path to readerd.tac file")
    subparsers = parser.add_subparsers(help="sub-commands", dest="subcommand")

    # `start' command
    p = subparsers.add_parser("start", help="start readerd instance")

    # `stop' command
    p = subparsers.add_parser("stop", help="stop readerd instance")

    # `create' command
    p = subparsers.add_parser("create", help="create readerd setup")

    args = parser.parse_args()

    if not os.path.isdir(args.path):
        sys.stderr.write("path is not a directory: {}\n".format(args.path))
        return 1

    if args.subcommand == "start":
        return start(args.path)
    elif args.subcommand == "stop":
        return stop(args.path)
    elif args.subcommand == "create":
        from readerd.scripts import config
        return config.create(args.path)

def start(path, _test=False):
    """Start the readerd instance.
    """
    tac_file = os.path.join(path, "readerd.tac")
    if not os.path.exists(tac_file):
        if not _test:
            sys.stderr.write("unable to locate {}, exiting\n".format(tac_file))
        return 1
    os.chdir(path)
    sys.path.insert(0, os.path.abspath(os.getcwd()))

    argv = [
        "twistd",
        "--no_save",
        "--logfile=twistd.log",
        "--python=readerd.tac"
    ]
    sys.argv = argv

    if _test:
        # Do not try to start twistd during unittesting
        return 0

    # Starting twistd
    from twisted.scripts import twistd
    sys.stdout.write("readerd process is starting\n")
    twistd.run()

def stop(path, _test=False):
    """Stop the readerd instance.
    """
    pid_file = os.path.join(path, "twistd.pid")
    if not os.path.exists(pid_file):
        if not _test:
            sys.stderr.write("cannot find {}, ".format(pid_file))
            sys.stderr.write("is readerd really running here?\n")
        return 1
    pid = int(file(pid_file, "r").readline().strip())
    try:
        os.kill(pid, signal.SIGTERM)
    except OSError:
        sys.stderr.write("readerd process doesn't look alive, removing stale pid file\n")
    else:
        sys.stdout.write("readerd process was stopped\n")
