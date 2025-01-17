sudo cat "Types: deb\nURIs: http://mirrors.aliyun.com/ubuntu/\nSuites: noble noble-updates noble-security\nComponents: main restricted universe multiverse\nSigned-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg\n" > /etc/apt/sources.list.d/ubuntu.sources
sudo apt update
sudo apt install libltdl7-dev