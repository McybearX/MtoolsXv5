
pkg update -y
pkg install mpv -y
pkg install gtts
pkg install transgoogle
pkg install play-audio -y
pkg install python2 -y
pkg install python -y
pkg install pip -y
pkg install git -y
termux-setup-storage
cp bin/thunder.py $PREFIX/lib/python3.11
cp bin/thunder.py $PREFIX/lib/python3.10
cp bin/thunder.py $PREFIX/lib/python3.9
cp bin/thunder.py $PREFIX/lib/python3.8
cp bin/thunder.py $PREFIX/lib/python3.7
pip install gtts
pip install requests
pip install bs4
pip install futures
pip install mechanize
pip install ipaddress
pip install hashlib
#mv bin/thunder.py $PREFIX/lib/python3.10
python3 menu.py
