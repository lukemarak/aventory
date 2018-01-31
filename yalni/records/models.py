from django.db import models

class Assembled(models.Model):
	customer = models.CharField(max_length=100)
	CHASIS_MODEL = (
		('510', 'IPC-510'),
		('610', 'IPC-610'),
		('A4000', 'ACP-4000'),
		('A4320', 'ACP-4320'),
		('A2010', 'ACP-2010'),
		('A4340', 'ACP-4340'),
		('A4360', 'ACP-4360'),
		
	)
	chasis = models.CharField(max_length=50, choices=CHASIS_MODEL)
	chasis_serial = models.CharField(max_length=50)
	
	MOTHERBOARDS = (
		('I701', 'AIMB-701'),
		('I767', 'AIMB-767'),
		('I769', 'AIMB-769'),
		('I780', 'AIMB-780'),
		('I781', 'AIMB-781'),
		('I782', 'AIMB-782'),
		('I785', 'AIMB-785'),
		('I784', 'AIMB-784'),
		('S584', 'ASMB-584'),
		('S784', 'ASMB-784'),
		('S785', 'ASMB-785'),
		('S781', 'ASMB-781'),
		('S782', 'ASMB-782'),
	)
	
	motherboard = models.CharField(max_length=50, choices=MOTHERBOARDS)
	board_serial = models.CharField(max_length=50)
	configuration = models.TextField(blank=True)
	others = models.TextField(blank=True)
	
	entered = models.DateTimeField(auto_now_add=True)
	
	
	class Meta:
		ordering = ('entered'),
		
	def __str__(self):
		return self.customer
	