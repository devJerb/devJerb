from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from rich import box

console = Console(record=True, width=150, height=100)

directory = Tree("[link=https://www.facebook.com/gutierrez.jerby/]Jerome Gutierrez", guide_style="bold white")

# tools for web dev
path = directory.add("💻 Programming", guide_style="bold red")
path.add("JavaScript")
path.add("React")
path.add("Python")
path.add("PHP")
path.add("Java")

# bio
description = """
    Hello World!

    I am an undergraduate studying BS - CSE.

    I make [link=https://reactjs.org/]React[/] websites & back-end [link=https://www.python.org/]Python[/] apps.

    I love music, check my [link=https://soundcloud.com/gutierrez-jerome]Soundcloud[/]!
"""

# output
panel = Panel.fit(description, border_style="red", box=box.DOUBLE, title="Development Phase", width=60)
console.print(Columns([panel, directory]))
FORMAT = """
<pre style="font-family: 'Montserrat', sans-serif">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=FORMAT)
