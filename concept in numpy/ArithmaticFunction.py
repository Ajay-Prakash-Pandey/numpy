import numpy as np

arr1=np.array([1,2,3,45,6,65,4,56,7])
print("min: ",np.min(arr1),np.argmin(arr1))
print("max: ",np.max(arr1),np.argmax(arr1))

arr2=np.array([[7,1,9,11,54],[9,7,3,11,15]])
print("min: ",np.min(arr2,axis=1),np.argmin(arr2))
print("max: ",np.max(arr2,axis=0),np.argmax(arr2))

# finding root

print("Root of arr2 is: ",np.sqrt(arr2))

angle=(1,20,30,60)
print("angle of sin: ",np.sin(angle))
print("angle of cos: ",np.cos(angle))


# cumunity sum

print("the sumsum of angle is: ",np.cumsum(angle))