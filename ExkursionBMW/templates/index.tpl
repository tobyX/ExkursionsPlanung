<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	{% load static %}
	{% get_static_prefix as STATIC_PREFIX %}
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	<title>Exkursion BMW</title>
	<link href="{{ STATIC_PREFIX }}cars-website-template.css" rel="stylesheet" type="text/css" />
</head>

<body>
    <div id="border">
    	<div id="left10">
    		<div class="name">Exkursion BMW</div>
    		<div class="tag">Built for the road ahead.</div>
		</div>
		<div id="car"></div>
		<div id="links-bg">
			<div class="toplinks"><a href="/">Anmelden</a></div>
			<div class="toplinks"><a href="/liste/">Liste anzeigen</a></div>
		</div>

		<div id="mainarea">

			<div id="headingbg">{% block title %}Exkursion BMW{% endblock %}</div>
			<div class="headingbg2"></div>
			<div style="background-image: url({{ STATIC_PREFIX }}images/bg2.gif); background-repeat: repeat-y; float: left;">
				<div id="left">
					<div id="main">
						{% block content %}{% endblock %}
					</div>
				</div>
				<div id="right">

				</div>
			</div>
		</div>
		<div class="headingbg2"></div>
		<div id="bottom">

        </div>

		<center>
		<div class="quicklinks">Designed by <a href="http://www.cmgtechnologies.com/" target="_blank">CMG Technologies</a>,
			Free <a href="http://www.cmgtechnologies.com/free-css-templates.php" target="_blank">CSS Templates</a>
		</div>
	</div>
</body>
</html>