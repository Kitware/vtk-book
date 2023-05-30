<!-- SPDX-FileCopyrightText: Copyright 2020 VTK Book Authors and Contributors -->
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# VTK Book

[![Documentation Status](https://readthedocs.org/projects/vtk-book/badge/?version=latest)](https://book.vtk.org/en/latest/?badge=latest)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Citing

When citing VTK in your scientific research, please mention the following work to support increased visibility and dissemination of our software:

> Schroeder, Will; Martin, Ken; Lorensen, Bill (2006), The Visualization Toolkit (4th ed.), Kitware, ISBN 978-1-930934-19-1

For your convenience here is a bibtex entry:

```bibtex
@Book{vtkBook,
  author    = "Will Schroeder and Ken Martin and Bill Lorensen",
  title     = "The Visualization Toolkit (4th ed.)",
  publisher = "Kitware",
  year      = "2006",
  isbn      = "978-1-930934-19-1",
}
```

## Build environment

To compile the document locally create a python virtual environment and install the required packages.
For example in Linux / MacOS:
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Use `make html` in this directory to build the documentation.
Open `_build/html/index.html` in your browser to inspect the result.

## License

The content of this repository is licensed under several licenses. We follow the [REUSE specification](https://reuse.software/) to indicate which license applies to the files specifically. Here are some general hints:

* The VTK Book content, including all text, figures, and code examples, is licensed under `CC BY 4.0`

* The website source code used to generate the page structure of the VTK Book website is licensed under `Apache-2.0`

For more details on the licenses, please have a look at the file headers or associated `*.license` files. The terms of all used licenses are located in the [LICENSES](https://github.com/Kitware/vtk-book/tree/master/LICENSES) directory.
