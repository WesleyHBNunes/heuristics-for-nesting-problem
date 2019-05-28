## How to Run
```
pip3 install matplotlib
pip3 install pyexcel-xls
sudo apt-get install python3-tk
pip3 install shapely
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

### ray_polygon
`
parameters: polygon (array of tuple (x,y))
`

`
return: float
`

### rectangle_polygon_area
`
parameters: polygon (array of tuple (x,y))
`

`
return: float
`

### area_no_used_of_polygon
`
parameters: polygon (array of tuple (x,y))
`

`
return: float
`

### percent_area_no_used_of_polygon
`
parameters: polygon (array of tuple (x,y))
`

`
return: float
`
### minimum_y
`
parameters: polygon (array of tuple (x,y))
`

`
return float
`
### sort:
`
parameters: polygons (array of array of tuple (x,y)), function (
function that determines the ordering)
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

### min_max_points_polygon
`
parameters: polygon (array of tuple (x,y))
`

`
return: float, float, float, float
`

### min_max_points_polygon
`
parameters: polygon (array of tuple (x,y))
`

`
return: float, float, float, float
`

### width_height
`
parameters: polygon (array of tuple (x,y))
`

`
return: float, float
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

### random_solve
`
parameters: array_polygons (array of tuple (x,y), required), x_lim (float, required):
`

`
return: List of type Polygon(), float
`

### better_solution
`
parameters: array_polygons (array of tuple (x,y), required), x_lim (float, required):
`

`
return: List of type Polygon(), float
`


### solve
`
parameters: array_polygons (array of tuple (x,y), required), x_lim (float, required)
function (funtion to solve, required), sort_function (funtion to sort, required):
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

### polygon_overlapping
`
parameters: polygon (array of puple (x,y)) polygons_to_analyze (array of array of puple (x,y))
`

`
return boolean
`