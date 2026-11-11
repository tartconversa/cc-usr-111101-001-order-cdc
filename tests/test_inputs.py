import json
import tempfile
import unittest
from pathlib import Path
from src.source_reader import load


class InputReaderTests(unittest.TestCase):
    def test_fixture_is_readable(self):
        self.assertGreater(len(load(Path(__file__).resolve().parents[1] / 'fixtures/transactions.jsonl')), 0)

    def test_bad_json_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.json"
            path.write_text("{bad", encoding="utf-8")
            with self.assertRaises(json.JSONDecodeError):
                load(path)

    def test_csv_retains_multiline_field(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "lines.csv"
            path.write_bytes(b'id,name\n1,"two\nlines"\n')
            self.assertEqual(load(path), [{"id": "1", "name": "two\nlines"}])

    def test_missing_file_is_not_empty(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(FileNotFoundError):
                load(Path(directory) / "absent.json")
