from sklearn.model_selection import train_test_split
x= [[1],[2],[3],[4],[5],[6],[7],[8]]
y= [3,5,7,9,11,13,15,17]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
print("X Train:", x_train)
print("X Test:", x_test)
print("Y Train:", y_train)
print("Y Test:", y_test)