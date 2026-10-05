import re

def markdownToHtml(texto_markdown):
	texto_html = texto_markdown

	# Tratar casos do '#'
	texto_html = re.sub(r"^### (.*)$", r"<h3>\1</h3>", texto_html, flags=re.M)
	texto_html = re.sub(r"^## (.*)$", r"<h2>\1</h2>", texto_html, flags=re.M)
	texto_html = re.sub(r"^# (.*)$", r"<h1>\1</h1>", texto_html, flags=re.M)

	# Tratar link e imagem
	texto_html = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', texto_html)
	texto_html = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', texto_html)

	# Tratar bold e itálico
	texto_html = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", texto_html)
	texto_html = re.sub(r"\*(.*?)\*", r"<i>\1</i>", texto_html)

	# Tratar listas numeradas
	texto_html = re.sub(r"^\d+\.\s+(.*)$", r"<li>\1</li>", texto_html, flags=re.M)
	texto_html = re.sub(r"((?:<li>.*?</li>\n?)+)", r"<ol>\n\1\n</ol>", texto_html)


	return texto_html


with open("input.md", "r", encoding="utf-8") as f_in:
    conteudo_md = f_in.read()

conteudo_html = markdownToHtml(conteudo_md)

with open("output.html", "w", encoding="utf-8") as f_out:
    f_out.write(conteudo_html)

print("Ficheiro 'output.html' gerado.")