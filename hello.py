#from cgi import parse_qs
# 
#def app(environ, start_response):
#    start_response('200 OK', [('Content-type', 'text/plain')])
#    qs = parse_qs(environ['QUERY_STRING'])
#    return ['%s=%s\n' %(c,d) for c in qs for d in qs[c] ]
   
##
#import urlparse
#
#def app(environ, start_response):
#	qs = urlparse.parse_qs(environ['QUERY_STRING'])
#	start_response('200 OK', [('Content-type', 'text/plain')])
#	return ['%s=%s\n' %(c,d) for c in qs for d in qs[c] ]

#import urlparse

##
def app(environ, start_response):
	st = environ['QUERY_STRING']
	qs = st.split('&')
	start_response('200 OK', [('Content-type', 'text/plain')])
	return ['%s\n' %(c) for c in qs]	
