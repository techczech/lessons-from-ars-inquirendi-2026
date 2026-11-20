"""Build index.html (self-contained, searchable, interlinked) from data/conference-resources-2026.json.
Usage: python3 build.py"""
import json, pathlib

here = pathlib.Path(__file__).parent
data = json.loads((here / "data" / "conference-resources-2026.json").read_text())
tpl = (here / "template.html").read_text()
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
(here / "index.html").write_text(tpl.replace("/*DATA*/null", blob))
print("wrote index.html,", len(data["items"]), "items")
