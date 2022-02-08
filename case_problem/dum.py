class FormatAndSortNames():

    person_lst = []


    def __init__(self,person_lst):
        self.person_lst = person_lst

    #Using class method to parse and set class attribute instead of using constructors
    @classmethod
    def name_format(cls,people):
        tmp_lst = []
        for person in people:
            name = ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
            age = person[2]
            tmp_lst.append((name,age))

        person_lst = tmp_lst

        return cls(person_lst)
    

    def sort_ages(self):
        tup = self.person_lst
        lst = len(tup) 
        for i in range(0, lst): 
          
            for j in range(0, lst-i-1): 
                if (tup[j][1] > tup[j + 1][1]): 
                    temp = tup[j] 
                    tup[j]= tup[j + 1] 
                    tup[j + 1]= temp 
        return tup
    

    def show_names(self,names):
        for i in names:
            name,age = i
            print(name)
        
    


    
if __name__ == '__main__':
    n_people = int(input())

    people = [input().split() for i in range(n_people)]

    FormatObj = FormatAndSortNames.name_format(people)
    result = FormatObj.sort_ages()
    FormatObj.show_names(result)


    

    
