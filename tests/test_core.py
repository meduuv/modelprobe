from modelprobe import capabilities


def test_capabilities_normalize_values():
    assert capabilities({"capabilities": "chat, tools"}) == {"chat", "tools"}
