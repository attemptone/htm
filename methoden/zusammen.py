import raum_methods

def raum(Input, region):
	print "		check overlap"
	raum_methods.get_overlap_onedim(Input, region)
	print "		get winners"
	winner = raum_methods.check_inhibition(region)
	print "		learning"
	raum_methods.learning(winner,region)


	
