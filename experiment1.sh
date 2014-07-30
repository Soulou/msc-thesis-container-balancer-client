#!/bin/bash

build=yes
if [ "x$1" = "x--no-rebuild" ] ; then
	build=no
fi

if [ $build = yes ] ; then
	./client.py stop --service service1
	./client.py stop --service service2
	./client.py stop --service service3

	# Service 1 - High consumption application 10 containers
	for i in `seq 1 1 10` ; do
		./client.py start --image soulou/msc-thesis-memory-http-service service1
	done

	# Service 2 - Medium consumption application 5 containers
	for i in `seq 1 1 5` ; do
		./client.py start --image soulou/msc-thesis-memory-http-service service2
	done

	# Service 3 - Low consumption application 3 containers
	for i in `seq 1 1 3` ; do
		./client.py start --image soulou/msc-thesis-memory-http-service service3
	done
fi

(echo "Service1 $(wrk -c 10 -d 1m http://service1.thesis.dev/100/300 | grep 'Requests/sec:')") &
(echo "Service2 $(wrk -c 10 -d 1m http://service2.thesis.dev/50/250 | grep 'Requests/sec:')") &
(echo "Service3 $(wrk -t 3 -c 30 -d 1m http://service3.thesis.dev/10/10 | grep 'Requests/sec:')") &

echo "Wait for wrk instances to stop"
wait
