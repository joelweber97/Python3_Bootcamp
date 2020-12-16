import arcpy

arcpy.env.workspace = r'D:/test/dir'
arcpy.env.pyramid = 'None'
arcpy.env.rasterStatistics = 'None'
#save all the .tifs to a list.
rasters = arcpy.ListRasters('*.tif')
num_rasters = len(rasters)
print('{} rasters to process'.format(num_rasters))
count = 1
for r in rasters:
	output_name = r[:-4] + '_mod.tif'
	arcpy.Resample_management(r, output_name, '.0000050000000 .0000050000000', 'NEAREST')
	print('{} of {} rasters finished'.format(count, num_rasters)
	count += 1
	