## How to Run
```
pip3 install matplotlib
pip3 install pyexcel-xls
sudo apt-get install python3-tk
python3 main.py
```
## Functions: file (Visualizer.py)

### Constructor
`
constructor = parameters: array_polygons (array of type Polygon, required), title (String, required), x_lim (Integer, required) y_lim (Integer, required)
`

### plot_polygons

### plot_animation

## Functions: file (File.py)
###  polygons_from_xls
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: array of tuple (x,y), limit_x (int)
`

###  polygons_from_txt
`
parameters: file_name (String, required):
`

`
return: array of tuple (x,y), limit_x (int)
`

###  return_limits_of_board_xls
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: x_lim (float)
`

###  return_limits_of_board_txt
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: x_lim (float)
`
## Functions: file (Polygon.py)
### create_polygon
`
parameters: polygon_points (array of tuple (x,y), required):
`

`
return: Polygon()
`

### set_points_to_positive
`
parameters: polygon_points (array of tuple (x,y), required):
`

`
return: array of tuple (x,y)
`

### add_number_axis_x_y
`
parameters: polygon (array of tuple (x,y)), number_x (float), number_y (float):
`

`
return: array of tuple (x,y)
`

### area_polygon
`
parameters: polygon (array of tuple (x,y))
`

`
return: float
`

### sort_by_area(polygons):
`
parameters: polygons (array of array of tuple (x,y))
`

`
return: array of array of tuple (x,y)
`

### rotate_polygon
`
parameters: polygon (array of tuple (x,y)), angle (float)
`

`
return: array of tuple (x,y)
`

### is_overlapping
`
parameters: current_polygon (array of tuple (x,y)), polygon (array of tuple (x,y))
`

`
return: boolean
`

###create_polygons_to_plot
`
parameters: polygon (array of tuple (x,y))
`

`
return: List of type Polygon()
`

## Functions: file (BottomLeft.py)
### initial_solution
`
parameters: array_polygons (array of tuple (x,y), required):
`

`
return: List of type Polygon()
`
### solution
`
parameters: array_polygons (array of tuple (x,y), required), x_lim (float, required):
`

`
return: List of type Polygon(), float
`

### random_solution
`
parameters: array_polygons (array of tuple (x,y), required), x_lim (float, required):
`

`
return: List of type Polygon(), float
`
### sorted_by_area_solution
`
parameters: array_polygons (array of tuple (x,y), required), x_lim (float, required):
`

`
return: List of type Polygon(), float
`
### return_line_y
`
parameters: array_polygons (array of tuple (x,y):
`

`
return: float
`