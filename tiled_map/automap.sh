#!/bin/bash

for i in $(ls -X *.tmx)
do
	echo "$i"
	python converter "$i" doors=^ entities=?*
done
