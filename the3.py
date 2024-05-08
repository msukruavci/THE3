def area(Q,T):
    from math import atan2
    deviation = 1e-8
    class edge:
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2
    class point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    def area_polygon(polygon):
        #calculating the area of a polygon by using determinant
        n = len(polygon)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += polygon[i][0] * polygon[j][1]
            area -= polygon[j][0] * polygon[i][1]
        area = abs(area) / 2.0
        return area
    def area_triangle(x1, y1, x2, y2, x3, y3):
         #calculating the area of a polygon by using determinant 
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) 
                    + x3 * (y1 - y2)) / 2.0)
    def isInsideq(Q,Qptslist, t):
        #in order to find triangle corners which is in the quadrant
        ABCD = area_polygon(Q)   
        PAB =  area_triangle(Qptslist[0].x , Qptslist[0].y , t.x, t.y , Qptslist[1].x , Qptslist[1].y)
        PAD = area_triangle(Qptslist[0].x, Qptslist[0].y, t.x, t.y, Qptslist[3].x , Qptslist[3].y)
        PBC = area_triangle(Qptslist[2].x , Qptslist[2].y ,t.x , t.y ,Qptslist[1].x ,Qptslist[1].y)   
        PDC = area_triangle(Qptslist[2].x, Qptslist[2].y , t.x , t.y, Qptslist[3].x, Qptslist[3].y)   
        if(ABCD == PAB + PAD + PBC + PDC):
            return True  
        return False
    def isInsidet(Tptslist, q):
        #in order to find quadrant corners which is in the triangle
          
        ABC = area_triangle (Tptslist[0].x, Tptslist[0].y , Tptslist[1].x, Tptslist[1].y, Tptslist[2].x, Tptslist[2].y)
        PBC = area_triangle(q.x, q.y, Tptslist[1].x, Tptslist[1].y, Tptslist[2].x, Tptslist[2].y)
        PAC = area_triangle (Tptslist[0].x, Tptslist[0].y , q.x, q.y, Tptslist[2].x, Tptslist[2].y)	
        PAB = area_triangle (Tptslist[0].x, Tptslist[0].y , Tptslist[1].x, Tptslist[1].y, q.x, q.y)
        if(ABC == PBC + PAC + PAB):
            return True
        return False
    def equation(edge):
        #in order to find coefficients(a,b) of an equation(ax+b=y)
        if edge.p1.x-edge.p2.x ==0:
            return (edge.p1.x,"X")
        if edge.p1.y-edge.p2.y == 0:
            return ("Y",edge.p1.y)
        m = (edge.p1.y- edge.p2.y) / (edge.p1.x - edge.p2.x)
        return m,(edge.p1.y - (edge.p1.x*m))
    def evaluate(x,edge):
        #in order to find y value at x 
        if not(edge.p1.x >= x >= edge.p2.x or (edge.p1.x <= x <= edge.p2.x)):
            return "Never"
        if "X" in equation(edge):
            return (x,"All")
        if "Y" in equation(edge):
            return equation(edge)[1]
        return  x*equation(edge)[0] + equation(edge)[1] 
    def reveva(y,edge):
        #reverse of evaluate in order to find x value at y 
        if not(edge.p1.y >= y >= edge.p2.y or (edge.p1.y <= y <= edge.p2.y)):
            return "Never"
        a = equation(edge)[0]
        b = equation(edge)[1]
        if("X" in equation(edge)):
            return equation(edge)[0]
        if "Y" in equation(edge):
            if y == equation(edge)[1]:
                return ("All",equation(edge)[1])
            return "Never"
        return (y - b)/a    
    def intersect(edge1,edge2):
        #in order to find intersects of two edges
        if "X" in equation(edge1) and "X" in equation(edge2):
            return False  
        if ("Y" in equation(edge1)) and ("Y" in equation(edge2)):
            return False
        if("X" in equation(edge1)):
            a = evaluate(equation(edge1)[0],edge2)
            if "Never"  != evaluate(equation(edge1)[0],edge2):
                if min(edge1.p1.y,edge1.p2.y)  <= a <= max(edge1.p1.y,edge1.p2.y) :
                    return equation(edge1)[0],a
            return False
        if("X" in equation(edge2)):
            a = evaluate(equation(edge2)[0],edge1)
            if "Never"  != evaluate(equation(edge2)[0],edge1):
                if min(edge2.p1.y,edge2.p2.y)  <= a <= max(edge2.p1.y,edge2.p2.y) :
                    return equation(edge2)[0],a
            return False
        if ("Y" in equation(edge1)):
            a =reveva(equation(edge1)[1],edge2)
            if "Never"  != reveva(equation(edge1)[1],edge2):           
                if min(edge1.p1.x,edge1.p2.x)  <= a <= max(edge1.p1.x,edge1.p2.x) :
                    return a,equation(edge1)[1]
            return False    
        if ("Y" in equation(edge2)):
            a = reveva(equation(edge2)[1],edge1)
            if "Never" != reveva(equation(edge2)[1],edge1):
                if min(edge2.p1.x,edge2.p2.x)  <= a <= max(edge2.p1.x,edge2.p2.x) :
                    return a,equation(edge2)[1]
            return False
        a = equation(edge1)[0]
        b = equation(edge1)[1]
        c = equation(edge2)[0]
        d = equation(edge2)[1]
        if a-c == 0:
            return False
        x = (d-b)/(a-c)
        y = evaluate(x,edge1)
        y2 = evaluate(x,edge2)
        if(type(y2)== float and type(y)==float) or (type(y2)== int and type(y)==int):
            if (y2 - y) <= deviation:
                return (x,y)
        return False
    def order(temppolygon):
        #in order to order points to calculate the area by using determinant
        tanslist = []
        G = [0,0]
        for x,y in temppolygon:
            G[0] += x
            G[1] += y
        corner_count = len(temppolygon)
        if corner_count != 0:
            G[0] = G[0]/corner_count
            G[1] = G[1]/corner_count       
            for x,y in temppolygon:
                tanslist.append(atan2(y-G[1],x-G[0]))
        for arctan in range(len(tanslist)-1,0,-1):
            for i in range(arctan):
                if tanslist[i]>tanslist[i+1]:
                    tanslist[i],tanslist[i+1] = tanslist[i+1],tanslist[i]
                    temppolygon[i],temppolygon[i+1] = temppolygon[i+1],temppolygon[i]
        return temppolygon
    #declaration of variables line by line (corner points)(list of points)(edges)(list of edges)
    Q1,Q2,Q3,Q4,T1,T2,T3 = point(Q[0][0],Q[0][1]),point(Q[1][0],Q[1][1]),point(Q[2][0],Q[2][1]),point(Q[3][0],Q[3][1]),point(T[0][0],T[0][1]),point(T[1][0],T[1][1]),point(T[2][0],T[2][1]) 
    Qptslist ,Tptslist = [Q1,Q2,Q3,Q4],[T1,T2,T3]
    qedge1,qedge2,qedge3,qedge4,tedge1,tedge2,tedge3 = edge(Q1,Q2),edge(Q2,Q3),edge(Q3,Q4),edge(Q4,Q1),edge(T1,T2),edge(T2,T3),edge(T3,T1) 
    edgelines = [qedge1,qedge2,qedge3,qedge4,tedge1,tedge2,tedge3]
    #list which will store the corners of polygon that we have to find
    intersects = []
    cornerlist = []
    #these three for loop for finding points of polygon and storing
    for t in Tptslist:
        if isInsideq(Q,Qptslist, t):
            cornerlist.append((t.x,t.y))
    for q in Qptslist:
        if (isInsidet(Tptslist, q)):
            cornerlist.append((q.x,q.y))
    for edge1 in edgelines[:4]:
        for edge2 in edgelines[4:]:
            if(intersect(edge1,edge2)):
                if("Never" not in intersect(edge1,edge2)):
                    intersects.append(intersect(edge1,edge2))
    temppolygon = list(set(cornerlist+intersects))
    polygon = order(temppolygon)
    return area_polygon(polygon)


