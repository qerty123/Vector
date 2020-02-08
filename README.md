# Python module for working with vectors of different dimensionality
This module is designed for numerical operations with vectors of different dimensions. 
The module consists of classes:
* Vector (main class with basic functions. May contain vectors of any demension)
* Vector2d (chaild class of Vector. Workpiece for vector with two coordinates)
* Vector3d (chaild class of Vector. Workpiece for vector with three coordinates)

# Basic functions
* length - return length of vector
* length_squared - return squared length of vector
* normalize - just return another vector with single length
* set_normalized - set current vector single length
* velocity(dtime, *new_values) - calculates the velocity vector
* velocity_ema(rate, dtime, *new_values) - exponential moving average function
* dot(vector) - scalar multiplication of vectors
* angle(vector) - return angle between current vector and another vector
* project(vector) - projection to another vector
* reject(vector) - reverse projection
* reflect(vector) - calculate reflecting vector
* nreflect(vector) - normalized reflect vector
