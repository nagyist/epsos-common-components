# Protocol Terminators #

## JIRA ##

https://openncp.atlassian.net/browse/PT

## Mini Project Lead ##

Stefan Gustafsson


---


# Implementation #

## SCM location ##

https://code.google.com/p/epsos-common-components.protocolterminators

## Last update ##
### Version 0.1.1-SNAPSHOT ###

  * Client Connector (XCPD, XCA);
  * XDR Client Wave #1;
  * XCA Client Wave #1;
  * XCPD Client Wave #1;

## Server ##

  * _will be updated soon_

## Client ##

  * [Client Connector](Client_Connector.md)
  * [XCPD Client](XCPD_Client.md)
  * [XCA Client](XCAClient.md)
  * [XDR Client](XDR_Client.md)


---


# Build Instructions #

In order to correctly build this project, you first need to be aware that it depends on several other software components.
This building process, including the download and build of the required dependencies, will be explained bellow.

### 1. Protocol Terminator Main Project ###

First start by obtaining the Protocol Terminators source code with the following command:

```
git clone https://code.google.com/p/epsos-common-components.protocolterminators/```

In the Maven Project of Protocol Terminators you will find the following sub-projects:

  * **SERVER**
    * EpSOS CC WS Interface Declarations
    * EpSOS CC Web Services (based on IHE XCPD, XCA, XDR)
    * EpSOS CC IHE-XCPD Service Interface Implementation
    * EpSOS CC IHE-XCA Service Interface Implementation
    * EpSOS CC IHE-XDR Service Interface Implementation
  * **CLIENT**
    * EpSOS CC Web Services Client
      * EpSOS CC Client Connector
      * EpSOS CC IHE-XCPD Service Client
      * EpSOS CC IHE-XCA Service Client
      * EpSOS CC IHE-XDR Service Client

### 2. Audit Manager ###

This is project is a dependency for auditing purposes.
You can obtain it at the following link:

```
git clone https://code.google.com/p/epsos-common-components.auditmanager/```

### 3. Config Manager ###

This is project is a dependency for configuration management.

Please mind that this repository has a ConfigurationManager project, with the needed ConfigManager project inside it.

You can obtain it at the following link:

```
git clone https://code.google.com/p/epsos-common-components.configurationmanager/```

### 4. Terminology Services Access Manager ###

This is project is a dependency for handling terminologies.
You can obtain it at the following link:

```
git clone https://code.google.com/p/epsos-common-components.tsam/```

### 5. Security Manager ###

This is project is a dependency for handling security concerns.
You can obtain it at the following link:

```
git clone https://code.google.com/p/epsos-common-components.securitymanager/```

### 6. SRDC epSOS Consent Manager ###

This is project is a dependency for consent issues.
You can obtain it at the following link:

```
git clone https://code.google.com/p/epsos-common-components.consentmanager/```

### 7. SRDC epSOS Data Model ###

This is project is a dependency that contains several objects of the project used data model.
You can obtain it at the following link:

```
git clone https://code.google.com/p/epsos-common-components.datamodel/```

### 8. SRDC epSOS SAML Assertion Validator Implementation ###

This is project is a dependency for assertions validation.
You can obtain it at the following link:

```
git clone https://code.google.com/p/epsos-common-components.assertionvalidator/```

### 9. SRDC epSOS Utilities Package ###

This is project is a dependency that gathers several utilities.
You can obtain it at the following link:

```
git clone https://code.google.com/p/epsos-common-components.util/```

## Build Order ##

Please use the previous list in reverse order.