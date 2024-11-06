
def remove_gcodes(l, gcodes):
    return [line for line in l if not any(gcode in line for gcode in gcodes)]


bcu = None
drill = None
cutout = None

with open('bcu.gcode', 'r') as f:
    bcu = f.readlines()
with open('drill.gcode', 'r') as f:
    drill = f.readlines()
with open('cutout.gcode', 'r') as f:
    cutout = f.readlines()

if bcu is None or drill is None or cutout is None:
    print('Error reading files')
    exit(1)

bcu = remove_gcodes(bcu, ['M05'])
drill = remove_gcodes(drill, ['M05', 'G4', 'M03'])
cutout = remove_gcodes(cutout, ['G4', 'M03'])

with open('combined.gcode', 'w') as f:
    f.writelines(bcu)
    f.writelines(drill)
    f.writelines(cutout)

# copy to combined.fnc
with open('combined.gcode', 'r') as f:
    with open('combined.fnc', 'w') as f2:
        f2.write(f.read())

print('Sucessfully saved to combined.gcode and combined.fnc')