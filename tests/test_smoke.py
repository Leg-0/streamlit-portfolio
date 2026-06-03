"""Smoke tests: run the whole app via Streamlit's AppTest and assert the
core sections render without uncaught exceptions.

Note: under AppTest's bare mode the `streamlit-pdf` component can't register
(it needs a real server), so `st.pdf` raises a harness-only exception. We
tolerate that one specific error and fail on anything else.
"""

from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parent.parent / "app.py")


def _run():
    return AppTest.from_file(APP, default_timeout=30).run()


def test_app_runs_without_unexpected_exceptions():
    at = _run()
    unexpected = [e for e in at.exception if "streamlit-pdf" not in e.message]
    assert not unexpected, [e.message for e in unexpected]


def test_core_sections_render():
    at = _run()
    headers = [h.value for h in at.header]
    # "Contact" is intentionally omitted: it renders after st.pdf, which halts the
    # script under AppTest's bare mode (see module docstring). All sections up to
    # and including the resume header should render.
    for section in ("Experience", "Certifications", "Skills", "Education", "Resume"):
        assert section in headers, f"missing section header: {section}"


def test_resume_update_date_renders():
    at = _run()
    subheaders = [s.value for s in at.subheader]
    assert any(s.startswith("Latest update:") for s in subheaders), subheaders
