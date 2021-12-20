from aqt.utils import getText, qconnect
from aqt.qt import QMenu
from aqt import mw, deckchooser

from anki import search_pb2

from html.parser import HTMLParser
parser = HTMLParser()

def unescape_note(note):
    note.fields = [parser.unescape(field) for field in note.fields]
    note.flush()

def unescape(deck_id):
    deck = mw.col.decks.get(deck_id)
    node = search_pb2.SearchNode(deck=deck['name'])

    search_string = mw.col.build_search_string(node)
    note_ids = mw.col.find_notes(search_string)

    for note_id in note_ids:
        note = mw.col.get_note(note_id)
        unescape_note(note)


def add_unescape_menu(m: QMenu, id: int):
    a = m.addAction("Unescape notes")
    qconnect(a.triggered, lambda b, did=id: unescape(id))

from aqt import gui_hooks
gui_hooks.deck_browser_will_show_options_menu.append(add_unescape_menu)