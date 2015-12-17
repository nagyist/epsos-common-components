**The IHE-profiles project is currently disabled**

# description #

This sub-project contains wsdl's and xsd's from [ftp://ftp.ihe.net/](ftp://ftp.ihe.net/) pertaining to the web service profiles defined by [IHE](http://www.ihe.net/). The build file provided with this project will generate [JSR224](http://jcp.org/en/jsr/detail?id=224) compliant java classes for use with JAX-WS webservice clients and stubs.

# maven goals #

The goals needed to build the webservice clients and stubs is the general
```
mvn install
```

issued in the `ihe-profiles` directory.

The build can be memory intensive, and might require you to set the PermGen higher than default. On unix, use:

```
export MAVEN_OPTS="-Xmx512m -XX:MaxPermSize=256m"
```