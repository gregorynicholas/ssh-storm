# ssh-storm

ssh-storm is a command line tool to manage your ssh connections.

<img src="https://raw.github.com/gregorynicholas/ssh-storm/master/ss.png">

## installation

    $ [sudo] pip install ssh-storm

or if you like 90s:

    $ [sudo] easy_install ssh-storm

or download add storm directory to the your `$PATH`. E.g.

    $ git clone git://github.com/gregorynicholas/ssh-storm.git
    $ export PATH=$PATH:`pwd`/storm/storm/bin/; ssh-storm

## getting started

### adding hosts

    $ ssh-storm add [-h]  [--id_file ID_FILE] name connection_uri

Where `-h`, `id_file` are optional arguments.

example:

    $ ssh-storm add my_vps root@emreyilmaz.me:22
    my_vps added to your ssh config. you can connect it by typing "ssh my_vps".

### modifying hosts

    $ ssh-storm edit [-h] [--id_file ID_FILE] name connection_uri

Where `-h`, `id_file` are optional arguments.

example:

    $ ssh-storm edit my_vps emre@emreyilmaz.me:2400
    "my_vps" updated successfully.

### deleting a single host

    $ ssh-storm delete name

example:

    $ ssh-storm delete my_vps
    success hostname "my_vps" deleted successfully.

### searching hosts
    $ ssh-storm search git
    Listing results for git:
      github -> emre@github.com:22


### listing hosts

    $ ssh-storm list
    Listing hosts:
      vps -> 22@emreyilmaz.me:22
      netscaler -> root@127.0.0.1:8081

### deleting all hosts

    $ ssh-storm delete_all
    all entries deleted.

## known issues

If you use zsh on a mac and get "command not found: storm" for main storm script, make sure you have storm in your PATH.

example:

    $ export PATH=$PATH:/usr/local/share/python/; ssh-storm

## connection_uri format

    - user@server:port
    - server:port
    - server

defaults for user -> $USER, port -> 22

/see <a href="https://github.com/gregorynicholas/ssh-storm/blob/master/storm/ssh_uri_parser.py">ssh_uri_parser</a> for further look.

## contributors

-   <a href="http://github.com/ras0ir">@ras0ir</a> - PKGBUILD for Archlinux and testing excessive ssh configs.</a>
-   <a href="http://github.com/benvand">@benvand</a>
-   <a href="http://github.com/Bengt">@Bengt</a>
-   <a href="http://github.com/henrysher">@henrysher</a>
-   <a href="http://github.com/playpauseandstop">@playpauseandstop</a>
