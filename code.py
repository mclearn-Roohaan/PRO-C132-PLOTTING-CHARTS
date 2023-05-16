import csv 
data=[]
csv.dropna()
 
with open("archive_dataset.csv",'r') as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data.append(row)
headers=data[0]
planet_data=data[1:]

for data_point in planet_data:
    data_point[2]=data_point[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("sorted.csv","a+")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)

with open('sorted.csv') as input, open('sorted1.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)

load_duplicate_colum=False

distance = 2 * 3.14 * (float(planet_data[8].split(" ")[0]) * 1.496e+9)

distance = 2 * 3.14 * (float(planet_data[8].split(" ")[0]) * 6.957e+8)

  gravity_planet = 0
  for key, value in csv.writer():
    if "gravity" in value:
    gravity_planet += 1

  print(gravity_planet)

planet_masses.append(planet_data[3])
planet_radiuses.append(planet_data[7])

if planet_masses < 1.898*10^27 *10 :
      features_list.append("mass")
      planet_data.append(planet_masses) 

if plane_radius < 1.898*10^27 *10 :
      features_list.append("planet_radius")
      planet_data.append(planet_radius) 

fig = px.scatter(x=planet_masses,y=planet_radius)
fig.show()

list={"radius","mass","gravity"}

planet_masses = []
planet_radiuses = []
planet_types = []
for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_types.append(planet_data[6])

fig = px.scatter(x=planet_radiuses, y=planet_masses, color=planet_types)
fig.show()