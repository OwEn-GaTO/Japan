import sys,os
#elias Quiñones Jaime se hace pasar por desarrollador de roblox jajaja


class Nagasaki:
    def __init__(self,name,sizeX = 1,sizeY = 1,expandable = True,fragmenter = "ç~`|~!ç",extension = "senior"):
        self.name = name
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.expandable = expandable
        self.fragmenter = fragmenter
        self.extension = "."+extension
        if expandable:
            self.adder = 1 
        else:
            self.adder = 0
        self.ok = Osaka(fragmenter = fragmenter,extension = self.extension)
        if not os.path.exists(f"{self.name}.senior"):
            self.__createdb()
            
    def __createdb(self):
        if self.expandable == False:
                self.ok.create_database(self.name,self.sizeX,self.sizeY)
        elif self.expandable == True:
                self.adder = 1
                self.ok.create_database(self.name,4,1)
                self.ok.write_array(self.name,[[self.name,"dynamic","dynamic",self.expandable]])

    def getsizeY(self):
        return self.ok.sizeY(self.name,adder = self.adder)
    def getsizeX(self):
        return self.ok.sizeX(self.name,adder = self.adder)
    def getline(self,numline):
        return self.ok.read_row(self.name,numline+self.adder)
    def getcolum(self,numcolum):
        return self.ok.read_colum(self.name,numcolum,adder = self.adder)
    def setpoint(self,val,pointY,pointX):
        self.ok.write_cordinate(self.name,val,pointX,pointY,adder = self.adder)
    def getpoint(self,pointY,pointX):
        return self.ok.read_cordinate(self.name,pointX,pointY + self.adder)
    def setline(self,val,numline):
        
        if numline > self.ok.sizeY(self.name,adder = self.adder) or numline == 0:
            self.ok.append(self.name,val)
        sizex = self.getsizeX()
       
        if type(sizex) == list:
            sizex = sorted(sizex)[0] 
        elif len(val) <= sizex:
            for i in range(1,len(val) + 1):
               
                self.ok.write_cordinate(self.name,val[i - 1],i,numline + self.adder,adder = self.adder)
        else:
            if len(val) > self.ok.sizeY(self.name):
                with open(f"{self.name}.senior","r") as f:
                    data = f.read()
                with open(f"{self.name}.senior","w") as f:
                    f.write(data)
                    
                    line = ""
                    ltj = len(data.split("\n")[0]) + 2
                    for j in range(self.adder,numline):
                        ltj += len(data.split("\n")[j]) + 2
                    f.seek(ltj)
                    for i in range(0,len(val)):
                        line += str(val[i]) + self.fragmenter
                    e = ""
                    if len(line) < len(data.split("\n")[numline]):
                        for i in range(0,len(data.split("\n")[numline])):
                            e += " "
                        f.write(e)      
                    f.seek(ltj)
                    f.write(line+"\n")    
            else:
              self.ok.write_row(self.name,numline+self.adder,val,adder=self.adder)    
    def setcolum(self,val,numcolum):
        sizex = self.getsizeX()
       
        if type(sizex) == list:
            sizex = sorted(sizex)[0] 
        if len(val) == self.getsizeY() and numcolum <= sizex:
          
            self.ok.write_colum(self.name,numcolum,val,adder = self.adder)
        else:
            if not numcolum <= sizex and not len(val) == self.getsizeY():
                print(f"the length of val({len(val)}) is greater than the number of lines({self.getsizeY()}) AND column index({numcolum}) is greater than number of attributes({sizex})")

            elif not numcolum <= sizex:
                print(f"column index({numcolum}) is not equal to the number of attributes({sizex})")
            elif not len(val) <= self.getsizeY():
                print(f"the length of val({len(val)}) is greater than the number of lines({self.getsizeY()})")
            else:
                print("An unknown error has occurred, please report the error along with your code at https://github.com/OwEn-GaTO/Japan/issues")

class Osaka:
    def __init__(self,fragmenter = "ç~`|~!ç",extension = ".senior"):
        self.fragmenter = fragmenter
        self.extension = extension
    def read_row(self,name,row,adder):
        ret = []
        for i in range(1 + adder,self.sizeX(name)[row - 1] + 1):
            ret.append(self.read_cordinate(name,i,row))
        return ret    

    def read_colum(self,name,colum,adder):
        ret = []
        for i in range(1 + adder,self.sizeY(name)+1):
            ret.append(self.read_cordinate(name,colum,i))
        return ret  
    def write_row(self,name,row,array,adder = 0):
        for i in range(1,len(array) + 1):
            self.write_cordinate(name,array[i - 1],i,row + adder,adder = adder)
    def write_colum(self,name,colum,array,adder = 0):

        for i in range(1 + adder,self.sizeY(name) + adder):
           
            self.write_cordinate(name,array[i - 1 - adder],colum,i,adder = adder,cadder = adder)
    def append(self,name,array):
      

        filename = name + self.extension
        #inicia #comprobar si el tamaño de la base de datos coincide con el tamaño del array
        file1 = open(filename,"r")
        lines1 = file1.read()
        file1.close()
        AsizeX = len(array)
        FsizeX = lines1.split("\n")[0].count(self.fragmenter)

    

        file = open(filename,"a")


        finalArray = []

        for i in range(0, AsizeX):
            val = str(array[i]) + self.fragmenter
            finalArray.append(val)
            file.write(finalArray[i])
        file.write("\n")
        file.close()

    def delete_database(self,name):
        os.remove(name+self.extension)




    def create_database(self,name,sizeX,sizeY):


        filename = name+self.extension
        if os.path.isfile(filename)==True:
           print(f"{name} database already exist")
           sys.exit(2)
        file = open(filename,"w")
        array = []
        for j in range(0,sizeY):
            array.append([])
        for i in range(0,len(array)):


            for t in range(0,sizeX):
                array[i].append(f" {self.fragmenter} ")

        for n in range(0,len(array)):
            for m in range(0,sizeX):
                file.write(array[n][m])
            file.write("\n")

        file.close()

    def sizeY(self,name,adder = 0):
        filename = name + self.extension
        file = open(filename,"r")
        lines1 = file.read()
        file.close()
        resultado1=lines1.splitlines()
        numn1 = len(resultado1)
        return int(numn1) - adder
    def sizeX(self,name,adder = 0):
        filename = name + self.extension
        file = open(filename,"r")
        lines1 = file.read()
        file.close()
        FsizeX = lines1.split("\n")[adder].count(self.fragmenter)
        ret = []
        for i in range(adder,self.sizeY(name,adder = adder) + adder):
            ret.append(lines1.split("\n")[i].count(self.fragmenter))

        if ret.count(ret[0]) == len(ret):
                return ret[0]
        else: 
            return ret



    def read_database(self,name,mode):
        nk = Nagasaki(name,expandable = False)
        sizex = nk.getsizeX()
       
        if type(sizex) == list:
            sizex = sorted(sizex)[-1] 
        db = Osaka()
        filename = name + self.extension
        file = open(filename,"r")
        read = file.read()
        file.close()
        text = ""
        if mode == "text n":
           for i in range(1, db.sizeY(name) + 1):
               for j in range(1,sizex - 1):
                    text += db.read_cordinate(name, j,i) + " "
               text += "\n"
           return text
        if mode == "text wn":
           for i in range(1, db.sizeY(name) + 1):
               for j in range(1,sizex - 1):
                    text += db.read_cordinate(name, j,i) + " "
           return text
        if mode == "list wn":

           for i in range(1, db.sizeY(name) + 1):
               for j in range(1,sizex - 1):
                    text += db.read_cordinate(name, j,i)
           text2 = list(text)
           return list(text2)
        if mode == "list n":

           for i in range(1, db.sizeY(name) + 1):
               for j in range(1,sizex - 1):
                    text += db.read_cordinate(name, j,i)
               text += "\n"
           text2 = list(text)
           return list(text2)
        return read

    def write_array(self,name,array):
        filename = name + self.extension
        #inicia#comprobar si el tamaño de la base de datos coincide con el tamaño del array
        file1 = open(filename,"r")
        lines1 = file1.read()
        file1.close()
        resultado1=lines1.splitlines()
        numn1 = len(resultado1)
        AsizeY = len(array)
        AsizeX = len(array[0])
        FsizeY = numn1
        FsizeX = lines1.split("\n")[0].count(self.fragmenter)
        

       
        #termina#comprobar si el tamaño de la base de datos coincide con el tamaño del array


        file = open(filename,"w")
        finalArray = []

        for i in range(0,AsizeY):
            finalArray.append([])
        for n in range(0,AsizeY):
            for m in range(0,AsizeX):
               val = str(array[n][m])+self.fragmenter
               finalArray[n].append(val)


        for s in range(0,len(array)):
            for r in range(0,AsizeX):
                file.write(finalArray[s][r])
            file.write("\n")
        file.close()
    def read_cordinate(self,name,X,Y):
        filename = name+self.extension
        file = open(filename,"r")

        line = file.readlines()[Y - 1]
        line = line.split(self.fragmenter)[X - 1]
        return line
    def write_cordinate(self,name,val,X,Y,adder = 0,cadder = 0):
        filename = name+self.extension
        lines = open(filename,"r").read()
        lines = lines.split("\n")
        lines2 = []
      
        for i in range(0,len(lines) - 1):
            lines2.append(lines[i].split(self.fragmenter)) 
       
     
        for j in range(0,len(lines2)):
            lines2[j].pop(-1)
        a = 0
        if adder == 0:
            a = 1
         

        lines2[Y - a - cadder][X - 1] = val
        file = open(filename,"w")
     
        for t in lines2:
            for i in t:
                
                file.write(str(i)+self.fragmenter)
            file.write("\n")  
        file.close()  


