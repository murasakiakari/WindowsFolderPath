class WindowsFolderPath:
    class __FolderID:
        desktop = '{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}'
        documents = '{FDD39AD0-238F-46AF-ADB4-6C85480369C7}'
        downloads = '{374DE290-123F-4565-9164-39C4925E467B}'
        music = '{4BD8D571-6D19-48D3-BE97-422220080E43}'
        pictures = '{33E28130-4E1E-4676-835A-98395C3BC3BB}'
        videos = '{18989B1D-99B5-455B-841C-AB7C74E4DDFC}'
    
    class __NotSupportError(BaseException):
        pass

    def __init__(self):
        import os
        if os.name != 'nt':
            raise self.__NotSupportError('This Program is designed to run on Windows')
    
    def __get_folder_path(self, folderid):
        import ctypes
        from ctypes import windll, wintypes
        from uuid import UUID
        class GUID(ctypes.Structure):
            _fields_ = [("Data1", wintypes.DWORD), ("Data2", wintypes.WORD), ("Data3", wintypes.WORD), ("Data4", wintypes.BYTE * 8)] 
            def __init__(self, folderid):
                super().__init__()
                uuid = UUID(folderid)
                self.Data1, self.Data2, self.Data3, self.Data4[0], self.Data4[1], rest = uuid.fields
                for i in range(2, 8):
                    self.Data4[i] = rest >> (8 - i - 1) * 8 & 0xff
        SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
        SHGetKnownFolderPath.argtypes = [ctypes.POINTER(GUID), wintypes.DWORD, wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)]
        pathptr = ctypes.c_wchar_p()
        guid = GUID(folderid)
        if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
           raise ctypes.WinError()
        return pathptr.value

    def Desktop(self):
        return self.__get_folder_path(self.__FolderID.desktop)
    
    def Documents(self):
        return self.__get_folder_path(self.__FolderID.documents)
    
    def Downloads(self):
        return self.__get_folder_path(self.__FolderID.downloads)

    def Music(self):
        return self.__get_folder_path(self.__FolderID.music)
    
    def Pictures(self):
        return self.__get_folder_path(self.__FolderID.pictures)
    
    def Videos(self):
        return self.__get_folder_path(self.__FolderID.videos)
