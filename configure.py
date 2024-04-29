#!/usr/bin/python3

import sys
import os
import argparse
import stat

import pathlib
configure_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

cwd = os.getcwd()

# ========================================================= Process commandline
#                                                           arguments
arguments_help = "Configures a folder for a c++ cmake project."

parser = argparse.ArgumentParser(
    description=arguments_help,
    epilog=arguments_help
)

parser.add_argument(
    "-d", "--directory", default=None, type=str, required=True,
    help="The directory in which to setup the project"
)
parser.add_argument(
    "-n", "--app_name", default=None, type=str, required=True,
    help="The name of the application"
)

argv = parser.parse_args()  # argv = argument values

params: dict = {}
params["directory"] = argv.directory
params["app_name"] = argv.app_name

# ========================================================= Setup folder
#                                                           structure
# Setup main directory
if not os.path.isdir(params["directory"]):
    print('Directory "' + params["directory"] + '" Does not exist. Creating it.')
    os.makedirs(params["directory"])

template_dir = configure_path + "template_files"

for dir_path, sub_dirs, file_names in os.walk(template_dir):
    rel_dir_path = os.path.relpath(dir_path, template_dir)
    output_dir = params["directory"] + "/" + rel_dir_path

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for file_name in file_names:
        out_file_name = file_name.replace("tttAppNamettt", params["app_name"])
        in_file = open(dir_path + "/" + file_name, "r")
        out_file = open(output_dir + "/" + out_file_name, "w")
        lines = in_file.readlines()
        for line in lines:
            while line.find("tttAppNamettt") >= 0:
                line = line.replace("tttAppNamettt", params["app_name"])
            out_file.write(line)
        in_file.close()
        out_file.close()

        # Match permissions
        perms = os.stat(dir_path + "/" + file_name)
        os.chmod(output_dir + "/" + out_file_name, perms.st_mode)


