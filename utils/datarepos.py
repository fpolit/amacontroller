#!/usr/bin/env python3
#
# Python script to create 'ama' user and initialize
# amacontroller bare and no bare data repositories.

import pygit2
import argparser
import subprocess

def create_user(username, homedir):
    uid = 137
    subprocess.run(['useradd',
                    '-u', uid,
                    '-m', '-d', homedir,
                    username])

def create_sshkey(path: str, password: str = None):
    """
    Create a SSH key and save it to path, if no password is supplied,
    then a strong password is generated
    """


def main():

    parser = argparser.ArgumentParser(
        description="Create 'ama' user and initialize amacontroller data repositories",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('--home',
                        default='/var/lib/amacontroller',
                        description="ama home path")

    parser.add_argument('-d', '--data-repo',
                        dest='data_repo',
                        description="Path of data repository (default: (PARSED HOME VARIABLE)/data)")

    parser.add_argument('-b', '--bare-repo',
                        dest='bare_repo',
                        default='/etc/amacontroller/amadata.git',
                        description="Path of bare data repository")

    parser.add_argument('-n', '--no-create-user',
                        dest='no_create_user',
                        action='store_true',
                        description="Skip creating 'ama' user")

    sshkey_parser = parser.add_argument_group('SSH key of data repository')
    sshkey_parser = add_argument('-p', '--public-sshkey',
                                 dest='public_sshkey',
                                 description='Public SSH key (DEFAULT: SSH_KEY + .pub)')
    private_key_parser = sshkey_parser.add_mutually_exclusive_group(required=True)
    private_key_parser.add_argument('-s', '--ssh-key',
                                    dest='sshkey',
                                    description="private ssh key of data repository")
    private_key_parser.add_argument('-g', '--generate-ssh-key',
                                    dest='generate_ssh_key',
                                    action='store_true',
                                    description="Generate a new ssh key for data repository (LOCATION: AMA_HOME/.ssh/id_rsa_ama)")

    args = parser.parse_args()

    pygit2.init_repository(args.bare_repo, True)

    pygit2.clone
