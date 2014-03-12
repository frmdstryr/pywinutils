pywinutils
==========

Copy, move, and delete files using window's built in copy dialogs (with progress window).


### Requires ###


[pywin32](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32) >= 218.4 

> Note: the version from Sourceforge will not work


### Usage ###

```python
In [1]: import winutils
In [2]: winutils.copy(src=r'C:\Users\jrm\Downloads\bitnami-gitlab-6.4.3-1-linux-x64-installer.run',dst=r'C:\Users\jrm\Desktop')
Out[2]: True

```

![Copy progress](https://lh6.googleusercontent.com/0JeNt0WSw2S4QwbbgEqx8STNdXlu2WHJTb0hFZI1krRKfkh2dxU6pFAavMq5z-1YR1Mmgzoc61vCxvlMM0SUDKRT49YoJ9mCG2caXpJYtwbLtFXLhsKcZXV0Csb8-A)
