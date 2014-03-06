import pythoncom
from win32com.shell import shell,shellcon

def copy(src,dst,flags=shellcon.FOF_NOCONFIRMATION):
    """ Copy files using the built in Windows File copy dialog
    
    Requires absolute paths. Does NOT create root destination folder if it doesn't exist.
    
    Overwrites and is recursive by default 
    
    @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx for flags available
    
    """
    # @see IFileOperation
    pfo = pythoncom.CoCreateInstance(shell.CLSID_FileOperation,None,pythoncom.CLSCTX_ALL,shell.IID_IFileOperation)

    # Respond with Yes to All for any dialog
    # @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx
    pfo.SetOperationFlags(flags)

    # Set the destionation folder
    dst = shell.SHCreateItemFromParsingName(dst,None,shell.IID_IShellItem)
    
    if type(src) not in (tuple,list):
        src = (src,)

    for f in src:
        item = shell.SHCreateItemFromParsingName(f,None,shell.IID_IShellItem)
        pfo.CopyItem(item,dst) # Schedule an operation to be performed

    # @see http://msdn.microsoft.com/en-us/library/bb775780(v=vs.85).aspx
    success = pfo.PerformOperations()

    # @see sdn.microsoft.com/en-us/library/bb775769(v=vs.85).aspx
    aborted = pfo.GetAnyOperationsAborted()
    return success is None and not aborted

def move(src,dst,flags=shellcon.FOF_NOCONFIRMATION):
    """ Move files using the built in Windows File copy dialog
    
    Requires absolute paths. Does NOT create root destination folder if it doesn't exist.
    
    @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx for flags available
    
    """
    # @see IFileOperation
    pfo = pythoncom.CoCreateInstance(shell.CLSID_FileOperation,None,pythoncom.CLSCTX_ALL,shell.IID_IFileOperation)

    # Respond with Yes to All for any dialog
    # @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx
    pfo.SetOperationFlags(flags)

    # Set the destionation folder
    dst = shell.SHCreateItemFromParsingName(dst,None,shell.IID_IShellItem)
    
    if type(src) not in (tuple,list):
        src = (src,)

    for f in src:
        item = shell.SHCreateItemFromParsingName(f,None,shell.IID_IShellItem)
        pfo.MoveItem(item,dst) # Schedule an operation to be performed

    # @see http://msdn.microsoft.com/en-us/library/bb775780(v=vs.85).aspx
    success = pfo.PerformOperations()

    # @see sdn.microsoft.com/en-us/library/bb775769(v=vs.85).aspx
    aborted = pfo.GetAnyOperationsAborted()
    return success is None and not aborted

def delete(path,flags=shellcon.FOF_NOCONFIRMATION):
    """ Delete files using the built in Windows File copy dialog
    
    Requires absolute paths.
    
    @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx for flags available
    
    """
    # @see IFileOperation
    pfo = pythoncom.CoCreateInstance(shell.CLSID_FileOperation,None,pythoncom.CLSCTX_ALL,shell.IID_IFileOperation)

    # Respond with Yes to All for any dialog
    # @see http://msdn.microsoft.com/en-us/library/bb775799(v=vs.85).aspx
    pfo.SetOperationFlags(flags)
    
    if type(path) not in (tuple,list):
        src = (path,)

    for f in path:
        item = shell.SHCreateItemFromParsingName(f,None,shell.IID_IShellItem)
        pfo.DeleteItem(item) # Schedule an operation to be performed

    # @see http://msdn.microsoft.com/en-us/library/bb775780(v=vs.85).aspx
    success = pfo.PerformOperations()

    # @see sdn.microsoft.com/en-us/library/bb775769(v=vs.85).aspx
    aborted = pfo.GetAnyOperationsAborted()
    return success is None and not aborted
