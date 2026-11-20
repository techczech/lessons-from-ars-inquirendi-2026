"""Build index.html (searchable list) and map.html (pipeline map) from data/.
Usage: python3 build.py"""
import json, pathlib

here = pathlib.Path(__file__).parent
data = json.loads((here / "data" / "conference-resources-2026.json").read_text())
ins = json.loads((here / "data" / "map-insights.json").read_text())
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
(here / "index.html").write_text((here / "template.html").read_text().replace("/*DATA*/null", blob))
(here / "map.html").write_text((here / "template-map.html").read_text().replace("/*DATA*/null", blob)
                               .replace("/*INSIGHTS*/[]", json.dumps(ins, ensure_ascii=False)))
print("wrote index.html and map.html,", len(data["items"]), "items")
