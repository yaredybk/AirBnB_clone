#!/usr/bin/python3
"""create a new instance of filestorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
