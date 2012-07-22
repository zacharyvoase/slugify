# `slugify`

`slugify` is a generic slugifier utility, inspired by Django’s `slugify`
template filter, packaged as a standalone Python library and command-line
application.

## Installation

    % [sudo] pip install slugify # OR
    % [sudo] easy_install slugify


## Usage

Works out of the box for Latin-based scripts:

    >>> from slugify import slugify
    >>> slugify(u"C'est Noël !")
    u'cest-noel'
    >>> slugify(u"C'est Noël !", separator="_")
    u'cest_noel'

It will handle all unicode equivalences if (and only if) the optional
unidecode library is installed:

    % [sudo] pip install unidecode # OR
    % [sudo] easy_install unidecode

Then:

    >>> slugify(u"北亰")
    u'bei-jing'

More about it:
  - http://en.wikipedia.org/wiki/Unicode_equivalence;
  - http://pypi.python.org/pypi/Unidecode.

If you do have unidecode installed, but wish not to use it, use the
unicodedata_slugify fonction:

    >>> slugify(u"Héllø Wörld") # slugify() uses unidecode if it can
    u'hello-world'
    >>> unicodedata_slugify(u"Héllø Wörld") # this will more limited
    u'hell-world'

If you don't use unidecode, the result may vary according to your Python
implementation or system. unidecode brings a richer equivalence and
a more consistent cross plateform output:

    >>> unicodedata_slugify(u"Héllø Wörld") # on Ubuntu 12.04 and Python 2.7
    u'hell-world'
    >>> unidecode_slugify(u"Héllø Wörld")
    u'hello-world'

If ne case you wish to keep the non ASCII caracters "as-is", use
unicode_slugify():

    >>> print unicode_slugify(u"C'est Noël !")
    cest-noël

### Command-line

    % echo "Héllø Wörld" | slugify
    hello-world

## License

The parts of this application that I wrote are released into the public domain
via [The Unlicense](http://unlicense.org/).

The slugifying routine is derived from Django, and as such is BSD-licensed:

> Copyright (c) Django Software Foundation and individual contributors.
> All rights reserved.
>
> Redistribution and use in source and binary forms, with or without modification,
> are permitted provided that the following conditions are met:
>
>     1. Redistributions of source code must retain the above copyright notice,
>        this list of conditions and the following disclaimer.
>
>     2. Redistributions in binary form must reproduce the above copyright
>        notice, this list of conditions and the following disclaimer in the
>        documentation and/or other materials provided with the distribution.
>
>     3. Neither the name of Django nor the names of its contributors may be used
>        to endorse or promote products derived from this software without
>        specific prior written permission.
>
> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
> ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
> WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
> DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
> ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
> (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
> LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
> ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
> (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
> SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
