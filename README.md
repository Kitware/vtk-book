# VTK Book  

[![Documentation Status](https://readthedocs.org/projects/vtk-book/badge/?version=latest)](https://book.vtk.org/en/latest/?badge=latest)

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
