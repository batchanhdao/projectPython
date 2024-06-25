from abc import ABC, abstractmethod 
import os

class Logger(ABC):
    def __init__(self, log_file):
        present_folder = os.getcwd()
        log_file = os.path.join(present_folder, log_file)
        if not os.path.exists(log_file):
            with open(log_file, 'w') as f:
                f.write('')

        self.log_file = log_file

    @abstractmethod
    def write(self, message):
        pass

class FileLogger(Logger):
    def write(self, message):
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(message + '\n')
                print(message)
        except Exception as e:
            print(f"Error writing log: {e}")

class ErrorLogger(Logger):
    def write(self, message):
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(message + '\n')
                print(message)
        except Exception as e:
            print(f"Error writing log: {e}")


    

