x	=	"""designation,name,period_years,last_perihelion,next_perihelion
C/1989 A3,Bradfield,81.9,1988/12/05,2070/11/01
C/1991 L3,Levy,51.28,1991/07/08,2042/10/19
C/2005 N5,Catalin,153.65,2005/08/22,2159/01/01
C/2005 O2,Christensen,115.43,2005/09/08,2121/02/15
C/2011 L1,McNaught,36.66,2010/12/18,2047/08/15
C/2011 S2,Kowalski,65.83,2011/10/26,2077/08/25
C/2013 V3,Nevsky,45.36,2013/10/29,2059/03/09
C/2014 Q3,Borisov,151.64,2014/11/19,2166/07/10
C/2015 H1,Bressi,185.5,2015/03/28,2200/10/07
"""
#Halley	not	in	list

import	csv
rd = csv.DictReader(x.split('\n'))
for	row	in	rd:
    print(row)

simple_list	=	[
				"ceres",
				"vesta",
				"pallas",
				"hygiea",
				"euphrosyne"
]

discovered_dict	=	{
				'ceres':	'1801-01-01',
				'vesta':	'1807-03-29',
				'pallas':	'1802-03-28',
				'hygiea':	'1849-04-12',
				'euphrosyne':	'1854-09-01',
}

#	Required	Keys:	minor_planet_designation,	discovered_by,	discovered_date
#	Optional	Keys:	approx_mean_diameter_km,	max_surface_temp_kelvin

complex_dict	=	{
				"ceres":	{
								"minor_planet_designation":	"(1)	Ceres",
								"discovered_by":	"Giuseppe	Piazzi",
								"discovered_date":	"1801-01-01",
								"approx_mean_diameter_km":	939,
								"max_surface_temp_kelvin":	155,
				},
				"vesta":	{
								"minor_planet_designation":	"(4)	Vesta",
								"discovered_by":	"Heinrich	Wilhelm	Olbers",
								"discovered_date":	"1807-03-29",
								"approx_mean_diameter_km":	525,
								"max_surface_temp_kelvin":	270,
				},
				"pallas":	{
								"minor_planet_designation":	"(2)	Pallas",
								"discovered_by":	"Heinrich	Wilhelm	Olbers",
								"discovered_date":	"1802-03-28",
								"approx_mean_diameter_km":	512,
				},
				"hygiea":	{
								"minor_planet_designation":	"(10)	Hygiea",
								"discovered_by":	"Annibale	de	Gasparis",
								"discovered_date":	"1849-04-12",
								"approx_mean_diameter_km":	434,
				},
				"euphrosyne":	{
								"minor_planet_designation":	"(31)	Euphrosyne",
								"discovered_by":	"James	Ferguson",
								"discovered_date":	"1854-09-01",
				},
}
