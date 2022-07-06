from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from rich import box

console = Console(record=True, width=50)

directory = Tree("[link=https://www.facebook.com/gutierrez.jerby/]Jerome Gutierrez", guide_style="bold white")

# tools for web dev
path = directory.add("💻 Programming", guide_style="bold blue")
path.add("JavaScript")
path.add("React")
path.add("Java")
path.add("Python")

# bio
description = """
    Hi!👋, I like technology!

    I am an undergraduate studying BS - CSE.

    I like making websites! I focus on [link=https://www.javascript.com/]Javascript[/].

    I love music check my [link=https://soundcloud.com/discover]Soundcloud[/]! 🎶 
"""

# output
panel = Panel.fit(description, border_style="red", box=box.DOUBLE, title="Hello World!", width=50)
console.print(Columns([panel, directory]))
FORMAT = """
<pre style="font-family: 'Montserrat', sans-serif">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=FORMAT)