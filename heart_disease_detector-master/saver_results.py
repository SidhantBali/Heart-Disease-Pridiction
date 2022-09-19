import os

class SaveResult:
    
    def __init__(self):
        self.file_name = "results.data"
        self.path_to_save = ""
    
    def set_path(self, path):
        """
        Set the path to save the results.
        The method doesn't create folders, please submit only existing path.\n
        Default name of file: results.data \n
        Example: \n
        1) "folder1/folder2/"\n
        2) "folder1/folder2/name_of_file.data"                 
        """
        
        self.path_to_save = ""
        for arg in path.split("/"):
            self.path_to_save = os.path.join(self.path_to_save, arg)
            
        if self.path_to_save.split('.')[-1] != 'data':
            self.path_to_save = os.path.join(self.path_to_save, self.file_name)
    
    def save(self, data):
        formatted_data = ','.join(str(i) for i in data)
        with open(self.path_to_save, "a+") as f:
            f.write(formatted_data + "\n")