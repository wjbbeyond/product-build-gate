import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('gate', Path(__file__).resolve().parents[1] / 'scripts/gate.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class GateTests(unittest.TestCase):
    def test_title_roundtrip(self):
        for title in ['中文项目', 'A "quoted" title', r'A\B']:
            for template in gate.ASSET_DIR.glob('*.md'):
                self.assertEqual(gate.project_title(gate.render_asset(template.name, title)), title)

    def test_invalid_titles(self):
        for title in ['', '  ', 'a\nb', 'a\rb']:
            with self.assertRaises(gate.GateError):
                gate.render_asset('PRODUCT_BUILD_GATE.template.md', title)

    def test_markers(self):
        start, end = '<!-- GATE:x:START -->', '<!-- GATE:x:END -->'
        for text in [start, end + start, start + start + end, start + end + end]:
            with self.assertRaises(gate.GateError):
                gate.marked_section(text, 'x')
        failures = []
        gate.check_section(start + end, 'x', 'x', failures)
        self.assertTrue(failures)

    def test_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'document.md'
            gate.write_new(target, 'original')
            with self.assertRaises(gate.GateError):
                gate.write_new(target, 'replacement')
            self.assertEqual(target.read_text(), 'original')

    def test_refuses_external_docs_symlink(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder) / 'project'
            project.mkdir()
            (project / 'docs').symlink_to(Path(folder), target_is_directory=True)
            with self.assertRaises(gate.GateError):
                gate.project_path(str(project))


if __name__ == '__main__':
    unittest.main()
