###select airport.name, country.name
from airport inner join country on
airport.iso_country=country.iso_country where country.name='Nepal';###

###select count(name) from airport where iso_country='FI';###