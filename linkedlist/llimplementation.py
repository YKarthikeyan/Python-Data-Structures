from linkedlist.LinkedList import LinkedList

mylist = LinkedList();
mylist.insertlast(12);
mylist.insertfirst(121);
mylist.insertlast(4);
mylist.insertfirst(81);
mylist.insertlast(1);
mylist.insertlast(2);
mylist.insertlast(3);
mylist.insertlast(4);

mylist.traverselist();
size = mylist.size();
print("size is : ",size)

mylist.search(1);
mylist.search(4);

mylist.remove(121);
mylist.traverselist();
size = mylist.size();
print("size is : ",size)

mylist.remove(121);
mylist.traverselist();
size = mylist.size();
print("size is : ",size)

mylist.remove(2);
mylist.traverselist();
size = mylist.size();
print("size is : ",size)

mylist.remove(4);
mylist.traverselist();
size = mylist.size();
print("size is : ",size)

mylist.remove(1);
mylist.traverselist();
size = mylist.size();
print("size is : ",size)

mylist.search(1);

