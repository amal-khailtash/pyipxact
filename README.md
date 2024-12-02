# pyipxact - Accellera IP-XACT Python Binding

Moving to xsData[^1] instead of PyXB[^2] that provides a cleaner Pythong interface using dataclasses.

Old PyXB version has been moved to `PyXB` directory.


# Directory Structure

```
src/
└── org
    ├── accellera
    │   ├── ipxact
    │   │   ├── v1685_2014
    │   │   └── v1685_2022
    │   │       ├── tgi
    │   │       └── ve
    │   └── spirit
    │       ├── v1_0
    │       ├── v1_1
    │       ├── v1_2
    │       ├── v1_4
    │       │   └── tgi
    │       ├── v1_5
    │       │   └── tgi
    │       └── 1685-2009
    │           ├── tgi
    │           └── ve
    │               ├── ams
    │               ├── core
    │               ├── pdp
    │               └── power
```

# Examples


# References

* [Accellera](https://accellera.org/)
  * [IP-XACT Working Group](https://accellera.org/activities/working-groups/ip-xact)
  * [IP-XACT Downloads](https://accellera.org/downloads/standards/ip-xact)
  * [IP-XACT User Guide](https://accellera.org/images/downloads/standards/ip-xact/IPXACT-2022_user_guide.pdf)
  * [XML Schemas](http://www.accellera.org/XMLSchema)
* xsData - Naive XML & JSON Bindings for python
  * [Docs](https://xsdata.readthedocs.io/en/latest/)
  * [github](https://github.com/tefra/xsdata)

[^1]: [xsData - Naive XML & JSON Bindings for python](https://github.com/tefra/xsdata)
[^2]: [PyXB: Python XML Schema Bindings](https://pyxb.sourceforge.net/)