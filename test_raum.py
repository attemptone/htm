import methoden
import encoder
import cla

region_groesse = 20
datei_pfad     = "/home/martin/Dokumente/htm/daten/test.csv"

if __name__ == "__main__":
	region = cla.region(region_groesse,258)

	datei  = encoder.open_file(datei_pfad)
	row    = encoder.convert_row(datei[0])
	name   = row[0]
	b = encoder.show_only_actives(name[0])

