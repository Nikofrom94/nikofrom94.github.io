import csv
abilities = []

with open('/home/niko/Documents/jdr/CypherSystem/Cypher-SRD-FR/CSCG/cscgsite/ability.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    skipfirst = False
    for row in reader:
        if not skipfirst:
            skipfirst = True
            continue
        abilities.append(row)

with open('index-fr.html','r',encoding='utf-8') as input_file, open('index.temp.html','w',encoding='utf-8',newline='') as outut_file:
    for buffer in input_file:
        for ab in abilities:
            skip = False
            input_string = '<p><strong>{}:</strong> '.format(ab['name'])
            if len(ab['stat']) > 0:
                if '(' in ab['stat']:
                    output_string = '<p><strong>{0} {1}:</strong> '.format(ab['name'], ab['stat'])
                else:
                    output_string = '<p><strong>{0} ({1}):</strong> '.format(ab['name'], ab['stat'])
            else:
                skip = True
            if not skip:
                buffer = buffer.replace(input_string, output_string)
        print(buffer.strip('\n'),file=outut_file)


