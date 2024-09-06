import os
import sys
import platform
import webview

class Api:
    def show_pwd(self):
        return os.getcwd()
    
    def show_arch(self):
        return str(platform.platform())
    
    def show_args(self):
        return str(sys.argv)
    

if __name__ == '__main__':
    api = Api()
    webview.create_window('VueTest1', 'assets/index.html', js_api=api, min_size=(600, 450))
    webview.start()