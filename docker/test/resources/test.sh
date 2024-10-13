#!/bin/bash

if [ ! -d /app/build/reports/xunit/xml ]; then
    mkdir -p /app/build/reports/xunit/xml/
fi

if [ ! -d /app/build/reports/cover/xml ]; then
    mkdir -p /app/build/reports/cover/xml/
fi

export TESTS_DIR=/app/tests
export BUILD_DIR=/app/build/reports

# Ejecutar las pruebas y generar el informe de cobertura
pynose --with-xunit --xunit-file=$BUILD_DIR/xunit/xml/xunit.xml \
       --with-coverage --cover-xml --cover-xml-file=$BUILD_DIR/cover/xml/coverage.xml \
       --cover-html --cover-html-dir=$BUILD_DIR/html --cover-package=applicant -v $TESTS_DIR
