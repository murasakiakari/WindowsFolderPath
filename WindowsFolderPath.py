class WindowsFolderPath:
    def __get_folder_path(folderid):
        from os import name as os_name
        assert (os_name == 'nt'), 'This Program is designed to run on Windows only.'
        import ctypes
        from ctypes import windll, wintypes
        from uuid import UUID
        class GUID(ctypes.Structure):
            _fields_ = [('data1', wintypes.DWORD), ('data2', wintypes.WORD), ('data3', wintypes.WORD), ('data4', wintypes.BYTE * 8)] 
            def __init__(self, folderid):
                super().__init__()
                uuid = UUID(folderid)
                self.data1, self.data2, self.data3, self.data4[0], self.data4[1], rest = uuid.fields
                self.data4[2:] = [rest >> (8 - i - 1) * 8 & 255 for i in range(2, 8)]
        SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
        SHGetKnownFolderPath.argtypes = [ctypes.POINTER(GUID), wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)]
        pathptr = ctypes.c_wchar_p()
        guid = GUID(folderid)
        if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
           raise ctypes.WinError()
        return pathptr.value
    
    Desktop = __get_folder_path('{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}')
    Documents = __get_folder_path('{FDD39AD0-238F-46AF-ADB4-6C85480369C7}')
    Downloads = __get_folder_path('{374DE290-123F-4565-9164-39C4925E467B}')
    Music = __get_folder_path('{4BD8D571-6D19-48D3-BE97-422220080E43}')
    Pictures = __get_folder_path('{33E28130-4E1E-4676-835A-98395C3BC3BB}')
    Videos = __get_folder_path('{18989B1D-99B5-455B-841C-AB7C74E4DDFC}')
