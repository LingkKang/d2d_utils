
Set up the virtual environment

``` PowerShell
python -m venv env
```

**Activate the virtual environment**

``` PowerShell
& e:/PublicRepo/d2d_utils/env/Scripts/Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Count lines of code**

```
cloc --exclude-dir="env" .
```

```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                           3             20             18             54
PowerShell                       2             18             24             36
Markdown                         1              7              0             26
Text                             1              3              0              8
-------------------------------------------------------------------------------
SUM:                             7             48             42            124
-------------------------------------------------------------------------------
```
