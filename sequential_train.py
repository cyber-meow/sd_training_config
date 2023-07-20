import argparse
import os
import subprocess


def run_scripts(script_name, dir_path):
    # Get all toml files in the directory
    config_files = [f for f in os.listdir(dir_path) if f.endswith('.toml')]

    for file in config_files:
        # Construct the full path to the config file
        config_file_path = os.path.join(dir_path, file)

        # Construct the command
        cmd = f'accelerate launch {script_name} --config_file {config_file_path}'

        # Run the command and wait for it to finish
        subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--script_name", type=str, required=True,
                        help="The name of the script to run, "
                        + "either 'train_network.py' or 'train_db.py'.")
    parser.add_argument("--dir_path", type=str, required=True,
                        help="The directory that contains the .toml files.")
    args = parser.parse_args()
    run_scripts(args.script_name, args.dir_path)
