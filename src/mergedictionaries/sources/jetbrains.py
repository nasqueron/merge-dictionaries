#   -------------------------------------------------------------
#   Merge dictionaries :: Sources :: JetBrains IDEs
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Find application-level dictionaries
#                   from JetBrains IDEs
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import os
from xml.etree import ElementTree


def get_configuration_path():
    return os.environ["HOME"] + "/.config/JetBrains"


def find_application_level_dictionaries():
    # We're looking for paths like:
    # ~/.config/JetBrains/PyCharm2021.3/options/cachedDictionary.xml
    base_path = get_configuration_path()

    return [
        candidate
        for candidate in [
            os.path.join(base_path, entry.name, "options", "cachedDictionary.xml")
            for entry in os.scandir(base_path)
            if entry.is_dir()
        ]
        if os.path.exists(candidate)
    ]


def extract_words(dictionary_path):
    tree = ElementTree.parse(dictionary_path)
    return [word.text for word in tree.getroot()[0][0]]


def extract_words_from_all_dictionaries():
    return {
        word
        for dictionary_path in find_application_level_dictionaries()
        for word in extract_words(dictionary_path)
    }
