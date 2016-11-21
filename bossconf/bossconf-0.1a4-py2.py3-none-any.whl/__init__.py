""" cli/lib dispatcher """
import os
import sys
from bossconf import BossConf

def main(): pass

def main_cli():
    # args
    args = sys.argv

    if len(args) < 2:
        print 'BossConf needs 2 arguments: [conf_file_path, "lev1, lev2"]'
        exit(1)
    else:
        abs_conf_path = args[1]
        get_string = args[2]

    # check conf file path is abs
    if not os.path.isabs(abs_conf_path):
        print 'Path provided is not absolute ' + abs_conf_path
        exit(1)

    # check if conf file exists
    if os.path.isfile(abs_conf_path):

        # prep lookup str
        if ',' in get_string:
            get_string = get_strig.split(',')
        else:
            get_string = [get_string]

        # run BossConf
        conf_file_name = abs_conf_path.split('/')[-1]
        conf_dir_path = abs_conf_path.split('/')[:-1]
        if conf_file_name and conf_dir_path:
            print BossConf(conf_dir_path, conf_file_name).get(get_string)
    else:
        print 'File does not exist at ' + abs_conf_path
        exit(1)
