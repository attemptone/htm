import cla_colloumn

class region():

	coll_groesse = 4
	max_groesse  = 20
    
	def __init__(self,groesse,input_groesse):
		self.colloums      = []
		self.input_groesse = input_groesse
		self.max_groesse = groesse
	
		for x in range(0,self.max_groesse):
			for y in range(0,self.max_groesse):
				pos = (x,y)
				self.add_Colloum(pos)

	# add a coloumn at a certain position and initializes a dendrit_segment
	def add_Colloum(self,pos):
		coll = cla_colloumn.colloum(self.coll_groesse,pos)
		coll.dendrit_segment.initialize_proximale_dendriten(self.input_groesse)
		self.colloums.append(coll)

	# returns a colloum by its position
	def coll_by_position(self,pos):
		for coll in self.colloums:
			if coll.position == pos:
				return coll

	# resets the overlap score of the colloums
	def reset_overlaps(self):		
		for coll in self.colloums:
			coll.overlap = 0

	def get_active_cells(self):
		active_cells = []
		for coll in self.colloums:
			for neuron in coll.neurons:
				if neuron.is_active():
					active_cells.append(neuron.pos)
		return activate_cells

# lets the winnercolloumn learn from their connections
	def learning(self,winners):
		for pos in winners:
			coll = self.coll_by_position(pos)
			coll.dendrit_segment.learning()
				

	# returns position of coll in the radius (the radius is a square not a circle)
	def nachbaren(self,pos,radius): 	
		nachbarlist = []
		pos_x 		= pos[0]
		pos_y 		= pos[1]
	
		x1 = pos_x - radius
		x2 = pos_x + radius
		y1 = pos_y - radius 
		y2 = pos_y + radius

		if x1 < 0:
			x1 = 0
		if y1 < 0:
			y1 = 0

		if x2 > self.max_groesse:
			x2 = self.max_groesse
		if y2 > self.max_groesse:
			y2 = self.max_groesse
		
		for x in range(x1,x2):
			for y in range(y1,y2):
				position = (x,y)
				nachbarlist.append(position)

		return nachbarlist

	# sets the overlap score for each colloumn
	def set_overlap(self,Input):
		for coll in self.colloums:
			coll.overlap = coll.dendrit_segment.get_overlap(Input)

