from console_explorer import *
import os

file = browse_for_file(extensions_list=('gguf',))
if file:
    model = os.path.basename(file)  # Safely extract the file name
else:
    model = None  # Handle case where no file was selected