# Integration of OpenNCP with National Connector #

## Introduction ##

This page describes how the OpenNCP Protocol Terminator common component can be integrated with the National Connector (NC).

## Background ##

Each country has their own implementation of the National Connector and therefore the way that OpenNCP connects with the NC will be different for each country. Therefore it is necessary to “inject” country-specific functionality into the OpenNCP Protocol Terminator module.

## Implementation ##

The following diagram shows the relevant OpenNCP classes and the classes that are country-specific.