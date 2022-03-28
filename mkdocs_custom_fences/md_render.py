"""Generate markdown embed in code blocks.
Credit @facelessuser/pydown-extension
https://github.com/facelessuser/pymdown-extensions/blob/main/tools/pymdownx_md_render.py
"""
import markdown
import yaml
import re
from collections import OrderedDict

def md_sub_render(src="", language="", class_name=None, options=None, md="", **kwargs):
    """Formatter wrapper."""
    try:
        md = markdown.markdown(
            src,
            extensions=[
                "nl2br",
                "footnotes",
                "attr_list",
                "mdx_breakless_lists",
                "smarty",
                "sane_lists",
                "tables",
                "admonition",
                "mdx_wikilink_plus"]
        )
        return md
    except Exception:
        import traceback
        print(traceback.format_exc())
        raise
