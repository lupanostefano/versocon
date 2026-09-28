"""pdf.js: il percorso vulnerabile a CVE-2024-4367 deve restare disattivato.

La 3.11.174 inclusa in `static/vendor/pdfjs/` rientra nelle versioni affette
(0.8.1181 -> 4.1.392, corretta in 4.2.67). Finche' non si aggiorna il vendor,
ogni `getDocument` deve passare `isEvalSupported: false`, che disattiva la
compilazione dei glifi in `Function` da cui dipende la vulnerabilita'.
"""
import re
from pathlib import Path

import pytest

STATIC = Path(__file__).resolve().parent.parent / "static"

# Versione di pdf.js attualmente nel bundle. Se aggiorni il vendor, aggiorna
# anche questa costante: serve a forzare una riverifica dello stato CVE.
BUNDLED_PDFJS = "3.11.174"
PDFJS_FIXED_IN = (4, 2, 67)


def _app_js() -> str:
    return (STATIC / "app.js").read_text(encoding="utf-8")


def _get_document_calls(js: str) -> list[str]:
    """Restituisce il testo di ogni chiamata `getDocument({...})`."""
    return re.findall(r"getDocument\(\s*\{.*?\}\s*\)", js, re.DOTALL)


def test_bundled_pdfjs_version_is_pinned():
    src = (STATIC / "vendor" / "pdfjs" / "pdf.min.js").read_text(encoding="utf-8", errors="replace")
    m = re.search(r'version\s*=\s*"(\d+\.\d+\.\d+)"', src)
    assert m, "versione di pdf.js non trovata in pdf.min.js"
    assert m.group(1) == BUNDLED_PDFJS, (
        f"pdf.js e' passato da {BUNDLED_PDFJS} a {m.group(1)}: aggiorna BUNDLED_PDFJS "
        "e verifica se la mitigazione isEvalSupported e' ancora necessaria "
        f"(CVE-2024-4367 e' corretta in {'.'.join(map(str, PDFJS_FIXED_IN))})."
    )


def test_every_get_document_disables_eval():
    calls = _get_document_calls(_app_js())
    assert len(calls) >= 2, f"attese almeno 2 chiamate getDocument, trovate {len(calls)}"
    for call in calls:
        assert "isEvalSupported: false" in call, (
            "chiamata getDocument senza `isEvalSupported: false` "
            f"(CVE-2024-4367, pdf.js {BUNDLED_PDFJS}):\n{call}"
        )


@pytest.mark.parametrize("marker", [
    "data: buf, password: edPdfPw || undefined, isEvalSupported: false",
    "data, isEvalSupported: false",
])
def test_known_call_sites_are_patched(marker):
    assert marker in _app_js(), f"call site non patchato: {marker}"
