# trace generated using paraview version 5.6.2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

import numpy as np

import os

py_path = os.path.dirname(os.path.abspath(__file__))

print(py_path)

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
pNTest_1vtp = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1247, 818]

# show data in view
pNTest_1vtpDisplay = Show(pNTest_1vtp, renderView1)

# trace defaults for the display properties.
pNTest_1vtpDisplay.Representation = 'Surface'
pNTest_1vtpDisplay.ColorArrayName = [None, '']
pNTest_1vtpDisplay.OSPRayScaleArray = 'network | net_01 | labels | pore.all'
pNTest_1vtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pNTest_1vtpDisplay.SelectOrientationVectors = 'None'
pNTest_1vtpDisplay.ScaleFactor = 3.0399999999999997e-05
pNTest_1vtpDisplay.SelectScaleArray = 'None'
pNTest_1vtpDisplay.GlyphType = 'Arrow'
pNTest_1vtpDisplay.GlyphTableIndexArray = 'None'
pNTest_1vtpDisplay.GaussianRadius = 1.5199999999999998e-06
pNTest_1vtpDisplay.SetScaleArray = ['POINTS', 'network | net_01 | labels | pore.all']
pNTest_1vtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pNTest_1vtpDisplay.OpacityArray = ['POINTS', 'network | net_01 | labels | pore.all']
pNTest_1vtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pNTest_1vtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
pNTest_1vtpDisplay.SelectionCellLabelFontFile = ''
pNTest_1vtpDisplay.SelectionPointLabelFontFile = ''
pNTest_1vtpDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pNTest_1vtpDisplay.OSPRayScaleFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pNTest_1vtpDisplay.ScaleTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pNTest_1vtpDisplay.OpacityTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
pNTest_1vtpDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.DataAxesGrid.XTitleFontFile = ''
pNTest_1vtpDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.DataAxesGrid.YTitleFontFile = ''
pNTest_1vtpDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.DataAxesGrid.ZTitleFontFile = ''
pNTest_1vtpDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.DataAxesGrid.XLabelFontFile = ''
pNTest_1vtpDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.DataAxesGrid.YLabelFontFile = ''
pNTest_1vtpDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
pNTest_1vtpDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.PolarAxes.PolarAxisTitleFontFile = ''
pNTest_1vtpDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.PolarAxes.PolarAxisLabelFontFile = ''
pNTest_1vtpDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
pNTest_1vtpDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
pNTest_1vtpDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(Input=pNTest_1vtp,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 3.0399999999999997e-05
glyph1.GlyphTransform = 'Transform2'

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = [None, '']
glyph1Display.OSPRayScaleArray = 'network | net_01 | labels | pore.all'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 3.344e-05
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 1.6719999999999998e-06
glyph1Display.SetScaleArray = ['POINTS', 'network | net_01 | labels | pore.all']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'network | net_01 | labels | pore.all']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.SelectionCellLabelFontFile = ''
glyph1Display.SelectionPointLabelFontFile = ''
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
glyph1Display.OSPRayScaleFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.XTitleFontFile = ''
glyph1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.YTitleFontFile = ''
glyph1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.ZTitleFontFile = ''
glyph1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.XLabelFontFile = ''
glyph1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.YLabelFontFile = ''
glyph1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
glyph1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
glyph1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
glyph1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
glyph1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# set scalar coloring
ColorBy(glyph1Display, ('POINTS', 'network | net_01 | properties | pore.pressure'))

# rescale color and/or opacity maps used to include current data range
glyph1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'networknet_01propertiesporediameter'
networknet_01propertiesporediameterLUT = GetColorTransferFunction('networknet_01propertiesporediameter')

# get opacity transfer function/opacity map for 'networknet_01propertiesporediameter'
networknet_01propertiesporediameterPWF = GetOpacityTransferFunction('networknet_01propertiesporediameter')

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'
glyph1.ScaleArray = ['POINTS', 'network | net_01 | properties | pore.diameter']
glyph1.ScaleFactor = 1.0

# show data in view
glyph1Display = Show(glyph1, renderView1)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(pNTest_1vtp)

# create a new 'Shrink'
shrink1 = Shrink(Input=pNTest_1vtp)

# set active source
SetActiveSource(shrink1)

# show data in view
shrink1Display = Show(shrink1, renderView1)

# trace defaults for the display properties.
shrink1Display.Representation = 'Surface'
shrink1Display.ColorArrayName = [None, '']
shrink1Display.OSPRayScaleArray = 'network | net_01 | labels | pore.all'
shrink1Display.OSPRayScaleFunction = 'PiecewiseFunction'
shrink1Display.SelectOrientationVectors = 'None'
shrink1Display.ScaleFactor = 3.0199998650459748e-05
shrink1Display.SelectScaleArray = 'None'
shrink1Display.GlyphType = 'Arrow'
shrink1Display.GlyphTableIndexArray = 'None'
shrink1Display.GaussianRadius = 1.5099999325229875e-06
shrink1Display.SetScaleArray = ['POINTS', 'network | net_01 | labels | pore.all']
shrink1Display.ScaleTransferFunction = 'PiecewiseFunction'
shrink1Display.OpacityArray = ['POINTS', 'network | net_01 | labels | pore.all']
shrink1Display.OpacityTransferFunction = 'PiecewiseFunction'
shrink1Display.DataAxesGrid = 'GridAxesRepresentation'
shrink1Display.SelectionCellLabelFontFile = ''
shrink1Display.SelectionPointLabelFontFile = ''
shrink1Display.PolarAxes = 'PolarAxesRepresentation'
shrink1Display.ScalarOpacityUnitDistance = 3.82840420104395e-05

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
shrink1Display.OSPRayScaleFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
shrink1Display.ScaleTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
shrink1Display.OpacityTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
shrink1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.XTitleFontFile = ''
shrink1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.YTitleFontFile = ''
shrink1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.ZTitleFontFile = ''
shrink1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.XLabelFontFile = ''
shrink1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.YLabelFontFile = ''
shrink1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
shrink1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
shrink1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
shrink1Display.PolarAxes.PolarAxisTitleFontFile = ''
shrink1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
shrink1Display.PolarAxes.PolarAxisLabelFontFile = ''
shrink1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
shrink1Display.PolarAxes.LastRadialAxisTextFontFile = ''
shrink1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
shrink1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# Properties modified on shrink1
shrink1.ShrinkFactor = 1.0

# show data in view
shrink1Display = Show(shrink1, renderView1)

# hide data in view
Hide(pNTest_1vtp, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=shrink1)

# set active source
SetActiveSource(cellDatatoPointData1)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Surface'
cellDatatoPointData1Display.ColorArrayName = [None, '']
cellDatatoPointData1Display.OSPRayScaleArray = 'network | net_01 | labels | pore.all'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'None'
cellDatatoPointData1Display.ScaleFactor = 3.039999941165661e-05
cellDatatoPointData1Display.SelectScaleArray = 'None'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'None'
cellDatatoPointData1Display.GaussianRadius = 1.5199999705828304e-06
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'network | net_01 | labels | pore.all']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'network | net_01 | labels | pore.all']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.SelectionCellLabelFontFile = ''
cellDatatoPointData1Display.SelectionPointLabelFontFile = ''
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 3.860145397968146e-05

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
cellDatatoPointData1Display.OSPRayScaleFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
cellDatatoPointData1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.XTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.YTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.ZTitleFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.XLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.YLabelFontFile = ''
cellDatatoPointData1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisTitleFontFile = ''
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.PolarAxisLabelFontFile = ''
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.LastRadialAxisTextFontFile = ''
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
cellDatatoPointData1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# hide data in view
Hide(shrink1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(Input=cellDatatoPointData1)

# set active source
SetActiveSource(extractSurface1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.ColorArrayName = [None, '']
extractSurface1Display.OSPRayScaleArray = 'network | net_01 | labels | pore.all'
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.SelectOrientationVectors = 'None'
extractSurface1Display.ScaleFactor = 3.039999941165661e-05
extractSurface1Display.SelectScaleArray = 'None'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.GlyphTableIndexArray = 'None'
extractSurface1Display.GaussianRadius = 1.5199999705828304e-06
extractSurface1Display.SetScaleArray = ['POINTS', 'network | net_01 | labels | pore.all']
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityArray = ['POINTS', 'network | net_01 | labels | pore.all']
extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface1Display.SelectionCellLabelFontFile = ''
extractSurface1Display.SelectionPointLabelFontFile = ''
extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface1Display.OSPRayScaleFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface1Display.ScaleTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface1Display.OpacityTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
extractSurface1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.XTitleFontFile = ''
extractSurface1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.YTitleFontFile = ''
extractSurface1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.ZTitleFontFile = ''
extractSurface1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.XLabelFontFile = ''
extractSurface1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.YLabelFontFile = ''
extractSurface1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
extractSurface1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
extractSurface1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.PolarAxisTitleFontFile = ''
extractSurface1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.PolarAxisLabelFontFile = ''
extractSurface1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.LastRadialAxisTextFontFile = ''
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
extractSurface1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# set active source
SetActiveSource(shrink1)

# show data in view
shrink1Display = Show(shrink1, renderView1)

# set active source
SetActiveSource(extractSurface1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView1)

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Tube'
tube1 = Tube(Input=extractSurface1)
tube1.Scalars = ['POINTS', 'network | net_01 | labels | pore.all']
tube1.Vectors = [None, '1']
tube1.Radius = 3.039999941165661e-06

# set active source
SetActiveSource(tube1)

# show data in view
tube1Display = Show(tube1, renderView1)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = [None, '']
tube1Display.OSPRayScaleArray = 'TubeNormals'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'None'
tube1Display.ScaleFactor = 3.089122690198565e-05
tube1Display.SelectScaleArray = 'None'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'None'
tube1Display.GaussianRadius = 1.5445613450992823e-06
tube1Display.SetScaleArray = ['POINTS', 'TubeNormals']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'TubeNormals']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.SelectionCellLabelFontFile = ''
tube1Display.SelectionPointLabelFontFile = ''
tube1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display.OSPRayScaleFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [0.10805884065089633, 0.0, 0.5, 0.0, 1080.5884065089633, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tube1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
tube1Display.DataAxesGrid.XTitleFontFile = ''
tube1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
tube1Display.DataAxesGrid.YTitleFontFile = ''
tube1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
tube1Display.DataAxesGrid.ZTitleFontFile = ''
tube1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
tube1Display.DataAxesGrid.XLabelFontFile = ''
tube1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
tube1Display.DataAxesGrid.YLabelFontFile = ''
tube1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
tube1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
tube1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
tube1Display.PolarAxes.PolarAxisTitleFontFile = ''
tube1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
tube1Display.PolarAxes.PolarAxisLabelFontFile = ''
tube1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
tube1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tube1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
tube1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# set active source
SetActiveSource(cellDatatoPointData1)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# set active source
SetActiveSource(tube1)

# Properties modified on tube1
tube1.Vectors = [None, '']

# show data in view
tube1Display = Show(tube1, renderView1)

# hide data in view
Hide(extractSurface1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tube1Display, ('POINTS', 'network | net_01 | properties | pore.pressure'))

# rescale color and/or opacity maps used to include current data range
tube1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'networknet_01propertiesthroatdiameter'
networknet_01propertiesthroatdiameterLUT = GetColorTransferFunction('networknet_01propertiesthroatdiameter')

# get opacity transfer function/opacity map for 'networknet_01propertiesthroatdiameter'
networknet_01propertiesthroatdiameterPWF = GetOpacityTransferFunction('networknet_01propertiesthroatdiameter')

# Properties modified on tube1
tube1.Scalars = ['POINTS', 'network | net_01 | properties | throat.diameter']
# paraview_params = np.loadtxt('/Users/bigelk/data/projects/mincutPN/PNM/paraview_params.txt')
paraview_params = np.loadtxt(py_path + '/paraview_params.txt')
tube1.Radius = paraview_params[0]
tube1.VaryRadius = 'By Scalar'
tube1.RadiusFactor = paraview_params[1]

# update the view to ensure updated data information
renderView1.Update()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.000153, 0.000153, 0.0011702038253451742]
renderView1.CameraFocalPoint = [0.000153, 0.000153, 0.000153]
renderView1.CameraParallelScale = 0.0002632717227504693

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).