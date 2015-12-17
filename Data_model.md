# Data Model #

## Project Lead ##

SRDC


---


## Implementation ##

### SCM location ###

https://code.google.com/p/epsos-common-components.datamodel/


---


## Version 0.3.2-SNAPSHOT ##

### by ###
SPMS

### changes ###

  * fix: PatientDemographics
    * fix: get/set id doesn't perform only for ext. part of the id.

### Description ###
Please mind the version change for snapshot, as like in other projects, this was done so development can occur with no need for constant version update.

### Related Improvements ###

  * [PT-8](https://openncp.atlassian.net/browse/PT-8)


---


## Version 0.3.1 ##

### by ###
SPMS

### changes ###

  * new class: InvalidInput

### Description ###
This exceptions can be used in a Data Transformation Service, to announce the caller that the given input has invalid content.
Also Added new package to store exceptions.

Also this update includes a property date type update for standard purposes.


---


## Version 0.3.0 ##

### by ###
SPMS

### changes ###

  * new class: PatientId.
  * update class: PatientDemographics:
    * new property: idList;
    * remove property: secondaryID;
    * update property: int administrativeGender -> String administrativeGender;

### Description ###
This update relates to the need from some countries to have more that one patientId.

Also this update includes a property date type update for standard purposes.

### Related Improvements ###

  * [PT-8](https://openncp.atlassian.net/browse/PT-8)


---


## Version 0.2.0 ##

### by ###
SRDC

### Description ###
This was the base code (version) provided to the openNCP.