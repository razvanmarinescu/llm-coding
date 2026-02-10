from src.text_utils import extract_emails, normalize_name, slugify


def test_normalize_name_collapses_spaces() -> None:
    assert normalize_name("  aLiCe   mArinescu  ") == "Alice Marinescu"


def test_slugify_removes_punctuation() -> None:
    assert slugify("LLM Workflow: Week 1!") == "llm-workflow-week-1"


def test_extract_emails_multiple() -> None:
    text = "Contact a@x.com, b.y@lab.edu; ignore no-at-symbol."
    assert extract_emails(text) == ["a@x.com", "b.y@lab.edu"]

