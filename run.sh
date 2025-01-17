sudo sh -c 'echo "Types: deb
URIs: http://mirrors.aliyun.com/ubuntu/
Suites: noble noble-updates noble-security
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
" > /etc/apt/sources.list.d/ubuntu.sources'
sudo apt update
sudo apt install libltdl7-dev