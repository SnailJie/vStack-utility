#!/bin/bash
cd $1
/usr/share/apache-maven-3.3.9/bin/mvn -DskipTests clean install
