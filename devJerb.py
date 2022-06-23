from rich.panel import Panel
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from rich import box

console = Console(record=True, width=200, height=50)

directory = Tree("[link=https://www.facebook.com/gutierrez.jerby/]Jerome Gutierrez")

path = directory.add("Web Development")
path.add("JS, HTML, & CSS")
framework = path.add("React JS")
framework.add("Bootstrap")
framework.add("Chakra")
framework.add("Three")

other = directory.add("Other Languages")
other.add("Python")
other.add("Java")
other.add("Dart")
other.add("C++")
other.add("SQL")


sites = directory.add("Competitive")
sites.add("[link=https://www.codewars.com/dashboard]Codewars")

description = """
    I'm an enthusiast of technology and its advancements; currently an undergraduate studying BS - CSE. I love gaming too!

    My forte is web development wherein I focus on [link=https://www.javascript.com/]Javascript[/], I do side projects with [link=https://www.python.org/]Python[/] and [link=https://www.java.com/en/]Java[/].
"""

panel = Panel.fit(description, box=box.DOUBLE, title="Development Phase", width=60)
console.print(Columns([panel, directory]))
FORMAT = """\
    <pre style="font-family: 'Montserrat', sans-serif,monospace">{code}</pre>
    """

console.save_html("README.md", inline_styles=True, code_format=FORMAT)