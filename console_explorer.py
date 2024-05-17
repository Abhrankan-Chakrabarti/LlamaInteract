from console_menu import Console, Menu
import os

sep = '\\' if os.name == 'nt' else '/'


def _browse(return_type='folder', extensions_list=None):
    cwd = os.getcwd().split(sep)
    _cwd = cwd[:]
    path = _path = '/'.join(cwd)
    dirs_list = []
    console = Console(width=59, height=30)
    while True:
    	text = (
    	    _path
    	)

    	options = {}
    	if return_type == 'folder':
    		options[_path] = 'Choose this folder'
    	parentdir = '/'.join(_cwd[:-1]) or '/'
    	if _path != '/':
    		options[parentdir] = chr(128193) + ' ..'

    	try:
    		files_list = []
    		for element in os.listdir(_path):
    			if os.path.isdir(_path + '/' + element):
    				options[_path + '/' + element] = chr(128193) + ' ' + element
    			elif extensions_list is None or element.split('.')[-1] in extensions_list:
    				files_list.append(element)
    		for file in files_list:
    			options[_path + '/' + file] = chr(128196) + ' ' + file
    		del files_list
    	except:
    		if path in options:
    			for dir in dirs_list:
    				if _path == dir[0]:
    					options['/'.join(dir)] = chr(128193) + ' ' + dir[1]
    					break
    		else:
    			options[path] = chr(128193) + ' ' + cwd[-1]
    			if ('/'.join(cwd[:-1]), cwd[-1]) not in dirs_list:
    				dirs_list.append(('/'.join(cwd[:-1]), cwd[-1]))
    	starting_menu = Menu(text, options, console)
    	starting_menu.print_menu(justify="left")
    	starting_menu.print_options(justify="left")
    	a = starting_menu.choice()

    	if return_type == 'filename' and not os.path.isdir(a):
    		return a
    	elif return_type == 'folder' and a == _path:
    		return a
    	path = _path
    	cwd = path.split('/')
    	_path = a
    	_cwd = _path.split('/')


def browse_for_file(extensions_list=None):
    return _browse('filename', extensions_list=extensions_list)


def browse_for_folder():
	return _browse()