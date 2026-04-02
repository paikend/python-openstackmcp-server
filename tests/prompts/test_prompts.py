from openstack_mcp_server.prompts import register_prompt


def test_get_servers_by_security_group_prompt_registered():
    """Test that the prompt is registered with the MCP instance."""
    from unittest.mock import MagicMock

    mcp = MagicMock()
    register_prompt(mcp)
    mcp.prompt.assert_called()


def test_get_servers_by_security_group_prompt_content():
    """Test that the prompt returns expected content."""
    from fastmcp import FastMCP

    mcp = FastMCP("test")
    register_prompt(mcp)

    prompts = mcp._prompt_manager._prompts
    assert "get_servers_by_security_group" in prompts

    prompt_obj = prompts["get_servers_by_security_group"]
    assert prompt_obj.fn is not None

    result = prompt_obj.fn(security_group_name="my-sg")
    assert "my-sg" in result
    assert "get_servers" in result
    assert "security_groups" in result
