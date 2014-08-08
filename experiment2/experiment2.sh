#!/bin/bash

wrk -c 10 -d 2m http://service1.thesis.dev/100/300 > /dev/null &
wrk -c 10 -d 2m http://service2.thesis.dev/50/250 > /dev/null &
wrk -t 3 -c 30 -d 2m http://service3.thesis.dev/10/10 > /dev/null &

sleep 1

build=yes
if [ "x$1" = "x--no-rebuild" ] ; then
	build=no
fi

if [ $build = yes ] ; then
	./client.py stop --service service1
	./client.py stop --service service2
	./client.py stop --service service3

	# Service 1 - High consumption application 10 containers
	for i in `seq 1 1 4` ; do
		./client.py start --image soulou/msc-thesis-memory-http-service service1
		sleep 5
	done

	# Service 2 - Medium consumption application 5 containers
	for i in `seq 1 1 4` ; do
		./client.py start --image soulou/msc-thesis-memory-http-service service2
		sleep 5
	done

	# Service 3 - Low consumption application 3 containers
	for i in `seq 1 1 2` ; do
		./client.py start --image soulou/msc-thesis-memory-http-service service3
		sleep 5
	done
fi

echo "Wait for wrk instances to stop"

killall wrk
wait

(echo "Service1 $(wrk -c 10 -d 2m http://service1.thesis.dev/100/300 | grep 'Requests/sec:')") &
(echo "Service2 $(wrk -c 10 -d 2m http://service2.thesis.dev/50/250 | grep 'Requests/sec:')") &
(echo "Service3 $(wrk -t 3 -c 30 -d 2m http://service3.thesis.dev/10/10 | grep 'Requests/sec:')") &

wait
