# Optimizing the picking and putaway problem as tsp problem.
## Code files Structure
    1) netmeds_picking_optimization.py  (python file)
    2) overall.csv (csv file)
    3) Requirements text (txt file)
### Input format 
    In the source code, the nodes variable has to be updated with the picklist or passing the picklist as argumnets to the program.
    Pick list in the format of list of elements 
        elements format : {aisle number}_{rack number}
    e.g = 
       If picklist conntains elements from aisle 1 rack 11 , aisle 2 rack 12 , aisle 10 rack 20 , aisle 20 rack 3 then input format should match with the given below(order of elemnts is not considered)
       [ "1_11" , "2_12" , "10_20" , "20_3"]
    
### How to run program ?
    If picklist conntains elements from aisle 1 rack 11 , aisle 2 rack 12 , aisle 10 rack 20 , aisle 20 rack 3 then input format should match with the given below(order of elemnts is not considered)
       [ "1_11" , "2_12" , "10_20" , "20_3"]
    
    In source code update nodes variable and run the program
    or 
    Run the program by passing the input as arguments in commad prompt
    python  netmeds_picking_optimization.py 1_11 2_12 10_20 20_3

### Ouptput format 
    Two lines of output:
    1) 1st line contains the order in which elemets have to be picked for optimal path.
    2) 2nd line contains the fitness value of the path, lesser the fitness more optimal is the path.