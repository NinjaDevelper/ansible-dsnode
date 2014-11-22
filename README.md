ansible-dsnode
==============

Ansible playbook for downstream-node deployment

To deploy a downstream-node cluster, you can use this ansible playbook.  It will install downstream-node, downstream-dash, and the appropriate back end services to run those applications.

First, install git and ansible, and clone the repository

```
$ sudo apt-get install git python-dev python-pip
$ pip install ansible
$ git clone https://github.com/wiggzz/ansible-dsnode
```

Then cd into the cloned repository and copy the hosts template.

```
$ cd ansible-dsnode
$ cp hosts.template hosts
```

Edit the hosts template ensuring that the hosts you configure are listed:

```
[nodes]
node1
node2
node3

[dbserver]
; it is assumed that the db server will be running as one
; of the nodes as well.  if this is not the case, the 
; database will not be configured correctly
node2

[loadbalancer]
node1

[dashboards]
node1
```

Replace `node1`, `node2` etc... with your ip or hostname for the nodes you want to configure.  If you need to modify any group_vars, such as setting the server_name, turning on or off ssl, and changing the paths to the ssl certificates, modify `group_vars/all.yml`

Then, run the playbook by issuing

```
$ ansible-playbook -i hosts site.yml
```

If your ssh host name is different from your current host name, or it needs sudo for configuration, add the `-u USER` option and/or the `--ask-sudo-pass` option, or specify it in the hosts template.  Please see the ansible documentation for further details.

