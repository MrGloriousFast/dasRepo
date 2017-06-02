
class Cube:
	def __init__(self,length,pos):
		self.length = length
		self.pos = pos
		
		#8 corners in a cube
		self.vertices = (pos,
						(pos[0]+self.length , pos[1], pos[2]),
						(pos[0]+self.length , pos[1]+self.length, pos[2]),
						(pos[0] , pos[1]+self.length, pos[2]),
						
						(pos[0] , pos[1], pos[2]+self.length)
						(pos[0]+self.length , pos[1], pos[2]+self.length),
						(pos[0]+self.length , pos[1]+self.length, pos[2]+self.length),
						(pos[0] , pos[1]+self.length, pos[2]+self.length))
						
						
		self.edges = (
			(0,1),
			(1,2),
			(2,3),
			(3,0),
			(0,4),
			(1,5),
			(2,5),
			(3,7),
			(4,5),
			(5,6),
			(6,7),
			(7,0))

		self.surfaces = (
				(0,1,2,3), #boden
				(0,1,5,4),
				(1,2,5,6),
				(2,3,7,6),
				(0,3,7,4),
				(4,5,6,7))#deckel


				
	def render():

		#drawing the edges
		glBegin(GL_LINES)
		glColor3fv((0,0,0))
		for edge in self.edges:
			for vertex in self.vertices:
				glVertex3fv(vertices[vertex])
		glEnd()
		
		
		
