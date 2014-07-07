# Client for cloud balancer

```
git clone https://github.com/Soulou/msc-thesis-container-balancer-client
cd msc-thesis-container-balancer-client
virtualenv .
source bin/activate
pip install -r requirements.txt
```

# Command line

```
./client.py start <service>
./client.py stop <host> <id>
./client.py migrate <host> <id>
./client.py status
```
