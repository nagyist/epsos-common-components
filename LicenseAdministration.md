# The use and consequences of the licenses in the project #

This project is developed under the ASLv2 and GPLv3 licenses. As the
GPLv3 is a strong copyleft license, some care has to be taken when
linking between the different components of this project.

In general, software libraries developed under ASLv2 can be used by
GPLv3 licensed applications while both retain their license terms (see
the [Apache text on GPL compatibility](http://www.apache.org/licenses/GPL-compatibility.html)). However, the other way around, the GPLv3
license will invoke the clauses set forth in
[section 10 of its license text](http://www.gnu.org/copyleft/gpl.html#section10):

> "10. Automatic Licensing of Downstream Recipients.

> Each time you convey a covered work, the recipient automatically
> receives a license from the original licensors, to run, modify and propagate
> that work, subject to this License. You are not responsible for
> enforcing compliance by third parties with this License."

Specifically, when using any of the miniprojects that are licensed under
the GPLv3, potential clients of these applications or libraries should
take special care to observe its license.

Also, the individual miniprojects are responsible for providing a list
of the licenses used by their respective components. This list should
reside in a file named `README` located at the root of the project,
alongside its `pom.xml` file.

# Tools #

Phil Hagelberg (Technomancy) has created a little script that hooks up
with the `pom.xml` of a project and lists the license of each of its
dependencies, as far as they can be found (i.e. they reside in one of
`LICENSE`, `LICENSE.txt`, `META-INF/LICENSE`, `META-INF/LICENSE.txt` or `license/LICENSE`).

The script is written in [clojure](http://clojure.org), a JVM
language. Get it [here](https://github.com/technomancy/lein-licenses)