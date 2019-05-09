import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_packages(host):
    fping_package = host.package('fping')
    tmux2u_package = host.package('tmux2u')

    assert fping_package.is_installed
    assert tmux2u_package.is_installed
