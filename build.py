print("Building Static Sites")


pages = [
{"filename": "content/index.html",
"output":	"docs/index.html",
"title": "About Me",
},

{"filename": "content/projects.html",
"output": "docs/projects.html",
"title": "Projects",
},

{"filename": "content/contact.html",
"output": "docs/contact.html",
"title": "Contact",
}
]

#loop
def main():
	for page in pages:
		file_name = page["filename"]
		output = page["output"]
		title = page["title"]
		content = open(file_name).read()
		full_page = apply_template(content, title)
		final_output = produce_output(output, full_page)
		



#templating
def apply_template(content, title):
	template = open("templates/base.html").read()
	template_with_content = template.replace("{{content}}", content)
	full_page = template_with_content.replace("{{title}}", title)
	return full_page


#produce output
def produce_output(output, full_page):
	open(output, 'w+').write(full_page)

 
main()



#previous code for reference.

# print('building static site')
# 	top_html = open('templates/top.html').read()
# 	bottom_html = open('templates/bottom.html').read()

# 	#index
# 	middle_html = open('content/index.html').read()
# 	combined_html = top_html + middle_html + bottom_html
# 	open('docs/index.html', 'w+').write(combined_html)

# 	#projects
# 	print('building static site')
# 	middle_html = open('content/projects.html').read()
# 	combined_html = top_html + middle_html + bottom_html
# 	open('docs/projects.html', 'w+').write(combined_html)

# 	#contact
# 	print('building static site')
# 	middle_html = open('content/contact.html').read()
# 	combined_html = top_html + middle_html + bottom_html
# 	open('docs/contact.html', 'w+').write(combined_html)
