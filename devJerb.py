from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from rich import box

console = Console(record=True, width=150, height=100)

directory = Tree("[link=https://www.facebook.com/gutierrez.jerby/]Jerome Gutierrez", guide_style="bold white")

# tools for web dev
path = directory.add("💻 Web Development", guide_style="bold blue")
path.add("JS, HTML, & CSS")
framework = path.add("React JS")
framework.add("Bootstrap")
framework.add("Chakra")
framework.add("Three")

# other languages known
other = directory.add("👀 Other Languages", guide_style="bold yellow")
other.add("Python")
other.add("Java")
other.add("Dart")
other.add("C++")
other.add("SQL")

# competitive site/s
sites = directory.add("⚔️  Competitive", guide_style="bold red")
sites.add("[link=https://www.codewars.com/dashboard]Codewars")

# bio
description = """
    Hi!👋, I'm an enthusiast of technology;
    currently an undergraduate studying BS - CSE.

    I like making websites! I focus on [link=https://www.javascript.com/]Javascript[/].
    I do side projects with [link=https://www.python.org/]Python[/] and [link=https://www.java.com/en/]Java[/].

    I love music so catch me on [link=https://soundcloud.com/discover]Soundcloud[/]! 🎶 
"""

# output
panel = Panel.fit(description, border_style="red", box=box.DOUBLE, title="Development Phase", width=60)
console.print(Columns([panel, directory]))
FORMAT = """
<pre style="font-family: 'Montserrat', sans-serif">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=FORMAT)