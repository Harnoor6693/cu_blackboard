import os, time, socket, shutil, requests, logging, coloredlogs
from zipfile import ZipFile


logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(asctime)s [%(levelname)s]: %(message)s',level='DEBUG', logger=logger)


# todo
## webdriver download in download function
## download items in hidden folder

global URL

URL = "https://api.github.com/repos/namishkhanna/cu_blackboard/tags"


class ErrorHandler():
    def __init__(self):
        pass

    # check if device is connected to internet
    def connectionCheck(self):
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            sock = socket.create_connection(("www.google.com", 80))
            if sock is not None:
                sock.close
            return True
        except:
            pass

            
        return False

    def is_connected(self):

        # waiting till network connection is available
        tempCounter = 0
        networkAvaliable = self.connectionCheck()
        if not networkAvaliable:
            logger.error("Network not available")

        while(not networkAvaliable):

            tempCounter+=1
            if tempCounter == 7:
                logger.info("Waiting for internet connection ...")
            time.sleep(2)
            
            networkAvaliable = self.connectionCheck()


class Updater():
    def __init__(self):
        pass


    def downloader(self):

        global URL
        ErrorHandlerobj = ErrorHandler()

        while(True):
            try:
                repo_response = requests.get(URL)
                repo_response = repo_response.json()[0]
                zip_url = repo_response["zipball_url"]
                break
            except:
                logger.error("Unable to Download Update Files")

                ErrorHandlerobj.is_connected()

        try:
            zip_file = requests.get(zip_url, stream=True)
            with open("update.zip", 'wb') as fd:
                for chunk in zip_file.iter_content(chunk_size=128):
                    fd.write(chunk)
        except:
            logger.error("Unable to Write Files")
                    


    def pre_remover(self):

        all_files = os.listdir(".")
        all_files.remove("update.zip")
        #all_files.remove("update.exe")
        #all_files.remove("test13.py")
        #all_files.remove("update.py")
        all_files.remove("BB_Attender")

        try:
            for i in all_files:
                if os.path.isdir(i):
                    shutil.rmtree(i)
                else:
                    os.remove(i)
        except:
            logger.error("Unable to Perform Cleanup")
        

    def post_remover(self, isInside):

        try:
            os.remove("update.zip")
            os.remove("installer.py")
        except:
            logger.error("Unable to Perform Cleanup")
        
        if(isInside):
            try:
                shutil.rmtree("BB_Attender")
            except:
                logger.error("Unable to Remove Repo Folder")


    def extractor(self):

        try:
            zip_file = "update.zip"
            with ZipFile(zip_file, 'r') as f:
                f.extractall()
        except:
            logger.error("Unable to Extract Files")
    

    def dir_rename(self):

        try:
            all_files = os.listdir(".")
            for i in all_files:
                if(os.path.isdir(i)) and ("namishkhanna-cu_blackboard" in i):
                    os.rename(i,"BB_Attender")
        except:
            logger.error("Unable to Rename Files")
            if("BB_Attender" in all_files):
                shutil.rmtree("BB_Attender")
                for i in all_files:
                    if(os.path.isdir(i)) and ("namishkhanna-cu_blackboard" in i):
                        os.rename(i,"BB_Attender")
    

    def mover(self):

        source_dir = "BB_Attender"
        target_dir = "."

        file_names = os.listdir(source_dir)
    
        for file_name in file_names:
            shutil.move(os.path.join(source_dir, file_name), target_dir)
    


if __name__ == '__main__':

    updaterobj = Updater()

    logger.info("Downloading Updates ...")
    updaterobj.downloader()

    

    logger.info("Extracting Files ...")
    updaterobj.extractor()
    
    updaterobj.dir_rename()

    current_directory = str(os.getcwd()).split("\\")[-1]
    if(current_directory=="BB_Attender"):

        logger.info("Installing Updates ...")
        updaterobj.pre_remover()

        updaterobj.mover()

        logger.info("Performing Cleanup ...")
        updaterobj.post_remover(True)

        
    
    else:
        
        logger.info("Performing Cleanup ...")
        updaterobj.post_remover(False)

    logger.info("Successfully Updated ^_^")