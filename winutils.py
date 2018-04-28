'''
Created on May 31, 2016

@author: frmdstryr
@copyright: frmdstryr@gmail.com
@license: MIT

'''
import pythoncom
from win32com.shell import shell,shellcon

def _file_operation(src,dst=None,operation='copy',flags=shellcon.FOF_NOCONFIRMATION):
    # @see IFileOperation
    pfo = pythoncom.CoCreateInstance(shell.CLSID_FileOperation,None,pythoncom.CLSCTX_ALL,shell.IID_IFileOperation)

    # Respond with Yes to All for any dialog
    # @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx
    pfo.SetOperationFlags(flags)

    if not isinstance(src,(tuple,list)):
        src = (src,)

    if dst is not None:
        # Set the destination folder
        dst = shell.SHCreateItemFromParsingName(dst,None,shell.IID_IShellItem)

    for f in src:
        item = shell.SHCreateItemFromParsingName(f,None,shell.IID_IShellItem)
        op = operation.strip().lower()
        if op=='copy':
            pfo.CopyItem(item,dst) # Schedule an operation to be performed
        elif op=='move':
            pfo.MoveItem(item,dst)
        elif op=='delete':
            pfo.DeleteItem(item)
        else:
            raise ValueError("Invalid operation {}".format(operation))

    # @see http://msdn.microsoft.com/en-us/library/bb775780(v=vs.85).aspx
    success = pfo.PerformOperations()

    # @see sdn.microsoft.com/en-us/library/bb775769(v=vs.85).aspx
    aborted = pfo.GetAnyOperationsAborted()
    return success is None and not aborted
    

def copy(src,dst,flags=shellcon.FOF_NOCONFIRMATION):
    """ Copy files using the built in Windows File operations dialog
    
    Requires absolute paths. Does NOT create root destination folder if it doesn't exist.
    
    Overwrites and is recursive by default 
    
    @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx for flags available
    
    """
    return _file_operation(src,dst,'copy',flags)

def move(src,dst,flags=shellcon.FOF_NOCONFIRMATION):
    """ Move files using the built in Windows File operations dialog
    
    Requires absolute paths. Does NOT create root destination folder if it doesn't exist.
    
    @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx for flags available
    
    """
    return _file_operation(src,dst,'move',flags)

def delete(path,flags=shellcon.FOF_NOCONFIRMATION):
    """ Delete files using the built in Windows File operations dialog
    
    Requires absolute paths.
    
    @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx for flags available
    
    """
    return _file_operation(path,None,'delete',flags)
