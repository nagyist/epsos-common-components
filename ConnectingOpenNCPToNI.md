# Introduction #

OpenNCP implements the software that is common for all epSOS Participating Nations (PNs). Each PN has to implement the missing functionality, including:
  * Patient consent management
  * Document retrieval from NI
  * Document submission to NI

# Protocol terminators #

The classes in the epsos-interface subproject of the protocolterminators repository includes the following interfaces that must be implemented nationally by each PN:
  * PatientSearchInterface: national part of the XCPD server, responsible for epSOS Identification Service.
  * DocumentSearchInterface: national part of the XCA server, responsible for epSOS Patient Service and epSOS Order Service
  * DocumentSubmitInterface: national part of the XDR server, responsible for epSOS Dispensation Service and epSOS Consent Service.

Please refer to the documentation of the interfaces provided in Java source code or Javadoc. Mockups of national implementations are provided as part of OpenNCP in classes PatientSearchMock, DocumentSearchMock, DocumentSubmitImpl.

Please also refer to the Wiki page [IntegrationOpenNCPwithNC](IntegrationOpenNCPwithNC.md) that describes in detail the proposed method for locating and loading the country-specific implementations into the OpenNCP.

# Policy Decision Point #

PNs must provide a national implementation of the PDP class (Policy Decision Point) in the consentmanager repository. The version included as part of OpenNCP always responds that access to the patient data is **not** allowed.