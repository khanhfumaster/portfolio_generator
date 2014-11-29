import time
from yattag import Doc

class PortfolioPage:
	def __init__(self, projects):
		self.timestamp = time.strftime("%H:%M %d/%m/%Y")
		self.generate_html(projects)

	def generate_html(self, projects):
		doc, tag, text = Doc().tagtext()
		doc.asis('<!DOCTYPE html>')
		with tag('html'):
			# HEAD
			with tag('head'):
				# Bootstrap CSS
				doc.asis('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">')
				doc.asis('<link rel="stylesheet" href="css/style.css">')
				doc.asis('<link rel="stylesheet" href="css/font-awesome.min.css">')
				doc.asis('<link rel="stylesheet" href="css/font-mfizz.css">')
				# jQuery
				doc.asis('<script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>')
				# Bootstrap Javascript
				doc.asis('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>')

			# BODY
			with tag('body'):
				with tag('div', klass='col-md-12'):
					with tag('div', klass='container'):
						with tag('h1'):
							text('Portfolio')
						with tag('small'):
							text("Generated by Portfolio Generator %s." % (self.timestamp) )
						# Projects
						with tag('div', klass='projects'):
							for project in projects:
								with tag('div', klass='project', id=project.friendly_name):
									# Project Title
									with tag('h2', klass='title'):
										text(project.name, " ")

										# Tech icons
										icons = self.get_tech_icons(project.technologies)
										for icon in icons:
											doc.asis(icon)

										# Organisation
									if hasattr(project, 'organisation') or project.type == 'personal':
										label_type = 'label-primary'
										if project.type == 'personal':
											label_type = 'label-default'
											project.organisation = 'Personal'
										elif project.type == 'uni':
											label_type = 'label-warning'
										elif project.type == 'hackathon':
											label_type = 'label-success'

										with tag('span', klass='label %s' % (label_type)):
											text(project.organisation)

									# Description
									with tag('p', klass='description'):
										text(project.description)
									
									# List of technologies
									with tag('div', klass='tech-list'):
										with tag('h3'):
											text('Technologies')
										with tag('ul'):
											for tech in project.technologies:
												with tag('li'):
													text(tech)

										# List of relevant URLs
										if hasattr(project, 'urls'):
											with tag('h3'):
												text('Links')
											with tag('ul'):
												for url in project.urls:
													with tag('li'):
														with tag('a', ('href', url)):
															text(url)

										# Images
										if hasattr(project, 'images'):
											with tag('div', klass='images'):
												for image in project.images:
													doc.asis('<img src="%s" class="image"></img>' % image)
										doc.stag('hr')
		self.html = doc.getvalue()

	def get_tech_icons(self, technologies):
		techs = []
		if 'Ruby on Rails' in technologies:
			techs.append('<i class="icon-ruby-on-rails-alt"></i>')
			techs.append('<i class="icon-ruby"></i>')
		if 'Groovy on Grails' in technologies or 'Grails' in technologies:
			techs.append('<i class="icon-grails"></i>')
		if 'Nginx' in technologies:
			techs.append('<i class="icon-nginx"></i>')
		if 'Tomcat' in technologies:
			techs.append('<i class="icon-tomcat"></i>')
		if 'PostgreSQL' in technologies:
			techs.append('<i class="icon-postgres"></i>')
		if 'AWS' in technologies:
			techs.append('<i class="icon-aws"></i>')
		if 'PHP' in technologies:
			techs.append('<i class="icon-php"></i>')
		if 'Python' in technologies or 'Pyramid' in technologies or 'Pylons' in technologies:
			techs.append('<i class="icon-python"></i>')
		if 'Node.js' in technologies:
			techs.append('<i class="icon-nodejs"></i>')
		if 'Android' in technologies:
			techs.append('<i class="fa fa-android"></i>')
		if 'iOS' in technologies:
			techs.append('<i class="fa fa-apple"></i>')
		if 'jQuery' in technologies:
			techs.append('<i class="icon-javascript"></i>')

		return techs