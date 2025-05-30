#
# ███╗   ███╗██████╗ ██████╗ ██╗  ██╗
# ████╗ ████║╚═══╗██╗██╔══██╗██║ ██╔╝
# ██╔████╔██║███████║██████╔╝█████╔╝
# ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗
# ██║ ╚═╝ ██║ █████╔╝██║  ██║██║  ██╗
# ╚═╝     ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
# Copyright (C) 2025  Daniel Hetrick
# https://github.com/nutjob-laboratories/merk
# https://github.com/nutjob-laboratories
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore

from datetime import datetime
import sys
import os
import math
import base64

from .version import *
from .servers import *
from .emoji1 import *
from .emoji2 import *
from .style import *

# Load in resource file
globals()["merk.resources.resources"] = __import__("merk.resources.resources")

SYSTEM_PREPEND_OPTIONS = [
	"Nothing",
	"&diams;",
	"&loz;",
	"&rarr;",
	"&dagger;",
	"&Dagger;",
	"&lambda;",
	"&Delta;",
	"&there4;",
	"&infin;",
	"&sect;",
	"&lt;",
	"&gt;",
	"&sum;",
	"&le;",
	"&ge;",
	"&oplus;",
	"&harr;",
	"&spades;",
	"&clubs;",
	"&hearts;",
	"&bull;",
	"&mdash;",
]

def encode_filename(filename):
	enc = filename.encode('utf-8')
	output = base64.urlsafe_b64encode(enc)
	return output

def decode_filename(encoded_filename):
	if isinstance(encoded_filename, str):
		encoded_filename = encoded_filename.encode('utf-8')
	decoded_filename_bytes = base64.urlsafe_b64decode(encoded_filename)
	decoded_filename = decoded_filename_bytes.decode('utf-8')
	return decoded_filename

def remove_duplicate_sublists(list_of_lists):
	seen = set()
	new_list = []
	for sublist in list_of_lists:
		tuple_sublist = tuple(sublist)
		if tuple_sublist not in seen:
			new_list.append(sublist)
			seen.add(tuple_sublist)
	return new_list

def is_running_from_pyinstaller():
	return getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

def is_deleted(obj):
	if hasattr(obj,"isVisible"):
		if not obj.isVisible():
			if hasattr(obj,"isMinimized"):
				if obj.isMinimized():
					return True
	if hasattr(obj,"isVisible"):
		if not obj.isVisible():
			return True
	return False

def is_wav_file(file_path):
	if not os.path.isfile(file_path):
		return False
	
	try:
		with open(file_path, 'rb') as f:
			header = f.read(44)  # Read the first 44 bytes (standard WAV header size)
			return header[:4] == b'RIFF' and header[8:12] == b'WAVE' and header[12:16] == b'fmt '
	except Exception:
		return False

INSTALL_DIRECTORY = sys.path[0]
MERK_MODULE_DIRECTORY = os.path.join(INSTALL_DIRECTORY, "merk")

APPLICATION_NAME = "MERK"
APPLICATION_SOURCE = "https://github.com/nutjob-laboratories/merk"
SCRIPT_FILE_EXTENSION = "merk"

EMOJI_AUTOCOMPLETE = EMOJI_AUTOCOMPLETE_DATA.split("\n")
EMOJI_AUTOCOMPLETE = EMOJI_AUTOCOMPLETE + EMOJI_AUTOCOMPLETE_ALIAS_DATA.split("\n")

LIST_OF_NETWORK_LINKS = []
for line in NETWORK_LINKS.split("\n"):
		line = line.strip()
		p = line.split(":",1)
		LIST_OF_NETWORK_LINKS.append(p)

def get_network_link(network):
	for ent in LIST_OF_NETWORK_LINKS:
		if ent[0].lower()==network.lower(): return ent[1]
	return None

# Sort the emoji autocomplete list by length
EMOJI_AUTOCOMPLETE.sort(key=len)

BUNDLED_FONT = ":/font-FiraMono-Regular.ttf"
OTHER_BUNDLED_FONTS = [
	":/font-FiraMono-Medium.ttf",
	":/font-FiraMono-Bold.ttf",
]
BUNDLED_FONT_SIZE = 10

# Constants

CHANNEL_WINDOW = 0
SERVER_WINDOW = 1
PRIVATE_WINDOW = 2
EDITOR_WINDOW = 3
LIST_WINDOW = 4

CHAT_WINDOW_WIDGET_SPACING = 5

SYSTEM_MESSAGE = 0
ERROR_MESSAGE = 1
ACTION_MESSAGE = 2
CHAT_MESSAGE = 3
SELF_MESSAGE = 4
NOTICE_MESSAGE = 5
SERVER_MESSAGE = 6
PRIVATE_MESSAGE = 7
RAW_SYSTEM_MESSAGE = 8
HORIZONTAL_RULE_MESSAGE = 9
HARD_HORIZONTAL_RULE_MESSAGE = 10
TEXT_HORIZONTAL_RULE_MESSAGE = 11
WHOIS_MESSAGE = 12
DATE_MESSAGE = 13
LIST_MESSAGE = 14

UNKNOWN_NETWORK = "UNKNOWN"

CUSTOM_MENU_ICON_SIZE = 24

# Icons

ROUND_UNCHECKED_ICON = ":/icon-runchecked.png"
ROUND_CHECKED_ICON = ":/icon-rchecked.png"
CHECKED_ICON = ":/icon-checked.png"
UNCHECKED_ICON = ":/icon-unchecked.png"
OPTIONS_ICON = ":/icon-options.png"
BOLD_ICON = ":/icon-bold.png"
ITALIC_ICON = ":/icon-italic.png"
SPELLCHECK_ICON = ":/icon-spellcheck.png"
MENU_ICON = ":/icon-menu.png"
WINDOW_ICON = ":/icon-window.png"
SYSTRAY_ICON = ":/icon-tray.png"
MDI_BACKGROUND = ":/gui-background.png"

DARK_ROUND_UNCHECKED_ICON = ":/icon-dark_runchecked.png"
DARK_ROUND_CHECKED_ICON = ":/icon-dark_rchecked.png"
DARK_CHECKED_ICON = ":/icon-dark_checked.png"
DARK_UNCHECKED_ICON = ":/icon-dark_unchecked.png"
DARK_OPTIONS_ICON = ":/icon-dark_options.png"
DARK_BOLD_ICON = ":/icon-dark_bold.png"
DARK_ITALIC_ICON = ":/icon-dark_italic.png"
DARK_MDI_BACKGROUND = ":/gui-dark_background.png"

APPLICATION_ICON = ":/icon-app.png"
NEXT_ICON = ":/icon-next.png"
PREVIOUS_ICON = ":/icon-previous.png"
CONSOLE_ICON = ":/icon-console.png"
PRIVATE_ICON = ":/icon-private.png"
CHANNEL_ICON = ":/icon-channel.png"
QUIT_ICON = ":/icon-quit.png"
NETWORK_ICON = ":/icon-network.png"
CONNECT_ICON = ":/icon-connect.png"
DISCONNECT_ICON = ":/icon-disconnect.png"
INFO_ICON = ":/icon-info.png"
BOOKMARK_ICON = ":/icon-bookmark.png"
SECURE_ICON = ":/icon-secure.png"
VISITED_BOOKMARK_ICON = ":/icon-visited_bookmark.png"
VISITED_SECURE_ICON = ":/icon-visited_secure.png"
STYLE_ICON = ":/icon-style.png"
WHOIS_ICON = ":/icon-whois.png"
KICK_ICON = ":/icon-kick.png"
BAN_ICON = ":/icon-ban.png"
KICKBAN_ICON = ":/icon-kickban.png"
CLIPBOARD_ICON = ":/icon-clipboard.png"
PLUS_ICON = ":/icon-plus.png"
MINUS_ICON = ":/icon-minus.png"
KEY_ICON = ":/icon-key.png"
FONT_ICON = ":/icon-font.png"
RESIZE_ICON = ":/icon-resize.png"
SETTINGS_ICON = ":/icon-settings.png"
EDIT_ICON = ":/icon-edit.png"
INPUT_ICON = ":/icon-input.png"
LOG_ICON = ":/icon-log.png"
MESSAGE_ICON = ":/icon-message.png"
ABOUT_ICON = ":/icon-about.png"
PRIVATE_WINDOW_ICON = ":/icon-private_window.png"
CHANNEL_WINDOW_ICON = ":/icon-channel_window.png"
LINK_ICON = ":/icon-link.png"
FOLDER_ICON = ":/icon-folder.png"
DICTIONARY_ICON = ":/icon-dictionary.png"
TIMESTAMP_ICON = ":/icon-timestamp.png"
NEWFILE_ICON = ":/icon-new_file.png"
OPENFILE_ICON = ":/icon-file_open.png"
SAVEFILE_ICON = ":/icon-save_file.png"
SAVEASFILE_ICON = ":/icon-save_as.png"
UNDO_ICON = ":/icon-undo.png"
REDO_ICON = ":/icon-redo.png"
CUT_ICON = ":/icon-cut.png"
COPY_ICON = ":/icon-copy.png"
SELECTALL_ICON = ":/icon-select_all.png"
SCRIPT_MENU_ICON = ":/icon-script_menu.png"
SETTINGS_MENU_ICON = ":/icon-settings_menu.png"
STYLE_MENU_ICON = ":/icon-style_menu.png"
LOG_MENU_ICON = ":/icon-log_menu.png"
APPLICATION_MENU_ICON = ":/icon-app_menu.png"
SCRIPT_ICON = ":/icon-script.png"
CLOSE_ICON = ":/icon-close.png"
AUTOCOMPLETE_ICON = ":/icon-autocomplete.png"
RUN_ICON = ":/icon-run.png"
RUN_MENU_ICON = ":/icon-run_menu.png"
WIDGET_ICON = ":/icon-widget.png"
JUSTIFY_ICON = ":/icon-justify.png"
PRIVATE_MENU_ICON = ":/icon-private_menu.png"
CLEAR_ICON = ":/icon-clear.png"
CONNECT_MENU_ICON = ":/icon-connect_menu.png"
DISCONNECT_MENU_ICON = ":/icon-disconnect_menu.png"
QT_ICON = ":/icon-qt.png"
PYTHON_ICON = ":/icon-python.png"
TWISTED_ICON = ":/icon-twisted.png"
TWISTED_BUTTON_ICON = ":/icon-twisted_button.png"
PYINSTALLER_ICON = ":/icon-pyinstaller.png"
PYQT_ICON = ":/icon-pyqt.png"
CONNECT_DIALOG_ICON = ":/icon-connect_connect_dialog.png"
NETWORK_MENU_ICON = ":/icon-network_menu.png"
NOTIFICATION_ICON = ":/icon-notifications.png"
DISCONNECT_WINDOW_ICON = ":/icon-disconnect_window.png"
SUBWINDOW_ICON = ":/icon-subwindow.png"
DARK_SHOW_ICON = ":/gui-dark_show.png"
SHOW_ICON = ":/icon-show.png"
DARK_HIDE_ICON = ":/gui-dark_hide.png"
HIDE_ICON = ":/icon-hide.png"
LIST_ICON = ":/icon-list.png"

SPLASH_LOGO = ":/gui-splash.png"
VERTICAL_SPLASH_LOGO = ":/gui-vertical.png"
DISCONNECT_DIALOG_IMAGE = ":/gui-disconnect_dialog.png"

ADMIN_USER = ":/gui-admin.png"
HALFOP_USER = ":/gui-halfop.png"
OP_USER = ":/gui-op.png"
OWNER_USER = ":/gui-owner.png"
VOICE_USER = ":/gui-voice.png"
NORMAL_USER = ":/gui-normal.png"
PROTECTED_USER = ":/gui-protected.png"

HORIZONTAL_DOTTED_BACKGROUND = ":/gui-horizontal_dotted.png"
HORIZONTAL_RULE_BACKGROUND = ":/gui-horizontal_rule.png"
LIGHT_HORIZONTAL_DOTTED_BACKGROUND = ":/gui-light_horizontal_dotted.png"
LIGHT_HORIZONTAL_RULE_BACKGROUND = ":/gui-light_horizontal_rule.png"
NUTJOB_LOGO = ":/gui-nutjob.png"

BELL_NOTIFICATION = ":/sound-notification.wav"


HELP_ENTRY_TEMPLATE='''<tr><td>%_USAGE_%&nbsp;</td><td>%_DESCRIPTION_%</td></tr>'''

HELP_DISPLAY_TEMPLATE='''<table style="width: 100%" border="0">
	<tbody>
				<tr>
					<td><center><b>Commands</b></center></td>
				</tr>
				<tr>
					<td><small>
					Arguments inside brackets are optional. If called from a channel window,
					channel windows can be omitted to apply the command to the current channel.
					%_AUTOCOMPLETE_%
					</small></td>
				</tr>
				<tr>
					<td>&nbsp;</center></td>
				</tr>
				<tr>
					<td>
						<table style="width: 100%" border="0">
							<tbody>
								%_LIST_%
							</tbody>
						</table>
					</td>
				</tr>
			</tbody>
		</table>'''

# Classes

class Message:
	def __init__(self,mtype,sender,contents,timestamp=None):
		if timestamp:
			self.timestamp = timestamp
		else:
			self.timestamp = datetime.timestamp(datetime.now())
		self.type = mtype
		self.sender = sender
		self.contents = contents
		self.channel = ''
		self.channel_count = ''
		self.channel_topic = ''

class ConnectInfo:
	def __init__(self,nick,alt,username,realname,host,port,password,reconnect,ssl,execute_script):
		self.nickname = nick
		self.alternate = alt
		self.username = username
		self.realname = realname
		self.host = host
		self.port = port
		self.password = password
		self.reconnect = reconnect
		self.ssl = ssl
		self.execute_script = execute_script

class WhoisData:
	def __init__(self):
		self.nickname = 'Unknown'
		self.username = 'Unknown'
		self.realname = 'Unknown'
		self.host = 'Unknown'
		self.signon = '0'
		self.idle = '0'
		self.server = 'Unknown'
		self.channels = 'Unknown'
		self.privs = 'is a normal user'

class WhoData:
	def __init__(self):
		self.username = 'Unknown'
		self.host = 'Unknown'
		self.server = 'Unknown'
		self.channel = 'Unknown'

class WhoWasData:
	def __init__(self):
		self.username = 'Unknown'
		self.host = 'Unknown'
		self.realname = 'Unknown'

# Functions

def convert_size(size_bytes):
	if size_bytes == 0:
		return "0 B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])

def convertSeconds(seconds):
	h = seconds//(60*60)
	m = (seconds-h*60*60)//60
	s = seconds-(h*60*60)-(m*60)
	return [h, m, s]

def prettyUptime(uptime):
	t = convertSeconds(uptime)
	hours = t[0]
	if len(str(hours))==1: hours = f"0{hours}"
	minutes = t[1]
	if len(str(minutes))==1: minutes = f"0{minutes}"
	seconds = t[2]
	if len(str(seconds))==1: seconds = f"0{seconds}"
	return f"{hours}:{minutes}:{seconds}"

def test_if_window_background_is_light(obj):
	# Determine if window color is dark or light
		mbcolor = obj.palette().color(QPalette.Window).name()
		c = tuple(int(mbcolor[i:i + 2], 16) / 255. for i in (1, 3, 5))
		luma = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
		luma = luma*100

		if luma>=40:
			return True
		else:
			return False

def test_if_background_is_light(style):

	bg = None
	style = style.strip()
	for e in style.split(';'):
		y = e.split(':')
		if len(y)==2:
			c = y[0].strip()
			if c.lower()=='background-color':
				bg = y[1].strip()

	if bg!=None:
		c = tuple(int(bg[i:i + 2], 16) / 255. for i in (1, 3, 5))
		luma = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
		luma = luma*100

		if luma>=40:
			return True
		else:
			return False

# Widgets

class QNoSpaceLineEdit(QLineEdit):

	def __init__(self, *args):
		QLineEdit.__init__(self, *args)

	def keyPressEvent(self,event):

		if event.key() == Qt.Key_Space:
			return
		else:
			return super().keyPressEvent(event)